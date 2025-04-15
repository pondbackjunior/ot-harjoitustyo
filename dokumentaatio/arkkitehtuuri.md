```mermaid
 classDiagram
    ui "1" -- "1" FileHandler
    ui "1" -- "1" EditorMain
    ui "1" -- "1" VisualEditor
    ui "1" -- "1" SourceEditor
    FileHandler "1" -- "1" FileDatabase

    class ui{
        root
        textarea
    }
```

Alustava luokkakaavio.