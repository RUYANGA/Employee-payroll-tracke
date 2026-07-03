# Professional Prints — Employee Payroll Tracker

> **Audience:** Technical reviewers, hiring managers, and peers.
> This document provides verifiable evidence of a complete software engineering workflow: development, testing, static analysis, debugging, and version control.

---

## Table of Contents

1. [Application Execution](#1-application-execution)
2. [Test Suite Results](#2-test-suite-results)
3. [Static Analysis & Formatting](#3-static-analysis--formatting)
4. [Debugging Walkthrough](#4-debugging-walkthrough)
5. [Commit History](#5-commit-history)
6. [Project Structure](#6-project-structure)
7. [Validation Coverage Matrix](#7-validation-coverage-matrix)

---

## 1. Application Execution

Full payroll run with 6 employees (2 Full-Time, 2 Contract, 2 Intern):

```
$ poetry run python -m employee_payroll_tracker.main

======================================================
         PAYSLIP — FULL-TIME
======================================================
  Employee  :  Alice Johnson
  ID        :  101
  Type      :  Full-Time
------------------------------------------------------
  Gross Pay :  $  5500.00
  Tax (20%) :  $  1100.00
------------------------------------------------------
  Net Pay   :  $  4400.00
======================================================

======================================================
         PAYSLIP — FULL-TIME
======================================================
  Employee  :  Bob Smith
  ID        :  102
  Type      :  Full-Time
------------------------------------------------------
  Gross Pay :  $  4500.00
  Tax (20%) :  $   900.00
------------------------------------------------------
  Net Pay   :  $  3600.00
======================================================

======================================================
         PAYSLIP — CONTRACT
======================================================
  Employee  :  Carol Davis
  ID        :  201
  Type      :  Contract
------------------------------------------------------
  Gross Pay :  $  5400.00
  Tax (20%) :  $  1080.00
------------------------------------------------------
  Net Pay   :  $  4320.00
======================================================

======================================================
         PAYSLIP — CONTRACT
======================================================
  Employee  :  David Lee
  ID        :  202
  Type      :  Contract
------------------------------------------------------
  Gross Pay :  $  4400.00
  Tax (20%) :  $   880.00
------------------------------------------------------
  Net Pay   :  $  3520.00
======================================================

======================================================
         PAYSLIP — INTERN
======================================================
  Employee  :  Eve Martin
  ID        :  301
  Type      :  Intern
------------------------------------------------------
  Gross Pay :  $  1200.00
  Tax (20%) :  $   240.00
------------------------------------------------------
  Net Pay   :  $   960.00
======================================================

======================================================
         PAYSLIP — INTERN
======================================================
  Employee  :  Frank Wilson
  ID        :  302
  Type      :  Intern
------------------------------------------------------
  Gross Pay :  $  1000.00
  Tax (20%) :  $   200.00
------------------------------------------------------
  Net Pay   :  $   800.00
======================================================

Processed 6 employee(s) successfully.
```

**Verification checklist:**

| Check | Result |
|---|---|
| All 3 employee types displayed | ✅ Full-Time, Contract, Intern |
| Gross pay computed per role logic | ✅ Bonus added, hours × rate, fixed stipend |
| Tax deducted at 20 % | ✅ Net Pay = Gross Pay × 0.80 |
| Currency formatting | ✅ Right-aligned `$` values |
| Zero runtime errors | ✅ Exit code 0 |

---

## 2. Test Suite Results

```
$ poetry run pytest tests/ -v

============================= test session starts ==============================
platform linux -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0
rootdir: .../employee-payroll-tracker
configfile: pyproject.toml
collected 41 items

tests/test_employee.py::TestFullTimeEmployee::test_create_valid_employee PASSED
tests/test_employee.py::TestFullTimeEmployee::test_salary_negative_raises_error PASSED
tests/test_employee.py::TestFullTimeEmployee::test_salary_zero_raises_error PASSED
tests/test_employee.py::TestFullTimeEmployee::test_bonus_negative_raises_error PASSED
tests/test_employee.py::TestFullTimeEmployee::test_bonus_zero_is_valid PASSED
tests/test_employee.py::TestFullTimeEmployee::test_string_representation PASSED
tests/test_employee.py::TestContractEmployee::test_create_valid_contractor PASSED
tests/test_employee.py::TestContractEmployee::test_hourly_rate_negative_raises_error PASSED
tests/test_employee.py::TestContractEmployee::test_hours_worked_negative_raises_error PASSED
tests/test_employee.py::TestContractEmployee::test_hours_worked_exceeds_max_raises_error PASSED
tests/test_employee.py::TestContractEmployee::test_calculate_salary_zero_hours PASSED
tests/test_employee.py::TestIntern::test_create_valid_intern PASSED
tests/test_employee.py::TestIntern::test_stipend_negative_raises_error PASSED
tests/test_employee.py::TestIntern::test_stipend_zero_raises_error PASSED
tests/test_employee.py::TestIntern::test_calculate_salary PASSED
tests/test_employee.py::TestEmployeeBase::test_cannot_instantiate_abstract_class PASSED
tests/test_employee.py::TestEmployeeBase::test_salary_setter_validates PASSED
tests/test_payroll.py::TestCalculateSalary::test_delegates_to_employee PASSED
tests/test_payroll.py::TestApplyTax::test_default_tax_rate PASSED
tests/test_payroll.py::TestApplyTax::test_custom_tax_rate PASSED
tests/test_payroll.py::TestApplyTax::test_zero_tax_rate PASSED
tests/test_payroll.py::TestApplyTax::test_full_tax_rate PASSED
tests/test_payroll.py::TestApplyTax::test_negative_gross_raises_error PASSED
tests/test_payroll.py::TestApplyTax::test_tax_rate_too_high_raises_error PASSED
tests/test_payroll.py::TestApplyTax::test_tax_rate_negative_raises_error PASSED
tests/test_payroll.py::TestApplyTax::test_rounding PASSED
tests/test_payroll.py::TestGeneratePayslip::test_contains_employee_info PASSED
tests/test_payroll.py::TestGeneratePayslip::test_contains_tax_deduction PASSED
tests/test_payroll.py::TestGeneratePayslip::test_contains_separator_lines PASSED
tests/test_payroll.py::TestProcessPayroll::test_returns_list_of_payslips PASSED
tests/test_payroll.py::TestProcessPayroll::test_empty_list PASSED
tests/test_utils.py::TestFormatCurrency::test_format_whole_number PASSED
tests/test_utils.py::TestFormatCurrency::test_format_with_cents PASSED
tests/test_utils.py::TestFormatCurrency::test_format_zero PASSED
tests/test_utils.py::TestFormatCurrency::test_format_large_number PASSED
tests/test_utils.py::TestValidatePositiveNumber::test_valid_positive PASSED
tests/test_utils.py::TestValidatePositiveNumber::test_zero_raises_error PASSED
tests/test_utils.py::TestValidatePositiveNumber::test_negative_raises_error PASSED
tests/test_utils.py::TestValidateNonNegativeNumber::test_valid_positive PASSED
tests/test_utils.py::TestValidateNonNegativeNumber::test_valid_zero PASSED
tests/test_utils.py::TestValidateNonNegativeNumber::test_negative_raises_error PASSED

============================== 41 passed in 0.08s ==============================
```

### Test breakdown by module

| Module | Tests | Focus Areas |
|---|---|---|
| `test_employee.py` | 17 | Creation, property validation, boundary values, abstract enforcement |
| `test_payroll.py` | 14 | Tax logic, payslip formatting, batch processing, edge cases |
| `test_utils.py` | 10 | Currency formatting, positive/non-negative validation |

---

## 3. Static Analysis & Formatting

```
$ poetry run ruff check src/
All checks passed!

$ poetry run ruff format --check src/
5 files already formatted
```

**Tools used:**

| Tool | Version | Role |
|---|---|---|
| Ruff (linter) | 0.15.20 | PEP 8 compliance, error detection |
| Ruff (formatter) | 0.15.20 | Consistent code style (88 char width, double quotes) |
| Pytest | 9.1.1 | Unit and integration testing |

---

## 4. Debugging Walkthrough

### 4.1 Bug Detected in Skeleton Code

The original `employee.py` contained a critical bug in the salary setter:

```python
# BUG: Original code — causes infinite recursion
@salary.setter
def salary(self, value):
    if value <= 0:
        ValueError('Salary must be great than zero')  # Not raised!
    return self.salary  # Calls the property getter again → recursion
```

**Root cause:** `ValueError` was constructed but never `raise`d, and `self.salary` in the setter called the getter, creating infinite recursion.

### 4.2 Debugging with pdb (Command Line)

```
$ poetry run python -m pdb src/employee_payroll_tracker/main.py
> .../main.py(1)<module>()
-> """CLI entry point for the Employee Payroll Tracker."""
(Pdb) break employee.py:29
Breakpoint 1 at .../employee.py:29
(Pdb) continue
> .../employee.py(29)__init__()
-> self.salary = salary
(Pdb) print(f"Setting salary to {salary}")
Setting salary to 5000.0
(Pdb) step
--Call--
> .../employee.py(32)salary()
-> def salary(self) -> float:
(Pdb) return
--Return--
> .../employee.py(34)salary()->5000.0
(Pdb) continue
```

### 4.3 Debugging with breakpoint() (Built-in)

Insert a breakpoint directly in the code:

```python
def process_payroll(employees: list) -> list:
    breakpoint()  # Execution pauses here in debugger
    return [generate_payslip(emp) for emp in employees]
```

When the application hits this line, the debugger drops into an interactive `(Pdb)` shell:

```
(Pdb) len(employees)
6
(Pdb) [e.employee_type() for e in employees]
['Full-Time', 'Full-Time', 'Contract', 'Contract', 'Intern', 'Intern']
(Pdb) employees[0].calculate_salary()
5500.0
(Pdb) continue
```

### 4.4 Debugging in VS Code

To debug in VS Code, create `.vscode/launch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Payroll Tracker",
            "type": "debugpy",
            "request": "launch",
            "module": "employee_payroll_tracker.main",
            "console": "integratedTerminal"
        },
        {
            "name": "Python: Test All",
            "type": "debugpy",
            "request": "launch",
            "module": "pytest",
            "args": ["tests/", "-v"],
            "console": "integratedTerminal"
        }
    ]
}
```

Set breakpoints by clicking the gutter in any `.py` file, then press `F5`.

### 4.5 Fix Applied

The corrected setter:

```python
@salary.setter
def salary(self, value: float) -> None:
    if value <= 0:
        raise ValueError("Salary must be greater than zero.")
    self._salary = value
```

After the fix, all 41 tests pass and the application runs without errors.

---

## 5. Commit History

```
$ git log --oneline --graph

* 249fe7a docs: update README with complete project documentation
* 042990c chore: configure CI/CD, update dependencies, add requirements.txt
* b5b6771 test: add comprehensive unit tests for all modules
* e236bdd feat: implement CLI entry point with sample employee data
* 2e8b283 feat: add utility functions module
* 5390b99 feat: implement payroll module with tax and payslip generation
* d838248 feat: implement Employee base class and role-specific subclasses
* 187f6a3 chore: initialize Poetry project and project structure
```

**Commit convention:** [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `test:`, `docs:`, `chore:`)

| Category | Count |
|---|---|
| Features | 4 |
| Tests | 1 |
| Documentation | 1 |
| Chores | 2 |
| **Total** | **8** |

---

## 6. Project Structure

```
employee-payroll-tracker/
├── .github/workflows/ci.yml        # GitHub Actions: lint + test on push/PR
├── prints/
│   └── professionals.md            # This file — prints & debugging evidence
├── src/employee_payroll_tracker/
│   ├── __init__.py
│   ├── employee.py                 # Employee ABC + FullTimeEmployee, ContractEmployee, Intern
│   ├── payroll.py                  # calculate_salary, apply_tax, generate_payslip, process_payroll
│   ├── utils.py                    # format_currency, validate_* helpers
│   └── main.py                     # CLI entry point
├── tests/
│   ├── __init__.py
│   ├── test_employee.py            # 17 tests
│   ├── test_payroll.py             # 14 tests
│   └── test_utils.py               # 10 tests
├── pyproject.toml                  # Poetry config with dev dependencies
├── requirements.txt                # pip alternative
└── README.md                       # Full project documentation
```

---

## 7. Validation Coverage Matrix

| Requirement | Status | Evidence |
|---|---|---|
| Python 3.12+ compatible | ✅ | Poetry config `>=3.12`, tested on 3.12.3 |
| Virtual environment (venv) | ✅ | `.venv/` created by Poetry |
| Lists & Dictionaries | ✅ | Employee list in `main.py`, dictionary mapping per spec |
| Arithmetic operations | ✅ | Salary computation in all 3 subclasses |
| Conditional logic | ✅ | Property setters validate ranges |
| Loops | ✅ | `process_payroll` processes iterable |
| Modular functions | ✅ | `calculate_salary`, `apply_tax`, `generate_payslip` |
| Module organization | ✅ | `employee.py`, `payroll.py`, `utils.py`, `main.py` |
| OOP — Inheritance | ✅ | `FullTimeEmployee(Employee)`, etc. |
| OOP — Encapsulation | ✅ | Private `_salary`, `_bonus`, `_hours_worked` |
| OOP — Polymorphism | ✅ | Same `calculate_salary()` call → different behavior |
| `@property` decorators | ✅ | `salary`, `bonus`, `stipend`, `hourly_rate`, `hours_worked` |
| Validation (salary > 0) | ✅ | `raise ValueError(...)` in setter |
| PEP 8 compliance | ✅ | Ruff linter: 0 errors |
| Docstrings | ✅ | Module, class, function, and `@property` docstrings |
| GitHub Actions CI | ✅ | `.github/workflows/ci.yml` |
| Debugging evidence | ✅ | Sections 4.1–4.5 above |
| requirements.txt | ✅ | pip-compatible dependency file |
| README.md | ✅ | Setup, usage, sample output, structure |

---

*Generated: 2026-07-03  |  Python 3.12.3  |  Employee Payroll Tracker v0.2.0*
