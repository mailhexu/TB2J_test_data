# TB2J_test_data

Data for TB2J tests.

## Directory Structure

```
TB2J_test_data/
├── inputs/
│   └── 1_template/
│       ├── metadata.toml
│       └── (input data files)
├── tests/
│   └── 1_template/
│       ├── metadata.toml
│       ├── runner/
│       │   └── run.sh
│       ├── refs/
│       │   └── output1.dat
│       └── check/
│           └── check.sh
├── utils/
│   └── (utility scripts)
├── README.md
└── .gitignore
```

## Naming Convention

- Use `index_keyword1_keyword2_etc` for test and input directories, e.g., `1_template`, `2_SrMnO3_wannier_collinear`.

## Metadata for Inputs

Each input directory must contain a `metadata.toml` file with fields such as:

```toml
name = "1_template"
description = "Template input for demonstration."
added_by = "your_name"
date = "2025-08-07"
```

## Metadata for Tests

Each test directory must contain a `metadata.toml` file with fields such as:

```toml
name = "1_template"
description = "Dummy test for template structure."
input_dir = "../../inputs/1_template"
run_command = "bash runner/run.sh"
reference_files = ["refs/output1.dat"]
keywords = ["template", "dummy"]
tb2j_version = "v0.7.0"
added_by = "your_name"
date = "2025-08-07"
```

## Test Directory Structure

For each test (e.g., `1_template`), the directory should contain:
- `metadata.toml`: Metadata for the test.
- `runner/`: Directory with command/script for running the test (e.g., `run.sh`).
- `refs/`: Directory with reference files to be checked.
- `check/`: Directory with command/script for checking the result.

## Inputs Directory Structure

Each input dataset should be in its own directory under `inputs/`, with a `metadata.toml` describing the dataset.

## Utils

The `utils/` directory contains Python scripts for adding, running, updating, and post-processing the tests.
