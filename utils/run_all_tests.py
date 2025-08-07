#!/usr/bin/env python3
import os
import subprocess

def run_test(test_dir):
    runner_sh = os.path.join(test_dir, "runner", "run.sh")
    runner_py = os.path.join(test_dir, "runner", "run.py")
    check_sh = os.path.join(test_dir, "check", "check.sh")
    result = {"test": test_dir, "run": None, "check": None}

    # Run the runner script
    if os.path.isfile(runner_sh):
        print(f"Running {runner_sh} ...")
        run_proc = subprocess.run(["bash", runner_sh], cwd=os.path.dirname(runner_sh))
        result["run"] = run_proc.returncode
    elif os.path.isfile(runner_py):
        print(f"Running {runner_py} ...")
        run_proc = subprocess.run(["python3", runner_py], cwd=os.path.dirname(runner_py))
        result["run"] = run_proc.returncode
    else:
        print(f"No runner script found in {test_dir}")
        result["run"] = -1

    # Run the check script
    if os.path.isfile(check_sh):
        print(f"Checking {check_sh} ...")
        check_proc = subprocess.run(["bash", check_sh], cwd=os.path.dirname(check_sh))
        result["check"] = check_proc.returncode
    else:
        print(f"No check.sh found in {test_dir}")
        result["check"] = -1

    return result

def main():
    tests_root = os.path.join(os.path.dirname(__file__), "..", "tests")
    test_dirs = [os.path.join(tests_root, d) for d in os.listdir(tests_root)
                 if os.path.isdir(os.path.join(tests_root, d))]
    results = []
    for test_dir in sorted(test_dirs):
        print(f"\n=== Running test: {os.path.basename(test_dir)} ===")
        res = run_test(test_dir)
        results.append(res)
    print("\n=== Summary ===")
    for res in results:
        print(f"{os.path.basename(res['test'])}: run={res['run']} check={res['check']}")

if __name__ == "__main__":
    main()
