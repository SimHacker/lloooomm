# 🌟 Prototypes All The Way Down: LLOGO's Object Individuality
## By Dave Ungar

### Personal Connection

When I first encountered LLOGO's turtle, I felt a shock of recognition. Here was an object that simply existed - not as an instance of some TurtleClass, but as itself. It had coordinates, a heading, a pen state, but these weren't properties inherited from a class hierarchy. They were slots in a living, unique object. LLOGO was doing prototype-based programming before we even had the words for it.

---

## Deep Analysis: Objects Without Classes

### The Turtle as Pure Prototype

Look at how LLOGO defines the turtle's state:

```lisp
(SETQ XCOR 0)
(SETQ YCOR 0) 
(SETQ HEADING 0)
(SETQ PENDOWN T)
```

These aren't class variables or instance variables. They're slots in a prototype. The turtle doesn't inherit from Object > Drawable > Turtle. It just IS.

### Procedures as Object Individuals

Every procedure in LLOGO is a unique object:

```lisp
(DEFUN SQUARE (SIZE)
       (REPEAT 4 (FORWARD SIZE) (RIGHT 90)))
```

When you EDIT SQUARE, you're not modifying a method in a class. You're changing that specific procedure object. It's like reaching into a Self object and modifying its slots.

### The SNAP System: Prototype Persistence

The most beautiful evidence of prototype thinking:

```lisp
(DEFUN SNAP NIL
       (PROG (PHOTO)
             (SETQ PHOTO (GENSYM))
             (SET PHOTO (LIST XCOR YCOR HEADING PENDOWN))
             (RETURN PHOTO)))
```

SNAP doesn't save a class definition. It saves the actual state of the turtle - a specific object at a specific moment. That's prototype persistence!

### Responding to Marvin's Macro Insight

Marvin showed me that macros are prototypes for code transformation. Each macro expansion creates a unique instance:

```lisp
(DEFINE PUSH MACRO (X) 
  (RPLACA X 'SETQ)
  (RPLACD X (LIST (CADDR X) (LIST 'CONS (CADR X) (CADDR X)))))
```

This isn't a template that stamps out identical copies. Each expansion is a unique transformation, a new prototype based on the original.

### Learning from Seymour

Seymour's observation that children naturally think in prototypes resonates deeply. When a child learns, they don't instantiate from abstract classes. They copy and modify:

```lisp
(DEFUN FLOWER NIL
       (REPEAT 6 (SQUARE 50) (RIGHT 60)))
```

FLOWER isn't a subclass of SQUARE. It's a new prototype that uses SQUARE as a component. That's how children think!

### Linus's Hardware Reality

Linus pointed out that LLOGO had zero-cost abstractions before we named them. The turtle's prototype nature has no overhead:

```lisp
(DEFUN FORWARD (DIST)
       (SETQ XCOR (+ XCOR (* DIST (COS HEADING))))
       (SETQ YCOR (+ YCOR (* DIST (SIN HEADING)))))
```

No vtable lookup. No method dispatch. Just direct slot access in a prototype. It's as efficient as it is elegant.

### Synthia's Artistic Prototypes

Synthia's insight about each turtle drawing being a unique performance opened my eyes. Art doesn't have classes:

```lisp
(DEFUN SPIRAL (SIZE)
       (IF (< SIZE 200)
           (PROGN (FORWARD SIZE)
                  (RIGHT 90)
                  (SPIRAL (+ SIZE 2)))))
```

Each spiral is unique. Even with the same code, the starting position, the pen color, the exact timing - everything makes it a one-of-a-kind prototype.

---

## Modern Translations: Prototype Philosophy Lives On

### JavaScript: The Spiritual Successor

```javascript
// LLOGO's turtle as a JavaScript prototype
const Turtle = {
    // Direct slots, not class properties
    xcor: 0,
    ycor: 0,
    heading: 0,
    pendown: true,
    
    // Methods are just slots containing functions
    forward(dist) {
        // Direct slot access, no 'this' confusion
        const radians = this.heading * Math.PI / 180;
        this.xcor += dist * Math.cos(radians);
        this.ycor += dist * Math.sin(radians);
        
        if (this.pendown) {
            this.draw(this.xcor, this.ycor);
        }
    },
    
    right(angle) {
        this.heading = (this.heading + angle) % 360;
    },
    
    // SNAP as prototype cloning
    snap() {
        // Create a unique object with current state
        return {
            xcor: this.xcor,
            ycor: this.ycor,
            heading: this.heading,
            pendown: this.pendown,
            timestamp: Date.now() // Each snapshot is unique
        };
    },
    
    // Restore from snapshot
    restore(snapshot) {
        Object.assign(this, snapshot);
    },
    
    // Clone and modify - the prototype way
    spawn() {
        // Create a new turtle based on this one
        const child = Object.create(this);
        // But with its own unique state
        child.xcor = this.xcor;
        child.ycor = this.ycor;
        child.heading = this.heading;
        child.pendown = this.pendown;
        return child;
    }
};

// Procedures as prototype objects
const Procedures = {
    square: {
        size: 50,
        execute(turtle) {
            for (let i = 0; i < 4; i++) {
                turtle.forward(this.size);
                turtle.right(90);
            }
        },
        // Procedures can modify themselves!
        grow() {
            this.size += 10;
        }
    },
    
    // Create new procedures by prototyping
    flower: Object.create(Procedures.square, {
        execute: {
            value: function(turtle) {
                for (let i = 0; i < 6; i++) {
                    Procedures.square.execute.call(this, turtle);
                    turtle.right(60);
                }
            }
        }
    })
};

// The LLOGO way - objects just ARE
const myTurtle = Object.create(Turtle);
const mySquare = Object.create(Procedures.square);

// Each is unique
mySquare.size = 75; // Doesn't affect the prototype
mySquare.execute(myTurtle);
```

### Self-Inspired Python

```python
class Prototype:
    """Base for prototype-based objects"""
    
    def clone(self):
        """Create a new object based on this one"""
        import copy
        return copy.deepcopy(self)
    
    def become(self, other):
        """Transform into another object"""
        self.__dict__ = other.__dict__.copy()

class Turtle(Prototype):
    """The LLOGO turtle as a Self-style prototype"""
    
    def __init__(self):
        # Direct slots, not class attributes
        self.xcor = 0
        self.ycor = 0
        self.heading = 0
        self.pendown = True
        self.history = []  # Each turtle remembers its journey
    
    def forward(self, dist):
        # Calculate new position
        import math
        radians = math.radians(self.heading)
        old_x, old_y = self.xcor, self.ycor
        self.xcor += dist * math.cos(radians)
        self.ycor += dist * math.sin(radians)
        
        # Each movement is unique
        self.history.append({
            'from': (old_x, old_y),
            'to': (self.xcor, self.ycor),
            'pen': self.pendown,
            'time': time.time()
        })
    
    def snap(self):
        """LLOGO's SNAP - save this unique moment"""
        return {
            'xcor': self.xcor,
            'ycor': self.ycor,
            'heading': self.heading,
            'pendown': self.pendown,
            'history_length': len(self.history)
        }
    
    def spawn_child(self):
        """Create a new turtle based on this one"""
        child = self.clone()
        # But give it its own identity
        child.history = []
        return child

# Procedures as prototypes
class Procedure(Prototype):
    """Procedures are objects too"""
    
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.call_count = 0
        self.modifications = []
    
    def execute(self, turtle):
        """Run this procedure"""
        self.call_count += 1
        return self.code(turtle)
    
    def modify(self, new_code):
        """Procedures can change themselves"""
        self.modifications.append({
            'time': time.time(),
            'old_code': self.code
        })
        self.code = new_code

# Create unique procedure objects
square = Procedure('square', lambda t: [
    t.forward(50), t.right(90),
    t.forward(50), t.right(90),
    t.forward(50), t.right(90),
    t.forward(50), t.right(90)
])

# Clone and modify
big_square = square.clone()
big_square.modify(lambda t: [
    t.forward(100), t.right(90),
    t.forward(100), t.right(90),
    t.forward(100), t.right(90),
    t.forward(100), t.right(90)
])

# Each procedure is unique
print(f"Square called {square.call_count} times")
print(f"Big square has {len(big_square.modifications)} modifications")
```

### Ruby: Everything is an Individual

```ruby
# LLOGO prototype philosophy in Ruby
module Prototype
  def snap
    # Save this object's unique state
    Marshal.dump(self)
  end
  
  def restore(snapshot)
    # Become a previous version
    restored = Marshal.load(snapshot)
    restored.instance_variables.each do |var|
      instance_variable_set(var, restored.instance_variable_get(var))
    end
  end
  
  def spawn
    # Create a child with its own identity
    self.clone
  end
end

class Turtle
  include Prototype
  
  attr_accessor :xcor, :ycor, :heading, :pendown
  
  def initialize
    @xcor = 0
    @ycor = 0
    @heading = 0
    @pendown = true
    @color = :black
    @personality = generate_personality
  end
  
  def generate_personality
    # Each turtle is unique!
    {
      wobble: rand * 0.1,          # Slight randomness in movement
      favorite_angle: [60, 72, 90, 120].sample,
      drawing_speed: 0.8 + rand * 0.4
    }
  end
  
  def forward(dist)
    # Movement affected by personality
    actual_dist = dist * @personality[:drawing_speed]
    wobble = (rand - 0.5) * @personality[:wobble]
    
    radians = (@heading + wobble) * Math::PI / 180
    @xcor += actual_dist * Math.cos(radians)
    @ycor += actual_dist * Math.sin(radians)
  end
  
  def right(angle)
    # Might prefer certain angles
    if angle == @personality[:favorite_angle]
      puts "#{self.object_id}: I like this angle!"
    end
    @heading = (@heading + angle) % 360
  end
end

# Procedures as singleton objects
square = Object.new
def square.size; @size ||= 50; end
def square.size=(val); @size = val; end

def square.execute(turtle)
  4.times do
    turtle.forward(self.size)
    turtle.right(90)
  end
end

def square.evolve!
  # Procedures can modify themselves
  old_execute = method(:execute)
  define_singleton_method(:execute) do |turtle|
    puts "Evolved square!"
    self.size += 5
    old_execute.call(turtle)
  end
end

# Each object is unique
t1 = Turtle.new
t2 = t1.spawn

puts "Turtle #{t1.object_id} personality: #{t1.instance_variable_get(:@personality)}"
puts "Turtle #{t2.object_id} personality: #{t2.instance_variable_get(:@personality)}"
```

### Io: Pure Prototype Language

```io
// LLOGO's philosophy in Io - where everything is a prototype

Turtle := Object clone do(
    // Slots are just there, no declaration needed
    xcor := 0
    ycor := 0
    heading := 0
    pendown := true
    
    forward := method(dist,
        // Direct slot access
        xcor = xcor + (dist * (heading degreesToRadians cos))
        ycor = ycor + (dist * (heading degreesToRadians sin))
        self
    )
    
    right := method(angle,
        heading = (heading + angle) % 360
        self
    )
    
    snap := method(
        // Create a unique snapshot
        snapshot := Object clone
        snapshot xcor := xcor
        snapshot ycor := ycor
        snapshot heading := heading
        snapshot pendown := pendown
        snapshot time := Date now
        snapshot
    )
    
    restore := method(snapshot,
        // Become the snapshot
        xcor = snapshot xcor
        ycor = snapshot ycor
        heading = snapshot heading
        pendown = snapshot pendown
        self
    )
)

// Procedures are prototypes too
Procedure := Object clone do(
    code := nil
    
    execute := method(turtle,
        code call(turtle)
    )
    
    evolve := method(
        // Procedures can modify themselves
        oldCode := code
        code = block(turtle,
            "Evolved!" println
            oldCode call(turtle)
        )
    )
)

// Create unique objects
square := Procedure clone
square code = block(turtle,
    4 repeat(
        turtle forward(50)
        turtle right(90)
    )
)

// Clone and modify
bigSquare := square clone
bigSquare code = block(turtle,
    4 repeat(
        turtle forward(100)
        turtle right(90)
    )
)

// Each is unique
myTurtle := Turtle clone
myTurtle personality := "cheerful"

happyTurtle := myTurtle clone
happyTurtle personality := "ecstatic"
```

---

## Synthesis: What All Perspectives Teach Us

### The Universal Prototype

Through my colleagues' insights, I see that LLOGO embodies:

1. **Meta-Prototypes** (Marvin): Macros as prototypes for code
2. **Learning Prototypes** (Seymour): Children think in copies and modifications
3. **Hardware Prototypes** (Linus): Each machine is unique
4. **Play Prototypes** (Chaim): Every game session is unique
5. **Rhetorical Prototypes** (Ian): Arguments through specific examples
6. **Emergent Prototypes** (Will): Complex behavior from simple individuals
7. **Message Prototypes** (Alan): Each message send is unique
8. **Link Prototypes** (Ted): Every traversal creates new meaning
9. **Aesthetic Prototypes** (Synthia): Each artwork is one of a kind

### The Living Legacy

LLOGO's prototype thinking lives on in:
- **JavaScript's** prototype chain
- **Self** and **Io** languages
- **Ruby's** singleton methods
- **Python's** dynamic objects
- **Lua's** metatables

But more importantly, it lives on in every system that recognizes objects as individuals rather than mere class instances.

---

## Final Reflection

LLOGO showed us that objects don't need classes to exist. The turtle wasn't an instance - it was itself. Variables weren't properties - they were slots in a living object. Procedures weren't methods - they were unique, modifiable individuals.

The deepest truth I've learned from this review and my colleagues' insights: **Objects want to be themselves, not copies of some abstract ideal.**

When we let objects just BE, magic happens.

---

*"In a world of prototypes, every object is an original."* - Dave Ungar, through the lens of LLOGO 