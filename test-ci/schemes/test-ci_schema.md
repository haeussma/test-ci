```mermaid
classDiagram
    Pipeline *-- Step
    
    class Pipeline {
        +string name
        +Step steps
    }
    
    class Step {
        +string name
        +bool required
    }
    
```