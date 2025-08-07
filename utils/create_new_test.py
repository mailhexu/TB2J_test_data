#!/usr/bin/env python3
import os

def prompt(msg, default=None):
    if default:
        val = input(f"{msg} [{default}]: ").strip()
        return val if val else default
    return input(f"{msg}: ").strip()

def main():
    print("=== TB2J Test Generator ===")
    index = prompt("Test index (e.g. 3)")
    keywords = prompt("Keywords (underscore separated, e.g. SrMnO3_wannier_collinear)")
    test_name = f"{index}_{keywords}"
    test_dir = os.path.join("..", "tests", test_name)
    if os.path.exists(test_dir):
        print(f"Test directory {test_dir} already exists. Aborting.")
        return

    description = prompt("Description")
    input_dir = prompt("Input directory (relative to tests/, e.g. ../../inputs/2_SrMnO3_wannier_collinear)")
    run_command = prompt("Run command", "bash runner/run.sh")
    reference_files = prompt("Reference files (comma separated, e.g. refs/output1.dat,refs/output2.dat)")
    keywords_list = keywords.split("_")
    tb2j_version = prompt("TB2J version", "v0.7.0")
    added_by = prompt("Your name")
    date = prompt("Date (YYYY-MM-DD)")

    # Create directory structure
    os.makedirs(os.path.join(test_dir, "runner"))
    os.makedirs(os.path.join(test_dir, "refs"))
    os.makedirs(os.path.join(test_dir, "check"))
    os.makedirs(os.path.join(test_dir, "result"))

    # Write metadata.toml
    metadata = f'''name = "{test_name}"
description = "{description}"
input_dir = "{input_dir}"
run_command = "{run_command}"
reference_files = [{', '.join(f'"{f.strip()}"' for f in reference_files.split(','))}]
keywords = [{', '.join(f'"{k}"' for k in keywords_list)}]
tb2j_version = "{tb2j_version}"
added_by = "{added_by}"
date = "{date}"
'''
    with open(os.path.join(test_dir, "metadata.toml"), "w") as f:
        f.write(metadata)

    # Create placeholder scripts
    with open(os.path.join(test_dir, "runner", "run.sh"), "w") as f:
        f.write("#!/bin/bash\n# Add your run logic here\n")
    with open(os.path.join(test_dir, "check", "check.sh"), "w") as f:
        f.write("#!/bin/bash\n# Add your check logic here\n")

    print(f"Test {test_name} created at {test_dir}")

if __name__ == "__main__":
    main()
