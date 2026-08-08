# GitHub Setup Instructions

## Quick Start

1. Create a new GitHub repository
2. Clone it to your machine
3. Copy these files into the repository:
   - `lab.py`
   - `test_lab.py`
   - `README.md`
   - `.gitignore`

4. Create the GitHub Actions workflow:
   - Create folder: `.github/workflows/`
   - Move `test.yml` → `.github/workflows/test.yml`

5. Push to GitHub:
   ```bash
   git add .
   git commit -m "Initial commit: add lab with auto-grading"
   git push origin main
   ```

## Automatic Grading

Once set up, tests run automatically when:
- You push code
- Someone submits a pull request

Results appear as a badge in your repo showing pass/fail status.

## Local Testing Before Push

Run tests locally first:
```bash
python test_lab.py
```

This catches errors before they're pushed to GitHub.

## Modifying the Lab

To create a new lab from this template:

1. Copy all files
2. Update `lab.py` with your exercise
3. Update `test_lab.py` with your test cases
4. Update `README.md` with new instructions
5. Push to GitHub

The same auto-grading system will work for any Python lab!
