# Data Model

## Objects

### Pipeline

This is the definition of a pipeline.

- __name__
  - Type: string
  - Description: Name of the pipeline
- steps
  - Type: Step
  - Description: List of steps in the pipeline
  - Multiple: True
- max_length
  - Type: int
  - Description: Maximum length of the pipeline

### Step

This is the definition of a step.

- __name__
  - Type: string
  - Description: Name of the pipeline
- __required__
  - Type: bool
  - Description: True, if step is required for the pipeline
- new_attr
  - Type: float
  - Description: New test attr
  - Multiple: True
- species
    - Type: https://github.com/EnzymeML/enzymeml-specifications.git@AbstractSpecies,
    - Description: Species of the step
    - Multiple: True
