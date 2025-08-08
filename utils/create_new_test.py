#!/usr/bin/env python3
import os
from datetime import date
import argparse

def main():
    parser = argparse.ArgumentParser(description="Generate a template TB2J test directory.")
    parser.add_argument("path", nargs="?", default=None, help="Test directory path (e.g. ../tests/3_SrMnO3_wannier_collinear)")
    parser.add_argument("-i", "--index", default="1", help="Test index (default: 1)")
    parser.add_argument("-k", "--keywords", default="template", help="Keywords (underscore separated, default: template)")
    parser.add_argument("-d", "--description", default="Dummy test for template structure.", help="Test description")
    parser.add_argument("-I", "--input_dir", default="../../inputs/1_template", help="Input directory (relative to tests/)")
    parser.add_argument("-r", "--run_command", default="bash runner/run.sh", help="Run command")
    parser.add_argument("-f", "--reference_files", default="refs/output1.dat", help="Reference files (comma separated)")
    parser.add_argument("-v", "--tb2j_version", default="v0.7.0", help="TB2J version")
    parser.add_argument("-a", "--added_by", default="your_name", help="Person who added the test")
    parser.add_argument("-D", "--date", default=date.today().isoformat(), help="Date (YYYY-MM-DD)")

    args = parser.parse_args()

    if args.path:
        test_dir = args.path
        test_name = os.path.basename(os.path.normpath(test_dir))
    else:
        test_name = f"{args.index}_{args.keywords}"
        test_dir = os.path.join("..", "tests", test_name)

    if os.path.exists(test_dir):
        print(f"Test directory {test_dir} already exists. Aborting.")
        return

    keywords_list = args.keywords.split("_")
    reference_files_list = [f.strip() for f in args.reference_files.split(",")]

    # Create directory structure
    os.makedirs(os.path.join(test_dir, "runner"))
    os.makedirs(os.path.join(test_dir, "refs"))
    os.makedirs(os.path.join(test_dir, "check"))
    os.makedirs(os.path.join(test_dir, "result"))

    # Write metadata.toml
    metadata = f'''name = "{test_name}"
description = "{args.description}"
input_dir = "{args.input_dir}"
run_command = "{args.run_command}"
reference_files = [{', '.join(f'"{f}"' for f in reference_files_list)}]
keywords = [{', '.join(f'"{k}"' for k in keywords_list)}]
tb2j_version = "{args.tb2j_version}"
added_by = "{args.added_by}"
date = "{args.date}"
'''
    with open(os.path.join(test_dir, "metadata.toml"), "w") as f:
        f.write(metadata)

    # Create dummy run.sh
    run_sh = os.path.join(test_dir, "runner", "run.sh")
    with open(run_sh, "w") as f:
        f.write("#!/bin/bash\n# Dummy run script for template test\necho \"Running dummy test\"\necho \"# Dummy reference output for template test\" > ../result/output1.dat\necho \"value = 42\" >> ../result/output1.dat\n")
    os.chmod(run_sh, 0o755)

    # Create dummy check.sh
    check_sh = os.path.join(test_dir, "check", "check.sh")
    with open(check_sh, "w") as f:
        f.write("#!/bin/bash\n# Dummy check script for template test\necho \"Checking dummy test output\"\nif diff ../result/output1.dat ../refs/output1.dat; then\n    echo \"Test passed: outputs are consistent.\"\n    exit 0\nelse\n    echo \"Test failed: outputs differ.\"\n    exit 1\nfi\n")
    os.chmod(check_sh, 0o755)

    print(f"Template test {test_name} created at {test_dir}")

if __name__ == "__main__":
    main()
