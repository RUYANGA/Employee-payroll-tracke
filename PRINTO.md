# PRINTO — Application Output & Execution Evidence

> Consolidated output log for the Employee Payroll Tracker.
> Captures CLI execution, test results, and static analysis.

---

## 1. CLI Execution

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

---

## 2. Test Suite

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

---

## 3. Static Analysis

```
$ poetry run ruff check src/
All checks passed!

$ poetry run ruff format --check src/
5 files already formatted
```

---

## 4. Git History

```
$ git log --oneline --graph

* a8f27dc docs: add professionals.md with debugging walkthrough and execution prints
* 249fe7a docs: update README with complete project documentation
* 042990c chore: configure CI/CD, update dependencies, add requirements.txt
* b5b6771 test: add comprehensive unit tests for all modules
* e236bdd feat: implement CLI entry point with sample employee data
* 2e8b283 feat: add utility functions module
* 5390b99 feat: implement payroll module with tax and payslip generation
* d838248 feat: implement Employee base class and role-specific subclasses
* 187f6a3 chore: initialize Poetry project and project structure
```

---

## 5. Environment

| Component | Version |
|---|---|
| Python | 3.12.3 |
| Pytest | 9.1.1 |
| Ruff | 0.15.20 |
| Poetry | Latest |
| OS | Linux |
