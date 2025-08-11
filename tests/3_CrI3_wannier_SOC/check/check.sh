#!/bin/bash
# Dummy check script for template test
echo "Checking dummy test output"
if diff ../result/output1.dat ../refs/output1.dat; then
    echo "Test passed: outputs are consistent."
    exit 0
else
    echo "Test failed: outputs differ."
    exit 1
fi
