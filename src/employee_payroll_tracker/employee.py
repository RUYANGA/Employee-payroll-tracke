"""Employee module defining the base Employee class and role-specific subclasses.

Supports full-time, contract, and intern employee types with
encapsulated attributes and property validation.
"""

from abc import ABC, abstractmethod


class Employee(ABC):
    """Abstract base class for all employee types.

    Provides common attributes (emp_id, name, salary) with property
    validation and enforces a contract for salary calculation.
    """

    def __init__(self, emp_id: int, name: str, salary: float) -> None:
        self.emp_id = emp_id
        self.name = name
        self._salary = 0.0
        self.salary = salary

    @property
    def salary(self) -> float:
        """Return the employee's base salary."""
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        """Set the employee's base salary, validating it is positive."""
        if value <= 0:
            raise ValueError("Salary must be greater than zero.")
        self._salary = value

    @abstractmethod
    def calculate_salary(self) -> float:
        """Calculate and return the total payable salary."""
        ...

    @abstractmethod
    def employee_type(self) -> str:
        """Return a human-readable label for the employee role."""
        ...

    def __str__(self) -> str:
        return f"{self.name} (ID: {self.emp_id})"


class FullTimeEmployee(Employee):
    """Full-time employee with a fixed monthly salary and optional bonus."""

    def __init__(
        self, emp_id: int, name: str, base_salary: float, bonus: float = 0.0
    ) -> None:
        self._bonus = 0.0
        super().__init__(emp_id, name, base_salary)
        self.bonus = bonus

    @property
    def bonus(self) -> float:
        """Return the employee's bonus amount."""
        return self._bonus

    @bonus.setter
    def bonus(self, value: float) -> None:
        """Set the bonus, ensuring it is non-negative."""
        if value < 0:
            raise ValueError("Bonus cannot be negative.")
        self._bonus = value

    def calculate_salary(self) -> float:
        """Return base salary plus bonus."""
        return self.salary + self.bonus

    def employee_type(self) -> str:
        return "Full-Time"


class ContractEmployee(Employee):
    """Contract employee paid at an hourly rate for hours worked."""

    def __init__(
        self, emp_id: int, name: str, hourly_rate: float, hours_worked: float
    ) -> None:
        self._hours_worked = 0.0
        super().__init__(emp_id, name, hourly_rate)
        self.hours_worked = hours_worked

    @property
    def hourly_rate(self) -> float:
        """Return the hourly rate (stored as the base salary)."""
        return self.salary

    @hourly_rate.setter
    def hourly_rate(self, value: float) -> None:
        """Set the hourly rate, delegating to the salary setter."""
        if value <= 0:
            raise ValueError("Hourly rate must be greater than zero.")
        self.salary = value

    @property
    def hours_worked(self) -> float:
        """Return the number of hours worked this period."""
        return self._hours_worked

    @hours_worked.setter
    def hours_worked(self, value: float) -> None:
        """Set hours worked, capped at 744 (max in a 31-day month)."""
        if value < 0:
            raise ValueError("Hours worked cannot be negative.")
        if value > 744:
            raise ValueError("Hours worked cannot exceed 744 in a month.")
        self._hours_worked = value

    def calculate_salary(self) -> float:
        """Return hourly rate multiplied by hours worked."""
        return self.hourly_rate * self.hours_worked

    def employee_type(self) -> str:
        return "Contract"


class Intern(Employee):
    """Intern who receives a fixed stipend."""

    def __init__(self, emp_id: int, name: str, stipend: float) -> None:
        super().__init__(emp_id, name, stipend)

    @property
    def stipend(self) -> float:
        """Return the intern's stipend."""
        return self.salary

    @stipend.setter
    def stipend(self, value: float) -> None:
        """Set the stipend, ensuring it is positive."""
        if value <= 0:
            raise ValueError("Stipend must be greater than zero.")
        self.salary = value

    def calculate_salary(self) -> float:
        """Return the fixed stipend amount."""
        return self.salary

    def employee_type(self) -> str:
        return "Intern"
