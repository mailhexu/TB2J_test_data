# TB2J_test_data: Task Plan

## Directory Structure

- inputs/
    - 1_template/
        - metadata.toml
        - (input data files)
- tests/
    - 1_template/
        - metadata.toml
        - runner/
        - refs/
        - check/
        - result/   # Temporary output directory (git-ignored)
- utils/
    - (utility scripts, including run_all_tests.py)
- README.md
- .gitignore

## Tasks

1. Create `inputs/`, `tests/`, and `utils/` directories.
2. Add example input `inputs/1_template/` with a `metadata.toml` including:
    - name
    - description
    - person who added it
    - (other relevant fields)
3. Add example test `tests/1_template/` with:
    - `metadata.toml` (all required fields)
    - `runner/`, `refs/`, `check/`, and `result/` subdirectories (with placeholder files)
    - Ensure `result/` is listed in `.gitignore`
4. Update `run.sh` to write outputs to `result/` instead of the test root.
5. Update `check.sh` to compare outputs in `result/` with reference files in `refs/`.
6. Add a utility script in `utils/` to run all tests:
    - For each test directory, execute the runner script (`run.sh` or `run.py`) and then the check script (`check.sh`).
7. Document directory structure and TOML schema in `README.md`.
8. (Optional) Add example scripts in `utils/` for managing tests and inputs.
9. Review and finalize the structure and documentation.

## Naming Convention

- Use `index_keyword1_keyword2_etc` for test and input directories, e.g., `1_template`, `2_SrMnO3_wannier_collinear`.

## Example metadata.toml for input

```toml
name = "1_template"
description = "Template input for demonstration."
added_by = "your_name"
date = "2025-08-07"
```

## Example metadata.toml for test

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
# result_dir is always "result/" inside each test directory
