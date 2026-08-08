"""
Auto-grading tests for Lab 2.6.1.9: Simple Input and Output
Run: python -m pytest test_lab.py -v
"""

import sys
import subprocess
from io import StringIO
import importlib.util

def load_lab_module():
    """Dynamically import the lab.py module"""
    spec = importlib.util.spec_from_file_location("lab", "lab.py")
    if spec is None or spec.loader is None:
        raise ImportError("Could not find lab.py")
    lab = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lab)
    return lab

def test_variables_exist():
    """Test that all required variables are defined"""
    lab = load_lab_module()
    assert hasattr(lab, 'a'), "Variable 'a' not defined"
    assert hasattr(lab, 'b'), "Variable 'b' not defined"
    assert hasattr(lab, 'result_add'), "Variable 'result_add' not defined"
    assert hasattr(lab, 'result_sub'), "Variable 'result_sub' not defined"
    assert hasattr(lab, 'result_mul'), "Variable 'result_mul' not defined"
    assert hasattr(lab, 'result_div'), "Variable 'result_div' not defined"

def test_variables_are_numeric():
    """Test that variables are numeric types"""
    lab = load_lab_module()
    assert isinstance(lab.a, (int, float)), f"Variable 'a' should be numeric, got {type(lab.a)}"
    assert isinstance(lab.b, (int, float)), f"Variable 'b' should be numeric, got {type(lab.b)}"
    assert isinstance(lab.result_add, (int, float)), "result_add should be numeric"
    assert isinstance(lab.result_sub, (int, float)), "result_sub should be numeric"
    assert isinstance(lab.result_mul, (int, float)), "result_mul should be numeric"
    assert isinstance(lab.result_div, (int, float)), "result_div should be numeric"

def test_arithmetic_operations():
    """Test that arithmetic operations are correct"""
    lab = load_lab_module()

    expected_add = lab.a + lab.b
    expected_sub = lab.a - lab.b
    expected_mul = lab.a * lab.b
    expected_div = lab.a / lab.b if lab.b != 0 else lab.a / lab.b

    assert abs(lab.result_add - expected_add) < 1e-9, \
        f"Addition incorrect: expected {expected_add}, got {lab.result_add}"
    assert abs(lab.result_sub - expected_sub) < 1e-9, \
        f"Subtraction incorrect: expected {expected_sub}, got {lab.result_sub}"
    assert abs(lab.result_mul - expected_mul) < 1e-9, \
        f"Multiplication incorrect: expected {expected_mul}, got {lab.result_mul}"
    assert abs(lab.result_div - expected_div) < 1e-9, \
        f"Division incorrect: expected {expected_div}, got {lab.result_div}"

def test_print_statement():
    """Test that the print statement exists and runs"""
    # Capture output
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        load_lab_module()
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout

    assert "That's all, folks!" in output, \
        "Print statement should output \"That's all, folks!\""

if __name__ == "__main__":
    print("Running self-grading tests...\n")

    try:
        test_variables_exist()
        print("✓ All variables defined")
    except AssertionError as e:
        print(f"✗ Variables check failed: {e}")
        sys.exit(1)

    try:
        test_variables_are_numeric()
        print("✓ All variables are numeric")
    except AssertionError as e:
        print(f"✗ Type check failed: {e}")
        sys.exit(1)

    try:
        test_arithmetic_operations()
        print("✓ All arithmetic operations correct")
    except AssertionError as e:
        print(f"✗ Arithmetic check failed: {e}")
        sys.exit(1)

    try:
        test_print_statement()
        print("✓ Print statement correct")
    except AssertionError as e:
        print(f"✗ Print statement check failed: {e}")
        sys.exit(1)

    print("\n✓ All tests passed! Grade: 100%")
