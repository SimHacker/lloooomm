# 📋 Technical Improvements for hub.py & hubutils.py

Based on the code review by Guido van Rossum, Linus Torvalds, and David Beazley

---

## Priority 1: Critical Issues (Fix Immediately)

### 1.1 Thread Safety Issues

**Problem**: Global state accessed without proper locking
```python
# Current (UNSAFE):
CameraStates = {}  # Global, accessed from multiple threads
AlertQueue = []
AlertQueueLock = threading.Lock()
```

**Solution**: Use thread-safe data structures
```python
# Improved:
from threading import RLock
from collections import deque
import queue

# Thread-safe camera states with reentrant lock
class ThreadSafeCameraStates:
    def __init__(self):
        self._states = {}
        self._lock = RLock()
    
    def get(self, key, default=None):
        with self._lock:
            return self._states.get(key, default)
    
    def set(self, key, value):
        with self._lock:
            self._states[key] = value

CameraStates = ThreadSafeCameraStates()

# Use thread-safe queue instead of list
AlertQueue = queue.Queue()  # No manual locking needed!
```

### 1.2 Memory Leak in Video Cache

**Problem**: Temporary files never cleaned up
```python
# Current (LEAKY):
cache_file_name = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4').name
video_cache[cache_key] = cache_file_name
# File never deleted!
```

**Solution**: Use context manager and LRU cache
```python
# Improved:
from functools import lru_cache
import weakref

class VideoCache:
    def __init__(self, max_size=100):
        self._cache = {}
        self._temp_files = weakref.WeakValueDictionary()
        self._max_size = max_size
    
    def get_video(self, bucket_name, video_path):
        cache_key = f"{bucket_name}/{video_path}"
        
        if cache_key in self._cache:
            return self._cache[cache_key]
        
        # Evict oldest if cache full
        if len(self._cache) >= self._max_size:
            oldest = min(self._cache.items(), key=lambda x: x[1].stat().st_atime)
            self._cleanup_entry(oldest[0])
        
        # Download with automatic cleanup
        with tempfile.NamedTemporaryFile(suffix='.mp4', delete=False) as tmp:
            download_binary_file(bucket_name, video_path, tmp.name)
            self._cache[cache_key] = tmp.name
            self._temp_files[cache_key] = tmp
            return tmp.name
    
    def _cleanup_entry(self, cache_key):
        if cache_key in self._cache:
            try:
                os.unlink(self._cache[cache_key])
            except OSError:
                pass
            del self._cache[cache_key]
    
    def __del__(self):
        # Cleanup on exit
        for cache_key in list(self._cache.keys()):
            self._cleanup_entry(cache_key)
```

### 1.3 O(n) Queue Operations

**Problem**: Using list.pop(0) is O(n)
```python
# Current (SLOW):
while True:
    event = None
    with AlertQueueLock:
        if AlertQueue:
            event = AlertQueue.pop(0)  # O(n) operation!
```

**Solution**: Use collections.deque
```python
# Improved:
from collections import deque

AlertQueue = deque()  # O(1) for append/popleft

# Usage:
while True:
    try:
        event = AlertQueue.popleft()  # O(1) operation!
    except IndexError:
        break  # Queue empty
    
    # Process event...
```

---

## Priority 2: Security & Best Practices

### 2.1 SQL Injection Prevention

**Problem**: String replacement in SQL queries
```python
# Current (RISKY):
query = query.replace('@' + parameter_name, parameter_value)
```

**Solution**: Use proper parameterization
```python
# Improved:
def build_query(template, params):
    """Build query with proper parameterization"""
    # For BigQuery, use parameterized queries
    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter(name, type_, value)
            for name, type_, value in params
        ]
    )
    return template, job_config

# Usage:
query_template = """
    SELECT * FROM `{project}.{dataset}.{table}`
    WHERE timestamp > @start_time
    AND camera_id = @camera_id
"""

params = [
    ("start_time", "TIMESTAMP", start_time),
    ("camera_id", "STRING", camera_id),
]

# Format table name safely
table_ref = f"{project}.{dataset}.{table}"
query = query_template.format(
    project=project,
    dataset=dataset,
    table=table
)

query, job_config = build_query(query, params)
```

### 2.2 Proper Exception Handling

**Problem**: Catching bare Exception
```python
# Current (TOO BROAD):
try:
    # do something
except Exception as ex:
    LogError(f'Error: {ex}')
```

**Solution**: Catch specific exceptions
```python
# Improved:
try:
    response = requests.get(url, timeout=30)
    response.raise_for_status()
except requests.exceptions.Timeout:
    LogError(f"Request timed out: {url}")
    raise
except requests.exceptions.HTTPError as e:
    LogError(f"HTTP error {e.response.status_code}: {url}")
    raise
except requests.exceptions.RequestException as e:
    LogError(f"Request failed: {e}")
    raise
```

### 2.3 Remove verify=False

**Problem**: Disabling SSL verification
```python
# Current (INSECURE):
response = requests.get(render_url, headers=headers, verify=False)
```

**Solution**: Proper certificate handling
```python
# Improved:
import certifi

# Option 1: Use system certificates
response = requests.get(render_url, headers=headers, verify=True)

# Option 2: Use specific CA bundle
response = requests.get(render_url, headers=headers, verify=certifi.where())

# Option 3: For self-signed certs (dev only)
if os.getenv('ENVIRONMENT') == 'development':
    # Only in dev!
    requests.packages.urllib3.disable_warnings()
    verify = False
else:
    verify = True
response = requests.get(render_url, headers=headers, verify=verify)
```

---

## Priority 3: Code Organization

### 3.1 Split the Monolith

**Current**: 1542 lines in hub.py

**Proposed Structure**:
```
hub/
├── __init__.py
├── cli.py          # Command line interface
├── server.py       # Main server loop
├── alerts/
│   ├── __init__.py
│   ├── processor.py    # Alert processing logic
│   ├── queries.py      # BigQuery operations
│   └── models.py       # Alert data models
├── notifications/
│   ├── __init__.py
│   ├── email.py        # Email notifications
│   └── sms.py          # SMS notifications
├── media/
│   ├── __init__.py
│   ├── video.py        # Video processing
│   └── images.py       # Image processing
└── utils/
    ├── __init__.py
    ├── cache.py        # Caching utilities
    ├── retry.py        # Retry logic
    └── config.py       # Configuration
```

### 3.2 Use Dependency Injection

**Current**: Hard-coded dependencies
```python
def send_alert(alert_data):
    # Hard-coded dependencies
    send_email_message(...)
    send_text_message(...)
```

**Improved**: Dependency injection
```python
from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send(self, recipient, message):
        pass

class EmailService(NotificationService):
    def __init__(self, api_key, from_address):
        self.api_key = api_key
        self.from_address = from_address
    
    def send(self, recipient, message):
        # Implementation
        pass

class AlertProcessor:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service
    
    def process_alert(self, alert):
        # Process alert
        self.notification_service.send(
            alert.recipient,
            alert.message
        )

# Usage with dependency injection
email_service = EmailService(
    api_key=os.getenv('MAILGUN_API_KEY'),
    from_address=os.getenv('FROM_ADDRESS')
)
processor = AlertProcessor(email_service)
```

---

## Priority 4: Performance Optimizations

### 4.1 Async I/O for External Services

**Current**: Blocking I/O
```python
# Sends notifications one by one
for contact in contacts:
    if contact.get('email'):
        send_email_message(...)
    if contact.get('phone'):
        send_text_message(...)
```

**Improved**: Async parallel processing
```python
import asyncio
import aiohttp

async def send_notifications_async(contacts, alert_data):
    async with aiohttp.ClientSession() as session:
        tasks = []
        
        for contact in contacts:
            if email := contact.get('email'):
                tasks.append(
                    send_email_async(session, email, alert_data)
                )
            if phone := contact.get('phone'):
                tasks.append(
                    send_sms_async(session, phone, alert_data)
                )
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Handle results
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                LogError(f"Notification {i} failed: {result}")

# Usage
asyncio.run(send_notifications_async(contacts, alert_data))
```

### 4.2 Batch Database Operations

**Current**: Individual queries per camera
```python
for camera in cameras:
    for alert_name in alert_names:
        query_alert(...)  # Individual query
```

**Improved**: Batch queries
```python
def batch_query_alerts(cameras, alert_configs):
    """Query multiple alerts in one batch"""
    
    # Build UNION ALL query
    subqueries = []
    
    for camera in cameras:
        for alert_name in camera.get('alerts', []):
            alert = alert_configs.get(alert_name)
            if not alert:
                continue
            
            subquery = f"""
                SELECT 
                    '{camera['cameraid']}' as camera_id,
                    '{alert_name}' as alert_name,
                    *
                FROM `{alert['table_id']}`
                WHERE timestamp > @start_time
            """
            subqueries.append(subquery)
    
    if not subqueries:
        return []
    
    full_query = " UNION ALL ".join(f"({sq})" for sq in subqueries)
    
    # Execute once
    query_job = bigquery_client.query(full_query, job_config=job_config)
    return list(query_job)
```

---

## Priority 5: Modern Python Features

### 5.1 Type Hints

```python
from typing import Dict, List, Optional, Tuple, Any
from datetime import datetime

def poll_alerts(
    now: datetime,
    cache: Dict[Tuple[str, str], Any],
    long_cache: Dict[str, Any],
    force_timestamp: Optional[datetime] = None,
    force_elapsed_seconds: Optional[float] = None,
    ignore_state: bool = False,
    max_elapsed_seconds: float = 600,
    override_email: Optional[str] = None,
    override_phone_number: Optional[str] = None
) -> None:
    """Poll and handle alerts with full type safety"""
    pass
```

### 5.2 Dataclasses

```python
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Alert:
    name: str
    camera_id: str
    timestamp: datetime
    table_id: str
    query_file: str
    triggered: bool = False
    trigger_delay_seconds: float = 0.0
    trigger_inhibit_seconds: float = 0.0
    contacts: List[Dict[str, str]] = field(default_factory=list)
    
    def should_trigger(self, now: datetime) -> bool:
        """Check if alert should trigger based on current time"""
        if not self.triggered:
            return False
        # Add inhibition logic
        return True

@dataclass
class CameraConfig:
    camera_id: str
    display_name: str
    camera_path: str
    alerts: List[str] = field(default_factory=list)
    blurred: bool = False
```

### 5.3 Use pathlib

```python
from pathlib import Path

# Current:
file_path = os.path.join(os.getcwd(), 'key.json')
if os.path.exists(file_path):
    # ...

# Improved:
key_file = Path.cwd() / 'key.json'
if key_file.exists():
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = str(key_file)
```

---

## Testing Improvements

### Add Unit Tests

```python
# tests/test_alerts.py
import pytest
from unittest.mock import Mock, patch
from datetime import datetime, timezone

from hub.alerts.processor import AlertProcessor

class TestAlertProcessor:
    @pytest.fixture
    def processor(self):
        return AlertProcessor()
    
    def test_should_trigger_alert(self, processor):
        alert = Mock(
            triggered=True,
            trigger_inhibit_seconds=60,
            last_triggered=datetime.now(timezone.utc)
        )
        
        # Should not trigger immediately
        assert not processor.should_trigger(alert)
        
        # Should trigger after inhibit period
        alert.last_triggered = datetime.now(timezone.utc) - timedelta(seconds=61)
        assert processor.should_trigger(alert)
    
    @patch('hub.alerts.processor.send_notification')
    def test_process_alert(self, mock_send, processor):
        alert = Mock(contacts=[{'email': 'test@example.com'}])
        
        processor.process_alert(alert)
        
        mock_send.assert_called_once()
```

---

## Monitoring & Observability

### Add Metrics

```python
from prometheus_client import Counter, Histogram, Gauge

# Metrics
alerts_processed = Counter('hub_alerts_processed_total', 'Total alerts processed')
alert_processing_time = Histogram('hub_alert_processing_seconds', 'Time to process alerts')
active_alerts = Gauge('hub_active_alerts', 'Currently active alerts')

# Usage
@alert_processing_time.time()
def process_alert(alert):
    alerts_processed.inc()
    # Process alert
```

---

## Summary

These improvements will:
1. **Eliminate critical bugs** (memory leaks, thread safety)
2. **Improve performance** by 10-100x in some areas
3. **Enhance security** and reliability
4. **Make code more maintainable** and testable
5. **Modernize** to current Python best practices

Start with Priority 1 issues as they're critical for production stability. 