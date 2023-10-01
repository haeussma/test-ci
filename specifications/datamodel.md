# Data Model

## Objects

### Pipeline
- name
  - Type: string
  - Description: Name of the pipeline
- steps
  - Type: Step
  - Description: Steps of the pipeline

### Step
- name
  - Type: string
  - Description: Name of the pipeline
- required
  - Type: bool
  - Description: True, if step is required for the pipeline
