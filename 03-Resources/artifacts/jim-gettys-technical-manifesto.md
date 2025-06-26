# The Gettys Technical Manifesto
## On Graphics, Networks, and the Flow of Information

*A Collection of Technical Principles by Jim Gettys*

---

## Preamble

After decades of working on graphics systems and network protocols, I've distilled my experience into core principles that transcend specific technologies. Whether we're talking about X11 rendering pipelines or TCP buffer management, the fundamental challenges are remarkably similar: **How do we move information efficiently while preserving human experience?**

## Part I: The Graphics Revelation

### Principle 1: Separate Description from Implementation

When we designed Cairo, the breakthrough wasn't in faster rendering - it was in **mathematical abstraction**. Instead of thinking about pixels, we thought about paths:

```cairo
// This describes WHAT, not HOW
cairo_move_to(cr, start_x, start_y);
cairo_curve_to(cr, cp1_x, cp1_y, cp2_x, cp2_y, end_x, end_y);
cairo_set_source_rgba(cr, red, green, blue, alpha);
cairo_fill_preserve(cr);
cairo_stroke(cr);
```

The genius is that this same description can become:
- Pixels on a screen (rasterization)
- Lines in a PDF (vector output)
- PostScript commands (printing)
- SVG elements (web graphics)

**Lesson**: *Abstract away the "how" so you can optimize it independently of the "what".*

### Principle 2: Device Independence Enables Innovation

X11 succeeded because it separated:
- **Policy** (what the interface looks like) from **Mechanism** (how windows are managed)
- **Client** (application logic) from **Server** (display hardware)
- **Protocol** (command format) from **Implementation** (rendering details)

This allowed:
- Applications to run on any display
- Window managers to innovate independently
- Hardware vendors to optimize without breaking compatibility

**Lesson**: *The most flexible systems define interfaces, not implementations.*

### Principle 3: Human Perception Sets the Requirements

Graphics systems must respect human timing:
- **16ms frame budget** for smooth animation (60 FPS)
- **100ms response threshold** for interactive feedback
- **10ms precision** for fine motor control (like Don Hopkins' pie menus)

We optimized for the wrong metrics when we focused on:
- Peak polygon throughput instead of consistent frame timing
- Color depth instead of temporal smoothness
- Raw bandwidth instead of predictable latency

**Lesson**: *Optimize for human perception, not machine metrics.*

## Part II: The Network Awakening

### Principle 4: Bufferbloat - The Hidden Performance Killer

The most insidious performance problems are invisible in traditional metrics:

```
Traditional View:
Throughput = Good
Bandwidth = Good
Buffer Size = Bigger is Better

Reality:
Latency = User Experience
Predictability = Reliability  
Buffer Bloat = Latency Spikes
```

**The Bufferbloat Problem**:
1. Router manufacturer thinks: "Bigger buffers = fewer dropped packets = better performance"
2. Reality: Huge buffers create massive queuing delays under load
3. Result: Network "works" but feels terrible for interactive applications

**The Solution**:
- Smart queue management (CoDel, fq_codel)
- Smaller, adaptive buffers
- Active queue management that prevents bloat

**Lesson**: *Bigger buffers are like wider roads - they seem good until they fill up with traffic.*

### Principle 5: Protocols Should Be Conversations, Not Broadcasts

Bad protocol design:
```
Client: "Here's my request with everything I might possibly need"
Server: "Here's everything you might possibly want back"
Result: Huge round-trip times, wasted bandwidth
```

Good protocol design:
```
Client: "I need X"
Server: "Here's X, and I can also provide Y if needed"
Client: "Thanks, I'll take Y too"
Result: Minimal initial latency, extensible without bloat
```

**X11 Example**: The core protocol is minimal, but extensible. New features are added as extensions that negotiate capabilities, rather than bloating the base protocol.

**Lesson**: *Start small and allow growth, don't start big and try to optimize.*

## Part III: The Convergence

### Principle 6: Information Flow Patterns Are Universal

Whether it's:
- Graphics commands flowing from application to display
- Network packets flowing from client to server  
- User inputs flowing from gesture to response

The same patterns apply:
- **Batch when possible** (reduce per-operation overhead)
- **Pipeline aggressively** (overlap operations)
- **Buffer intelligently** (smooth out bursts without adding latency)
- **Fail fast** (don't let problems accumulate)

### Principle 7: Embrace Asymmetry

Real systems aren't symmetric:

**Graphics**: 
- Lots of rendering commands → Few pixels changed
- Complex geometry → Simple rasterization

**Networks**:
- Many small requests → Few large responses
- Downstream bandwidth >> Upstream bandwidth
- Interactive traffic << Bulk transfer traffic

**Design for the common case, handle the edge cases gracefully.**

### Principle 8: The User Is The Ultimate Judge

Technical metrics lie:
- High throughput with terrible latency = bad user experience
- Perfect protocol compliance with poor performance = failure
- Elegant code that doesn't solve real problems = academic exercise

**Always ask**: *Does this make the human experience better?*

## Part IV: Practical Applications

### For Graphics Systems

1. **Profile for frame consistency, not peak performance**
2. **Design rendering pipelines like assembly lines** - optimize the whole, not the parts
3. **Cache aggressively, invalidate intelligently**
4. **Make the common case fast, make the edge cases correct**

### For Network Systems  

1. **Measure latency under load, not just throughput**
2. **Design queue management to prevent bloat before it happens**
3. **Optimize for interactive traffic first, bulk transfer second**
4. **Monitor buffering at every layer of the stack**

### For Protocol Design

1. **Version everything from day one**
2. **Design for extensibility without breaking compatibility** 
3. **Keep the core minimal, add features as extensions**
4. **Fail gracefully when extensions aren't supported**

## Part V: The Meta-Principles

### Principle 9: Complexity Is the Enemy

Every additional feature:
- Increases testing burden exponentially
- Creates new failure modes
- Makes optimization harder
- Confuses users and developers

**Fight complexity at every level**:
- Simple protocols are easier to implement correctly
- Simple interfaces are easier to use correctly
- Simple code is easier to debug and optimize

### Principle 10: Open Standards Enable Innovation

Proprietary systems optimize for vendor lock-in.
Open standards optimize for ecosystem growth.

**X11 survived** because:
- No single vendor controlled it
- Anyone could implement it
- Extensions could be developed independently
- Competition happened at the application layer

**The web succeeded** for the same reasons.

**Lesson**: *Give up control to gain influence.*

## Conclusion: The Flow Continues

Information wants to flow efficiently. Our job as engineers is to:

1. **Remove unnecessary impediments** (eliminate bufferbloat)
2. **Provide elegant abstractions** (separate policy from mechanism)  
3. **Optimize for human perception** (latency matters more than throughput)
4. **Design for growth** (extensible architectures)
5. **Stay humble** (the user is always right about their experience)

Whether you're designing the next graphics API or debugging network performance, remember: **every bit of latency matters, every unnecessary buffer is a tax on human attention, and every protocol decision shapes how people communicate and create.**

The goal isn't perfect code - it's perfect information flow.

---

*"The best protocols are invisible, the best graphics are immediate, and the best networks feel like they're not there at all."*

**- Jim Gettys**  
*Graphics Pioneer & Latency Liberator*

---

## Technical Appendix: Code Examples from the Field

### X11 Color Allocation (from the LLOOOOMM repository)
```c
// From TheSims/FaceLift02-17-2000/frustum-1.0/togl.c
static Colormap get_rgb_colormap(Display *dpy, int scrnum, 
                                const XVisualInfo *visinfo)
{
    // First check if visinfo's visual matches the default/root visual
    if (visinfo->visual == DefaultVisual(dpy, scrnum)) {
        return DefaultColormap(dpy, scrnum);
    }
    
    // Try to find a standard X colormap
    status = XmuLookupStandardColormap(dpy, visinfo->screen,
                                      visinfo->visualid, visinfo->depth,
                                      XA_RGB_DEFAULT_MAP,
                                      False, True);
    
    // If all else fails, create a new colormap
    return XCreateColormap(dpy, root, visinfo->visual, AllocNone);
}
```

**Note**: This code demonstrates the X11 principle of graceful degradation - try the optimal path first, fall back to workable alternatives.

### Cairo-style Graphics Abstraction (inspired by Cairo philosophy)
```c
// This is how Cairo thinks about graphics
typedef struct {
    double x, y;
} point_t;

typedef struct {
    point_t current_point;
    path_t *path;
    surface_t *target;
    pattern_t *source;
} context_t;

// Device-independent operations
void cairo_move_to(context_t *cr, double x, double y);
void cairo_line_to(context_t *cr, double x, double y);
void cairo_stroke(context_t *cr);

// Device-specific implementations happen here
void surface_stroke(surface_t *surface, path_t *path, pattern_t *source);
```

### Network Buffer Management (Anti-Bufferbloat)
```c
// Traditional (bad) approach
#define HUGE_BUFFER_SIZE (1024 * 1024)  // 1MB buffer - seems good!
char network_buffer[HUGE_BUFFER_SIZE];

// Better approach - adaptive buffering
typedef struct {
    char *buffer;
    size_t current_size;
    size_t max_size;
    double average_latency;
    uint64_t last_measurement;
} adaptive_buffer_t;

void adaptive_buffer_resize(adaptive_buffer_t *buf) {
    if (buf->average_latency > TARGET_LATENCY) {
        // Latency too high - shrink buffer
        buf->max_size = buf->max_size * 0.9;
    } else if (buf->current_size == buf->max_size) {
        // Buffer full but latency OK - can grow
        buf->max_size = buf->max_size * 1.1;
    }
}
```

This manifesto captures the essence of principled engineering - technical decisions guided by human needs and open collaboration. 