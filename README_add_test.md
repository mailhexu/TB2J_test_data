# How to Add a New Dataset and Test

This repository provides a utility script to help you add new datasets and tests in a standardized way. Follow the steps below to add your own test case.

## 1. Prepare Your Input Data
- Place your input files in a new directory under `inputs/`, e.g., `inputs/3_new_material/`.
- Make sure to include all necessary files for running your test (e.g., input files, pseudopotentials, etc.).

## 2. Create a New Test Using the Utility Script
Use the `create_new_test.py` script in the `utils/` directory to generate a new test template. You can customize the test name, input directory, reference files, and other metadata.

### Example Command
```bash
python utils/create_new_test.py ../tests/3_new_material_test \
    -d "Test for new material" \
    -I ../../inputs/3_new_material \
    -r "bash runner/run.sh" \
    -f "refs/output1.dat" \
    -k "new_material" \
    -v "v0.7.0" \
    -a "your_name"
```

- `../tests/3_new_material_test`: Path to the new test directory (relative to the script location).
- `-d`: Description of the test.
- `-I`: Path to the input directory (relative to the `tests/` folder).
- `-r`: Command to run the test.
- `-f`: Reference output files (comma separated if multiple).
- `-k`: Keywords (underscore separated).
- `-v`: TB2J version.
- `-a`: Your name.

## 3. Add Reference Output
- Place your reference output files in the `refs/` directory inside your new test folder.
- Update the `reference_files` field in `metadata.toml` if you have multiple reference files.

## 4. Customize the Run and Check Scripts
- Edit `runner/run.sh` to run your actual calculation and generate output in the `result/` directory.
- Edit `check/check.sh` to compare the output in `result/` with the reference files in `refs/`.

## 5. Update Metadata
- The script generates a `metadata.toml` file. Edit it if you need to update any information (e.g., description, keywords, etc.).

## 6. Run and Check Your Test
- Run your test using the command specified in `run_command` (usually `bash runner/run.sh`).
- Check the output using `bash check/check.sh`.

## 7. (Optional) Add to Automated Test Suite
- If you have an automated test runner (e.g., `utils/run_all_tests.py`), make sure your new test is included.

---

For more details, see the comments in `utils/create_new_test.py` or contact the repository maintainer.
