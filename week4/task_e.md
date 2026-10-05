# Week 4 - Part E: Dependency Mapping

Draw the dependency structure, starting from:

```
                 main.py
                /   |   \
               v    v    v
      validation calculations display
```

Answer these:

1. Which modules does `main.py` depend on?
2. Does `display.py` need to know how the grade is calculated?
3. Does `calculations.py` need to know how results are printed?
4. What would have to change if `display.py` were replaced by a GUI?
5. Which of the dependencies are necessary, and which would be unnecessary coupling?
