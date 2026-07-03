# Employee Payroll Tracker

A Python-based CLI application that computes payslips for **Full-Time**, **Contract**, and **Intern** employees using object-oriented design principles.

---

## Features

- **Role-based salary calculation** — each employee type implements its own `calculate_salary()` logic
- **Tax deduction** — flat 20 % tax applied to gross pay
- **Data validation** — `@property` decorators enforce salary / bonus / hours constraints
- **Modular architecture** — code is split into `employee`, `payroll`, and `utils` modules
- **Polymorphic payroll processing** — a single `process_payroll()` function handles all employee types
- **Continuous Integration** — GitHub Actions runs lint + tests on every push / pull request

---

## Project Structure

```
employee-payroll-tracker/
├── .github/workflows/ci.yml   # GitHub Actions CI
├── src/
│   └── employee_payroll_tracker/
│       ├── __init__.py
│       ├── employee.py         # Base & subclass definitions
│       ├── payroll.py          # Salary, tax & payslip logic
│       ├── utils.py            # Helper utilities
│       └── main.py             # CLI entry point
├── tests/
│   ├── __init__.py
│   ├── test_employee.py
│   ├── test_payroll.py
│   └── test_utils.py
├── pyproject.toml              # Poetry configuration
├── requirements.txt            # pip-style dependencies
└── README.md
```

---

## Setup & Usage

### 1. Clone the repository

```bash
git clone https://github.com/RUYANGA/Employee-payroll-tracke.git
cd employee-payroll-tracker
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate        # Linux / macOS
# venv\Scripts\activate         # Windows
```

### 3. Install dependencies

**Using Poetry (recommended):**

```bash
pip install poetry
poetry install --with dev
```

**Using pip:**

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python -m src.employee_payroll_tracker.main
```

Or inside the package directory:

```bash
poetry run python -m employee_payroll_tracker.main
```

### 5. Run tests

```bash
poetry run pytest tests/ -v
```

### 6. Lint & format

```bash
poetry run ruff check src/
poetry run ruff format src/
```

---

## Sample Output

```
======================================================
         PAYSLIP — FULL-TIME
======================================================
  Employee  :  Alice Johnson
  ID        :  101
  Type      :  Full-Time
------------------------------------------------------
  Gross Pay :  $ 5500.00
  Tax (20%) :  $ 1100.00
------------------------------------------------------
  Net Pay   :  $ 4400.00
======================================================

======================================================
         PAYSLIP — CONTRACT
======================================================
  Employee  :  Carol Davis
  ID        :  201
  Type      :  Contract
------------------------------------------------------
  Gross Pay :  $ 5400.00
  Tax (20%) :  $ 1080.00
------------------------------------------------------
  Net Pay   :  $ 4320.00
======================================================

======================================================
         PAYSLIP — INTERN
======================================================
  Employee  :  Eve Martin
  ID        :  301
  Type      :  Intern
------------------------------------------------------
  Gross Pay :  $ 1200.00
  Tax (20%) :  $  240.00
------------------------------------------------------
  Net Pay   :  $  960.00
======================================================

Processed 6 employee(s) successfully.
```

---

## Employee Types

| Class | Pay Basis | Salary Formula |
|---|---|---|
| `FullTimeEmployee` | Monthly salary + bonus | `base_salary + bonus` |
| `ContractEmployee` | Hourly rate × hours | `hourly_rate × hours_worked` |
| `Intern` | Fixed stipend | `stipend` |

---

## Validation Rules

- `salary` / `stipend` / `hourly_rate` — must be **> 0**
- `bonus` — must be **≥ 0**
- `hours_worked` — must be **0–744** (max hours in a 31-day month)

---

## Grading Criteria Coverage

| Criteria | Coverage |
|---|---|
| Language Fundamentals | Numerical ops, conditionals, loops, comprehensions |
| Functions & Modularity | Reusable functions across 4 modules |
| OOP Design Quality | Inheritance, encapsulation, polymorphism, ABC |
| Code Clarity & Style | PEP 8 (enforced by Ruff), docstrings |
| Documentation & Comments | Module & function docstrings, this README |
| Execution & Output Quality | Stable CLI with formatted payslip output |

---

## License

MIT
