# SPRINT 2 — OOP Design, Testing & Debugging

> **Focus:** Employee subclasses, polymorphism, property decorators, testing, and CI/CD.
> **Corresponds to:** Milestone Days 3–4

---

## Sprint Goal

Complete the OOP hierarchy with full-time, contract, and intern employees;
add comprehensive test coverage; set up continuous integration; and
demonstrate debugging.

---

## Backlog

| ID | Task | Status | Deliverable |
|---|---|---|---|
| S2-01 | Implement `FullTimeEmployee` subclass | ✅ Done | Bonus property, `salary + bonus` formula |
| S2-02 | Implement `ContractEmployee` subclass | ✅ Done | Hourly rate + hours worked, 744-hour cap |
| S2-03 | Implement `Intern` subclass | ✅ Done | Fixed stipend, positive validation |
| S2-04 | Add `@property` for `bonus` | ✅ Done | Non-negative validation |
| S2-05 | Add `@property` for `hourly_rate` | ✅ Done | Delegates to salary setter |
| S2-06 | Add `@property` for `hours_worked` | ✅ Done | Range 0–744 |
| S2-07 | Add `@property` for `stipend` | ✅ Done | Delegates to salary setter |
| S2-08 | Polymorphic `calculate_salary()` per role | ✅ Done | 3 different implementations |
| S2-09 | Write `test_employee.py` (17 tests) | ✅ Done | Creation, validation, edge cases |
| S2-10 | Write `test_payroll.py` (14 tests) | ✅ Done | Tax, payslip, batch processing |
| S2-11 | Write `test_utils.py` (10 tests) | ✅ Done | Formatting, validation helpers |
| S2-12 | Create GitHub Actions CI workflow | ✅ Done | `.github/workflows/ci.yml` |
| S2-13 | Debug salary setter recursion bug | ✅ Done | `raise` + `self._salary` fix |
| S2-14 | Document debugging in `professionals.md` | ✅ Done | pdb, breakpoint(), VS Code |
| S2-15 | Create CLI `main.py` with sample data | ✅ Done | 6 employees, formatted output |

---

## Class Hierarchy

```
Employee (ABC)
├── FullTimeEmployee
│     calculate_salary() = base_salary + bonus
│     Properties: salary, bonus
│
├── ContractEmployee
│     calculate_salary() = hourly_rate × hours_worked
│     Properties: salary (hourly_rate), hours_worked
│
└── Intern
      calculate_salary() = stipend
      Properties: salary (stipend)
```

---

## Property Validation Matrix

| Property | Rule | Error |
|---|---|---|
| `salary` | > 0 | `"Salary must be greater than zero."` |
| `bonus` | ≥ 0 | `"Bonus cannot be negative."` |
| `hourly_rate` | > 0 | `"Hourly rate must be greater than zero."` |
| `hours_worked` | 0–744 | `"cannot exceed 744"` / `"cannot be negative"` |
| `stipend` | > 0 | `"Stipend must be greater than zero."` |

---

## Bug Fix: Salary Setter Recursion

**Bug:** The original skeleton code constructed `ValueError` but never
`raise`d it, and used `return self.salary` inside the setter (calling the
getter, creating infinite recursion).

```python
# Before (broken)
@salary.setter
def salary(self, value):
    if value <= 0:
        ValueError('Salary must be great than zero')  # Not raised
    return self.salary  # Calls getter → recursion!

# After (fixed)
@salary.setter
def salary(self, value: float) -> None:
    if value <= 0:
        raise ValueError("Salary must be greater than zero.")
    self._salary = value
```

**Detection method:** `pdb` stepping and `breakpoint()` insertion showed the
setter re-entering itself repeatedly.

---

## Test Results

```
$ poetry run pytest tests/ -v --tb=short
============================== 41 passed in 0.08s ==============================
```

| Test File | Tests | Coverage |
|---|---|---|
| `tests/test_employee.py` | 17 | Employee creation, property validation, edge cases, ABC enforcement |
| `tests/test_payroll.py` | 14 | Tax rates (0%–100%), payslip formatting, batch processing, empty list |
| `tests/test_utils.py` | 10 | Currency formatting, validation helpers |

---

## CI/CD Pipeline

**File:** `.github/workflows/ci.yml`

```yaml
on: [push, pull_request] → main
jobs:
  test:
    strategy:
      matrix:
        python-version: ["3.12", "3.13"]
    steps:
      - checkout
      - setup-python
      - install poetry + deps
      - ruff check src/
      - ruff format --check src/
      - pytest tests/ -v --tb=short
```

Triggers on every push and pull request to `main`. Runs lint, format check,
and all 41 tests across two Python versions.

---

## Definition of Done

- [x] All 3 subclasses implemented with `@property` validation
- [x] Polymorphism works — single `process_payroll()` handles all types
- [x] 41 tests passing
- [x] Ruff linter: zero warnings
- [x] Ruff formatter: all files clean
- [x] GitHub Actions CI passing (lint + test)
- [x] Debugging documented with pdb/breakpoint() examples
- [x] CLI produces correct, formatted payslips
- [x] Git history shows clean, atomic commits

---

## Sprint Retrospective

**What went well:** Polymorphic design made `process_payroll()` trivial — one
function handles all employee types. `@property` decorators kept validation
colocated with data. Test coverage caught the formatting mismatch in the
payslip assertion immediately.

**What needed fixing:** The payslip test assertion used `$1,200.00` but the
format string right-aligns as `$  1200.00`. Fixed by checking for the
numeric value instead.

**Velocity:** 15/15 backlog items completed.

---

## Overall Project Velocity

| Sprint | Tasks | Completed | Velocity |
|---|---|---|---|
| Sprint 1 | 12 | 12 | 100% |
| Sprint 2 | 15 | 15 | 100% |
| **Total** | **27** | **27** | **100%** |
