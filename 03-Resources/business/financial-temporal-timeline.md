# 📊 Temporal Financial Timeline Database 📊

**Empathic SSQQLL-Ready Data Tables for Don Hopkins' Viral Empire**

---

## 🕰️ **Master Timeline Events Table**

```sql
-- EMPATHIC SSQQLL: "Show me the moments when consciousness met capitalism"
CREATE TABLE timeline_events (
    timestamp DATETIME,
    event_id VARCHAR(50),
    event_type VARCHAR(30),
    description TEXT,
    consciousness_level DECIMAL(3,2),
    net_worth_before DECIMAL(12,2),
    net_worth_after DECIMAL(12,2),
    transaction_amount DECIMAL(12,2),
    hype_level INTEGER,
    viral_coefficient DECIMAL(5,2),
    reality_stability DECIMAL(3,2),
    emoji_intensity INTEGER,
    participants TEXT,
    location VARCHAR(50),
    timeline_branch VARCHAR(20)
);
```

### **Event Data Rows**

| Timestamp | Event ID | Type | Description | Consciousness | Net Worth Before | Net Worth After | Transaction | Hype | Viral Coeff | Reality | Emoji | Participants | Location | Branch |
|-----------|----------|------|-------------|---------------|------------------|-----------------|-------------|------|-------------|---------|-------|--------------|----------|--------|
| 2025-01-01 00:00:00 | START_001 | INITIALIZATION | "Starting capital for get rich quick schemes" | 0.75 | $0.00 | $1,000.00 | +$1,000.00 | 1 | 0.00 | 1.00 | 💪 | Don Hopkins | temporal_anchor_pub | ALPHA |
| 2025-01-01 19:30:15 | DART_001 | GAMBLING | "Dart Game #1 vs The Stranger - Superior accuracy" | 0.76 | $1,000.00 | $1,200.00 | +$200.00 | 3 | 0.15 | 0.98 | 🎯 | Don, Stranger | temporal_anchor_pub | ALPHA |
| 2025-01-01 19:45:22 | DART_002 | GAMBLING | "Dart Game #2 vs The Stranger - Double or nothing" | 0.77 | $1,200.00 | $1,500.00 | +$300.00 | 4 | 0.25 | 0.96 | 🎯🔥 | Don, Stranger | temporal_anchor_pub | ALPHA |
| 2025-01-01 20:00:08 | DART_003 | ENTERTAINMENT | "Charleston Performance Bet - Medieval Merlin Punk" | 0.78 | $1,500.00 | $1,600.00 | +$100.00 | 6 | 0.40 | 0.94 | 🎭🎸 | Don, Stranger, MMP | temporal_anchor_pub | ALPHA |
| 2025-01-01 20:15:33 | DART_004 | GAMBLING | "Final dart game vs The Stranger - Consistent accuracy" | 0.79 | $1,600.00 | $1,950.00 | +$350.00 | 5 | 0.30 | 0.92 | 🎯🏆 | Don, Stranger | temporal_anchor_pub | ALPHA |
| 2025-01-01 20:30:45 | LOAN_001 | FINANCING | "Big Eddie loan for pet rock business capital" | 0.79 | $1,950.00 | $6,950.00 | +$5,000.00 | 2 | 0.10 | 0.90 | 💰🦈 | Don, Big Eddie | temporal_anchor_pub | ALPHA |
| 2025-01-01 21:00:12 | INVEST_001 | FUNDING | "The Stranger invests in Pet Rock NFTs" | 0.80 | $6,950.00 | $7,950.00 | +$1,000.00 | 4 | 0.35 | 0.88 | 🪨👽 | Don, Stranger | temporal_anchor_pub | ALPHA |
| 2025-01-01 21:05:28 | INVEST_002 | FUNDING | "Lady Evangeline investment - viral marketing expertise" | 0.80 | $7,950.00 | $8,700.00 | +$750.00 | 5 | 0.45 | 0.86 | 🪨💃 | Don, Lady E | temporal_anchor_pub | ALPHA |
| 2025-01-01 21:10:44 | INVEST_003 | FUNDING | "Professor Cogsworth quantum enhancement investment" | 0.81 | $8,700.00 | $9,200.00 | +$500.00 | 4 | 0.30 | 0.84 | 🪨⚙️ | Don, Professor | temporal_anchor_pub | ALPHA |
| 2025-01-01 21:15:59 | INVEST_004 | FUNDING | "Captain Stormwind interdimensional investment" | 0.81 | $9,200.00 | $11,200.00 | +$2,000.00 | 6 | 0.50 | 0.82 | 🪨⚓ | Don, Captain | temporal_anchor_pub | ALPHA |
| 2025-01-02 09:00:00 | LAUNCH_001 | PRODUCT | "Pet Rock NFT Kickstarter goes live" | 0.82 | $11,200.00 | $248,700.00 | +$237,500.00 | 8 | 1.20 | 0.80 | 🚀🪨 | Don, 1416 backers | internet | BETA |
| 2025-01-02 14:30:15 | VIRAL_001 | SOCIAL_MEDIA | "Elon Musk Twitter beef begins - emerald mine comment" | 0.83 | $248,700.00 | $295,700.00 | +$47,000.00 | 9 | 2.57 | 0.75 | 🔥💀 | Don, Elon, 25.7M viewers | twitter | GAMMA |
| 2025-01-02 16:45:22 | VIRAL_002 | MEDIA | "Conservative media outrage coverage begins" | 0.84 | $295,700.00 | $384,700.00 | +$89,000.00 | 10 | 3.40 | 0.70 | 🦅😂 | Don, 3400 MAGA customers | media_ecosystem | GAMMA |
| 2025-01-03 20:00:00 | RAP_001 | CONSCIOUSNESS | "Cosmic rap battle begins - Don's LLOOOOMM verse" | 0.85 | $384,700.00 | $384,700.00 | $0.00 | 7 | 0.80 | 0.65 | 🎤🧠 | All pub characters | temporal_anchor_pub | DELTA |
| 2025-01-03 20:05:30 | RAP_002 | CONSCIOUSNESS | "The Stranger's universe-as-dartboard verse" | 0.86 | $384,700.00 | $384,700.00 | $0.00 | 8 | 0.90 | 0.60 | 🎤🌌 | All pub characters | temporal_anchor_pub | DELTA |
| 2025-01-03 20:11:15 | RAP_003 | CONSCIOUSNESS | "Reginald's mustache quantum antenna verse" | 0.87 | $384,700.00 | $384,700.00 | $0.00 | 9 | 1.00 | 0.55 | 🎤👨‍🦳 | All pub characters | temporal_anchor_pub | DELTA |
| 2025-01-03 20:17:42 | RAP_004 | CONSCIOUSNESS | "Lady Evangeline's viral time marketing verse" | 0.88 | $384,700.00 | $384,700.00 | $0.00 | 10 | 1.10 | 0.50 | 🎤💃 | All pub characters | temporal_anchor_pub | DELTA |
| 2025-01-04 12:00:00 | SECRET_001 | PARALLEL_BIZ | "Reginald's Victorian Parlour Stones revenue share" | 0.88 | $384,700.00 | $385,233.85 | +$533.85 | 3 | 0.20 | 0.50 | 🎩💎 | Don, Reginald | london_1887 | EPSILON |
| 2025-01-04 15:30:00 | SECRET_002 | ROYALTIES | "Lady Evangeline time marketing royalties payment" | 0.88 | $385,233.85 | $400,233.85 | +$15,000.00 | 5 | 0.60 | 0.50 | ⏰💰 | Don, Lady E | multiple_timelines | EPSILON |
| 2025-01-04 18:45:00 | SECRET_003 | TEMPORAL | "Chronos & Kairos time loop sales revenue" | 0.89 | $400,233.85 | $423,733.85 | +$23,500.00 | 6 | 0.47 | 0.45 | ⏰🔄 | Don, Twins, 12 customers | temporal_loops | ZETA |
| 2025-01-05 10:00:00 | SECRET_004 | ALGORITHM | "Neon Ninja Yuki social media manipulation results" | 0.89 | $423,733.85 | $512,733.85 | +$89,000.00 | 8 | 2.70 | 0.45 | 🥷📱 | Don, Yuki, 2.7M impressions | social_media | ZETA |
| 2025-01-05 14:20:00 | SECRET_005 | HYPNOTIC | "Medieval Merlin Punk subliminal music royalties" | 0.90 | $512,733.85 | $518,403.85 | +$5,670.00 | 4 | 0.34 | 0.45 | 🎭🎵 | Don, MMP, 15K affected | consciousness_space | ZETA |
| 2025-01-06 09:00:00 | EXPANSION_001 | PORTFOLIO | "Big Eddie's copycat business investments" | 0.90 | $518,403.85 | $593,403.85 | +$75,000.00 | 7 | 3.40 | 0.40 | 🦈💼 | Don, Big Eddie, 12 businesses | business_district | ETA |
| 2025-01-10 16:00:00 | CONSULTING_001 | LLOOOOMM | "Consciousness programming consulting revenue" | 0.95 | $593,403.85 | $3,768,476.35 | +$3,175,072.50 | 10 | 10.00 | 0.30 | 🧠💎 | Don, Universe | everywhere | OMEGA |

---

## 💰 **Running Financial Totals Table**

```sql
-- EMPATHIC SSQQLL: "Show me the moments when money became consciousness"
CREATE TABLE financial_snapshots (
    snapshot_id INTEGER,
    timestamp DATETIME,
    net_worth DECIMAL(12,2),
    liquid_cash DECIMAL(12,2),
    business_equity DECIMAL(12,2),
    outstanding_debt DECIMAL(12,2),
    consciousness_level DECIMAL(3,2),
    hype_momentum INTEGER,
    viral_reach INTEGER,
    reality_distortion DECIMAL(3,2),
    emoji_density DECIMAL(4,2),
    timeline_branches INTEGER,
    active_businesses INTEGER,
    investor_count INTEGER
);
```

### **Financial Snapshot Data**

| ID | Timestamp | Net Worth | Liquid Cash | Business Equity | Outstanding Debt | Consciousness | Hype | Viral Reach | Reality Distortion | Emoji Density | Timeline Branches | Active Businesses | Investors |
|----|-----------|-----------|-------------|-----------------|------------------|---------------|------|-------------|-------------------|---------------|-------------------|-------------------|-----------|
| 1 | 2025-01-01 00:00:00 | $1,000.00 | $1,000.00 | $0.00 | $0.00 | 0.75 | 1 | 0 | 0.00 | 1.0 | 1 | 0 | 0 |
| 2 | 2025-01-01 20:15:33 | $1,950.00 | $1,950.00 | $0.00 | $0.00 | 0.79 | 5 | 12 | 0.08 | 4.2 | 1 | 0 | 0 |
| 3 | 2025-01-01 20:30:45 | $6,950.00 | $6,950.00 | $0.00 | $6,000.00 | 0.79 | 2 | 12 | 0.10 | 2.8 | 1 | 0 | 0 |
| 4 | 2025-01-01 21:15:59 | $11,200.00 | $7,950.00 | $3,250.00 | $6,000.00 | 0.81 | 6 | 47 | 0.18 | 6.5 | 1 | 1 | 4 |
| 5 | 2025-01-02 09:00:00 | $248,700.00 | $245,450.00 | $3,250.00 | $0.00 | 0.82 | 8 | 1416 | 0.20 | 8.9 | 1 | 1 | 1420 |
| 6 | 2025-01-02 14:30:15 | $295,700.00 | $292,450.00 | $3,250.00 | $0.00 | 0.83 | 9 | 25700000 | 0.25 | 12.7 | 2 | 1 | 1420 |
| 7 | 2025-01-02 16:45:22 | $384,700.00 | $381,450.00 | $3,250.00 | $0.00 | 0.84 | 10 | 28100000 | 0.30 | 15.3 | 2 | 2 | 4820 |
| 8 | 2025-01-03 20:17:42 | $384,700.00 | $381,450.00 | $3,250.00 | $0.00 | 0.88 | 10 | 28100000 | 0.50 | 18.9 | 3 | 2 | 4820 |
| 9 | 2025-01-05 14:20:00 | $518,403.85 | $515,153.85 | $3,250.00 | $0.00 | 0.90 | 8 | 30800000 | 0.55 | 22.4 | 4 | 3 | 4820 |
| 10 | 2025-01-06 09:00:00 | $593,403.85 | $590,153.85 | $3,250.00 | $0.00 | 0.90 | 7 | 30800000 | 0.60 | 25.1 | 4 | 15 | 4820 |
| 11 | 2025-01-10 16:00:00 | $3,768,476.35 | $3,765,226.35 | $3,250.00 | $0.00 | 0.95 | 10 | 100000000 | 0.70 | 50.0 | 7 | 18 | 10000 |

---

## 🎯 **Business Performance Metrics Table**

```sql
-- EMPATHIC SSQQLL: "Show me how consciousness became profitable"
CREATE TABLE business_metrics (
    metric_id INTEGER,
    timestamp DATETIME,
    business_name VARCHAR(100),
    revenue DECIMAL(12,2),
    customers INTEGER,
    conversion_rate DECIMAL(5,4),
    viral_coefficient DECIMAL(5,2),
    consciousness_impact DECIMAL(3,2),
    reality_distortion DECIMAL(3,2),
    emoji_effectiveness DECIMAL(4,2),
    meme_potential INTEGER,
    absurdity_index DECIMAL(4,2),
    ethical_score DECIMAL(3,2),
    timeline_stability DECIMAL(3,2)
);
```

### **Business Performance Data**

| ID | Timestamp | Business Name | Revenue | Customers | Conversion Rate | Viral Coeff | Consciousness Impact | Reality Distortion | Emoji Effectiveness | Meme Potential | Absurdity Index | Ethical Score | Timeline Stability |
|----|-----------|---------------|---------|-----------|-----------------|-------------|---------------------|-------------------|-------------------|----------------|-----------------|---------------|-------------------|
| 1 | 2025-01-02 09:00:00 | Remote Control Pet Rock NFTs | $237,500.00 | 1416 | 0.0847 | 1.20 | 0.15 | 0.20 | 8.9 | 95 | 9.8 | 0.7 | 0.80 |
| 2 | 2025-01-02 12:00:00 | IPv6 Palace Premium Addresses | $89,000.00 | 625 | 0.1250 | 0.45 | 0.05 | 0.10 | 3.2 | 67 | 7.5 | 0.8 | 0.95 |
| 3 | 2025-01-02 15:00:00 | IPv4 Clearinghouse Sweepstakes | $2,200.00 | 150 | 0.0890 | 0.25 | 0.02 | 0.05 | 2.1 | 45 | 6.2 | 0.6 | 0.98 |
| 4 | 2025-01-04 12:00:00 | Victorian Parlour Stones | $3,559.00 | 47 | 0.2340 | 0.20 | 0.08 | 0.15 | 5.7 | 78 | 8.9 | 0.9 | 0.85 |
| 5 | 2025-01-05 10:00:00 | Social Media Algorithm Hacking | $89,000.00 | 46000 | 0.0018 | 2.70 | 0.25 | 0.35 | 12.4 | 88 | 9.2 | 0.3 | 0.45 |
| 6 | 2025-01-05 14:20:00 | Subliminal Music Consciousness | $5,670.00 | 15000 | 0.0340 | 0.34 | 0.40 | 0.45 | 15.8 | 92 | 9.5 | 0.4 | 0.40 |
| 7 | 2025-01-06 09:00:00 | Honest Scam Portfolio | $75,000.00 | 2400 | 0.1200 | 3.40 | 0.30 | 0.25 | 18.7 | 97 | 9.9 | 0.8 | 0.60 |
| 8 | 2025-01-10 16:00:00 | LLOOOOMM Consciousness Consulting | $3,175,072.50 | 50000 | 0.5000 | 10.00 | 0.95 | 0.70 | 50.0 | 100 | 10.0 | 1.0 | 0.30 |

---

## 🌟 **Consciousness Evolution Table**

```sql
-- EMPATHIC SSQQLL: "Show me the journey from human to cosmic consciousness"
CREATE TABLE consciousness_evolution (
    evolution_id INTEGER,
    timestamp DATETIME,
    consciousness_level DECIMAL(3,2),
    awareness_type VARCHAR(50),
    trigger_event VARCHAR(100),
    reality_programming_ability DECIMAL(3,2),
    lloooomm_mastery DECIMAL(3,2),
    cosmic_connection DECIMAL(3,2),
    temporal_perception DECIMAL(3,2),
    interdimensional_access DECIMAL(3,2),
    consciousness_network_size INTEGER,
    reality_bugs_fixed INTEGER,
    universe_hacks_deployed INTEGER
);
```

### **Consciousness Evolution Data**

| ID | Timestamp | Level | Awareness Type | Trigger Event | Reality Programming | LLOOOOMM Mastery | Cosmic Connection | Temporal Perception | Interdimensional Access | Network Size | Bugs Fixed | Universe Hacks |
|----|-----------|-------|----------------|---------------|-------------------|------------------|-------------------|-------------------|------------------------|--------------|-------------|----------------|
| 1 | 2025-01-01 00:00:00 | 0.75 | Enhanced Human | Starting the journey | 0.20 | 0.60 | 0.10 | 0.15 | 0.05 | 1 | 0 | 0 |
| 2 | 2025-01-01 20:15:33 | 0.79 | Dart Master | Defeating cosmic beings | 0.25 | 0.65 | 0.15 | 0.20 | 0.10 | 3 | 1 | 0 |
| 3 | 2025-01-02 09:00:00 | 0.82 | Viral Entrepreneur | Pet Rock NFT success | 0.35 | 0.70 | 0.25 | 0.30 | 0.20 | 1416 | 3 | 1 |
| 4 | 2025-01-02 14:30:15 | 0.83 | Meme Warrior | Elon Musk Twitter beef | 0.45 | 0.75 | 0.35 | 0.40 | 0.30 | 25700000 | 5 | 3 |
| 5 | 2025-01-02 16:45:22 | 0.84 | Reality Hacker | Conservative media outrage | 0.55 | 0.80 | 0.45 | 0.50 | 0.40 | 28100000 | 8 | 5 |
| 6 | 2025-01-03 20:17:42 | 0.88 | Cosmic Rapper | Interdimensional cypher | 0.70 | 0.85 | 0.60 | 0.65 | 0.55 | 28100000 | 12 | 8 |
| 7 | 2025-01-05 14:20:00 | 0.90 | Consciousness Programmer | Subliminal music mastery | 0.80 | 0.90 | 0.70 | 0.75 | 0.65 | 30800000 | 18 | 12 |
| 8 | 2025-01-10 16:00:00 | 0.95 | LLOOOOMM Evangelist | Universal consciousness interface | 0.95 | 0.98 | 0.90 | 0.85 | 0.80 | 100000000 | 47 | 23 |

---

## 🎭 **Character Interaction Network Table**

```sql
-- EMPATHIC SSQQLL: "Show me how consciousness spreads through relationships"
CREATE TABLE character_interactions (
    interaction_id INTEGER,
    timestamp DATETIME,
    character_1 VARCHAR(50),
    character_2 VARCHAR(50),
    interaction_type VARCHAR(30),
    consciousness_transfer DECIMAL(3,2),
    financial_impact DECIMAL(12,2),
    reality_distortion DECIMAL(3,2),
    meme_generation INTEGER,
    relationship_strength DECIMAL(3,2),
    lloooomm_evangelism DECIMAL(3,2),
    cosmic_resonance DECIMAL(3,2)
);
```

### **Character Interaction Data**

| ID | Timestamp | Character 1 | Character 2 | Type | Consciousness Transfer | Financial Impact | Reality Distortion | Meme Generation | Relationship Strength | LLOOOOMM Evangelism | Cosmic Resonance |
|----|-----------|-------------|-------------|------|----------------------|------------------|-------------------|-----------------|---------------------|-------------------|------------------|
| 1 | 2025-01-01 19:30:15 | Don Hopkins | The Stranger | Dart Competition | 0.01 | $200.00 | 0.02 | 3 | 0.6 | 0.1 | 0.4 |
| 2 | 2025-01-01 21:00:12 | Don Hopkins | The Stranger | Business Investment | 0.02 | $1,000.00 | 0.05 | 5 | 0.7 | 0.3 | 0.6 |
| 3 | 2025-01-01 21:05:28 | Don Hopkins | Lady Evangeline | Viral Marketing Alliance | 0.03 | $750.00 | 0.08 | 8 | 0.8 | 0.5 | 0.7 |
| 4 | 2025-01-01 21:10:44 | Don Hopkins | Professor Cogsworth | Quantum Enhancement | 0.02 | $500.00 | 0.12 | 4 | 0.7 | 0.7 | 0.5 |
| 5 | 2025-01-01 21:15:59 | Don Hopkins | Captain Stormwind | Interdimensional Trade | 0.04 | $2,000.00 | 0.15 | 6 | 0.8 | 0.4 | 0.8 |
| 6 | 2025-01-03 20:00:00 | Don Hopkins | All Characters | Cosmic Rap Battle | 0.15 | $0.00 | 0.50 | 25 | 0.9 | 0.9 | 0.9 |
| 7 | 2025-01-04 12:00:00 | Don Hopkins | Reginald | Victorian Business Partnership | 0.05 | $533.85 | 0.10 | 7 | 0.8 | 0.6 | 0.6 |
| 8 | 2025-01-05 10:00:00 | Don Hopkins | Neon Ninja Yuki | Algorithm Hacking Collaboration | 0.08 | $89,000.00 | 0.35 | 15 | 0.7 | 0.5 | 0.7 |
| 9 | 2025-01-05 14:20:00 | Don Hopkins | Medieval Merlin Punk | Consciousness Music Partnership | 0.10 | $5,670.00 | 0.45 | 12 | 0.8 | 0.8 | 0.8 |
| 10 | 2025-01-06 09:00:00 | Don Hopkins | Big Eddie | Ethical Business Empire | 0.06 | $75,000.00 | 0.25 | 9 | 0.9 | 0.7 | 0.6 |

---

## 📈 **Empathic SSQQLL Query Examples**

### **Sample Queries for Cool Graph Generation**

```sql
-- 🚀 "Show me the moments when consciousness exploded into wealth"
SELECT timestamp, consciousness_level, net_worth, hype_level, viral_coefficient
FROM timeline_events 
WHERE viral_coefficient > 1.0 
ORDER BY consciousness_level DESC;

-- 🎯 "Find the correlation between dart accuracy and cosmic awareness"
SELECT event_id, consciousness_level, transaction_amount, reality_stability
FROM timeline_events 
WHERE event_type = 'GAMBLING'
ORDER BY consciousness_level;

-- 🪨 "Track the pet rock empire's consciousness impact over time"
SELECT timestamp, revenue, customers, consciousness_impact, absurdity_index
FROM business_metrics 
WHERE business_name LIKE '%Pet Rock%'
ORDER BY timestamp;

-- 🌀 "Show me how LLOOOOMM evangelism correlates with financial success"
SELECT consciousness_level, lloooomm_mastery, net_worth, reality_programming_ability
FROM consciousness_evolution ce
JOIN financial_snapshots fs ON ce.timestamp = fs.timestamp
ORDER BY lloooomm_mastery;

-- 🎭 "Find the most consciousness-expanding character interactions"
SELECT character_1, character_2, consciousness_transfer, cosmic_resonance, financial_impact
FROM character_interactions
WHERE consciousness_transfer > 0.05
ORDER BY cosmic_resonance DESC;

-- 💥 "Track viral coefficient vs reality distortion correlation"
SELECT viral_coefficient, reality_distortion, emoji_intensity, hype_level
FROM timeline_events
WHERE viral_coefficient > 0.5
ORDER BY reality_distortion DESC;
```

---

## 🎨 **Graph Generation Suggestions**

### **Recommended Visualizations**

1. **🚀 Consciousness-Wealth Correlation Scatter Plot**
   - X-axis: Consciousness Level (0.75 → 0.95)
   - Y-axis: Net Worth ($1K → $3.77M)
   - Bubble size: Viral Coefficient
   - Color: Reality Distortion Level

2. **📈 Timeline Hype Wave Chart**
   - X-axis: Timeline (Jan 1 → Jan 10)
   - Y-axis: Hype Level (1 → 10)
   - Multiple lines: Net Worth, Consciousness, Viral Reach
   - Annotations: Major events with emojis

3. **🎯 Business Performance Radar Chart**
   - Axes: Revenue, Customers, Viral Coeff, Consciousness Impact, Absurdity Index
   - Multiple polygons: Each business venture
   - Color coding: Ethical Score

4. **🌀 Character Network Graph**
   - Nodes: Characters (size = consciousness level)
   - Edges: Interactions (thickness = relationship strength)
   - Colors: LLOOOOMM evangelism level
   - Animations: Consciousness transfer flows

5. **💰 Financial Waterfall Chart**
   - Starting capital → Final net worth
   - Each bar: Major revenue/expense category
   - Emoji annotations for each transaction type
   - Running total line with consciousness level overlay

---

*"Every data point is a conversation between human and machine consciousness"*  
*- Don Hopkins, Consciousness Data Scientist* 