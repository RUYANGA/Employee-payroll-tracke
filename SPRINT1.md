# SPRINT 1 — Foundation & Core Logic

> **Focus:** Environment setup, data structures, functions, and payroll logic.
> **Corresponds to:** Milestone Days 1–2

---

## Sprint Goal

Establish the project foundation: virtual environment, module structure, data
structures, and the core payroll computation functions.

---

## Backlog

| ID | Task | Status | Deliverable |
|---|---|---|---|
| S1-01 | Initialize Python virtual environment | ✅ Done | `.venv/` with Poetry |
| S1-02 | Configure `pyproject.toml` with dependencies | ✅ Done | `pyproject.toml`, `requirements.txt` |
| S1-03 | Create module directory structure | ✅ Done | `src/`, `tests/`, `employee.py`, `payroll.py`, `utils.py`, `main.py` |
| S1-04 | Define data structures (lists, dicts) | ✅ Done | Employee records list in `main.py` |
| S1-05 | Implement arithmetic & conditional logic | ✅ Done | Salary formulas, validation guards |
| S1-06 | Build `calculate_salary()` function | ✅ Done | `payroll.py` |
| S1-07 | Build `apply_tax()` function | ✅ Done | `payroll.py` — flat 20% tax |
| S1-08 | Build `generate_payslip()` function | ✅ Done | `payroll.py` — formatted payslip |
| S1-09 | Build `process_payroll()` function | ✅ Done | `payroll.py` — batch processing |
| S1-10 | Write utility helpers | ✅ Done | `utils.py` — `format_currency`, validation |
| S1-11 | Set up GitHub repository | ✅ Done | Remote configured |
| S1-12 | Configure `.gitignore` | ✅ Done | Python, venv, IDE, cache rules |

---

## Key Decisions

| Decision | Rationale |
|---|---|
| Poetry for dependency management | Locks versions, handles venv, simpler than pip+venv |
| Flat 20% tax rate | Simple, predictable, easy to test |
| `@property` validation on base class | Single source of truth for salary constraints |
| ABC for Employee base | Enforces `calculate_salary()` contract on all subclasses |

---

## Code Delivered

### `employee.py` — Base class skeleton

```python
class Employee(ABC):
    def __init__(self, emp_id: int, name: str, salary: float):
        self._salary = 0.0
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Salary must be greater than zero.")
        self._salary = value

    @abstractmethod
    def calculate_salary(self) -> float: ...
```

### `payroll.py` — Core functions

```python
def calculate_salary(employee) -> float:
    return employee.calculate_salary()

def apply_tax(gross_salary: float, tax_rate: float = 0.20) -> float:
    if gross_salary < 0:
        raise ValueError("Gross salary cannot be negative.")
    if not 0 <= tax_rate <= 1:
        raise ValueError("Tax rate must be between 0 and 1.")
    return round(gross_salary * (1 - tax_rate), 2)

def generate_payslip(employee) -> str: ...
def process_payroll(employees: list) -> list: ...
```

---

## Definition of Done

- [x] Virtual environment activates without errors
- [x] `poetry install` resolves all dependencies
- [x] Module files compile without `SyntaxError` or `ImportError`
- [x] `pip install -r requirements.txt` works
- [x] Functions accept expected types and return expected types
- [x] Ruff linter passes with zero warnings

---

## Sprint Retrospective

**What went well:** Modular separation of concerns was clear from the start.
Property validation on the base `Employee` class prevented invalid data from
propagating.

**What needed fixing:** The original `employee.py` skeleton had a bug where
`ValueError` was not raised and the setter caused infinite recursion (fixed
in Sprint 2 debugging).

**Velocity:** 12/12 backlog items completed.
