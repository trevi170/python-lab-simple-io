# Lab 2.6.1.9: Simple Input and Output

**Objective:** Learn input/output operations and basic arithmetic in Python.

## Instructions

1. Open `lab.py`
2. Define variables `a` and `b` with float values
3. Calculate and store the results of:
   - Addition (a + b) → `result_add`
   - Subtraction (a - b) → `result_sub`
   - Multiplication (a * b) → `result_mul`
   - Division (a / b) → `result_div`
4. The print statement is already provided

## Example

```python
a = 10.5
b = 3.0

result_add = a + b      # 13.5
result_sub = a - b      # 7.5
result_mul = a * b      # 31.5
result_div = a / b      # 3.5

print("That's all, folks!")
```

## Testing

### Option 1: Run directly
```bash
python test_lab.py
```

### Option 2: Use pytest
```bash
pip install pytest
python -m pytest test_lab.py -v
```

### Option 3: GitHub Actions (Automatic)
Tests run automatically on every commit if `.github/workflows/test.yml` is configured.

## Grading Criteria

- ✓ Variables `a` and `b` are defined and numeric
- ✓ `result_add` equals `a + b`
- ✓ `result_sub` equals `a - b`
- ✓ `result_mul` equals `a * b`
- ✓ `result_div` equals `a / b`
- ✓ Print statement outputs "That's all, folks!"

All tests must pass for a 100% grade.
