# Don Hopkins: Programming Practices and Comments
## Documented Patterns from Code and Reviews

### Common Practices Found in Code

#### Progressive Disclosure in UI
From Sims design documents: "Make the invisible visible - but only when players want to see it."

Implementation:
- Base UI shows essential information
- Click to expand detailed panels
- Advanced options available through right-click
- Tooltips provide additional context

#### Opposition to Modal Dialogs
From design review: "MODAL DIALOGS CAUSE MANY MORE PROBLEMS THAN THEY SOLVE"

Alternative approaches used:
- Undo instead of confirmation dialogs
- Visual feedback during operations
- Non-blocking property panels
- Inline error messages

#### Code Documentation Style
Example from VitaBoy code:
```cpp
/****
@member: VBAnimMgr::LoadAnimation
@description
This takes a dir name, a file name, and a resource site,
and it loads all the Skeletons, Suits, and Skills 
into the animation manager.
****/
```

Consistent pattern of explaining what code does and why it matters.

#### Parameter Naming
Found in cellular automata code:
```python
cam.frob = 7  # Chaos injection parameter
cam.wrap = 3  # Toroidal topology
cam.neighborhood = 46  # CA rule number
```

Uses descriptive or playful names for experimental parameters.

#### Lazy Loading Pattern
Template from C++ code:
```cpp
template <class T>
class Envelope {
    T *mData;
    bool mLoaded;
    T *Expose() {
        if (!mLoaded) Load();
        return mData;
    }
};
```

Defers expensive operations until actually needed.

### Design Review Comments

#### On Naming Consistency
"This appears in 17+ code modules. If we don't fix it now, we'll have inconsistent variable names forever."

#### On User Interface
"The microworld needs a microscope - tools to see inside the simulation's thinking"

#### On Inclusion
"The whole relationship design and implementation (I've looked at the tree code) is Heterosexist and Monosexist."

#### On Development Process
"(NOTE: Live mode chapter below is based on the work done for 9/30 delivery milestone... changes will be taken up in the next design milestone.)"

### Technical Patterns

#### Memory Management
OwnedObject pattern for hierarchical cleanup:
```python
class OwnedObject:
    def destroy(self):
        for owned in self.owned:
            owned.destroy()
        for finalizer in self.finalizers:
            finalizer(self)
```

#### Context-Sensitive Menus
Pie menus that filter options based on:
- Actor state
- Target capabilities  
- Current relationship
- Environmental context

#### Visual Debugging
Tools that display internal state:
- Mood visualizers
- Relationship graphs
- Animation state displays
- Property inspectors

### Implementation Examples

#### From PizzaTool (NeWS)
Complete PostScript application for ordering pizza, demonstrating:
- Network communication
- UI in PostScript
- Practical application of window system

#### From Micropolis
Open source SimCity port showing:
- Cross-platform considerations
- Educational focus
- Community development practices

### Common Themes

These patterns appear consistently:
- Making internal state visible for debugging
- Avoiding modal interactions
- Enabling user experimentation
- Clear documentation of intent
- Playful approach to serious problems

### Available Resources

Code and documentation by Don Hopkins:
- https://www.donhopkins.com/home/archive/
- https://github.com/SimHacker/micropolis
- Various pie menu implementations
- Design document annotations 