"""Unit tests for the employee module."""

import pytest
from employee_payroll_tracker.employee import (
    Employee,
    FullTimeEmployee,
    ContractEmployee,
    Intern,
)


class TestFullTimeEmployee:
    """Tests for FullTimeEmployee."""

    def test_create_valid_employee(self):
        emp = FullTimeEmployee(101, "Alice", 5_000.00, bonus=500.00)
        assert emp.emp_id == 101
        assert emp.name == "Alice"
        assert emp.salary == 5_000.00
        assert emp.bonus == 500.00
        assert emp.calculate_salary() == 5_500.00
        assert emp.employee_type() == "Full-Time"

    def test_salary_negative_raises_error(self):
        with pytest.raises(ValueError, match="greater than zero"):
            FullTimeEmployee(101, "Alice", -100.00)

    def test_salary_zero_raises_error(self):
        with pytest.raises(ValueError, match="greater than zero"):
            FullTimeEmployee(101, "Alice", 0)

    def test_bonus_negative_raises_error(self):
        with pytest.raises(ValueError, match="cannot be negative"):
            FullTimeEmployee(101, "Alice", 5_000.00, bonus=-50.00)

    def test_bonus_zero_is_valid(self):
        emp = FullTimeEmployee(102, "Bob", 4_000.00, bonus=0.00)
        assert emp.bonus == 0.0
        assert emp.calculate_salary() == 4_000.00

    def test_string_representation(self):
        emp = FullTimeEmployee(101, "Alice", 5_000.00)
        assert str(emp) == "Alice (ID: 101)"


class TestContractEmployee:
    """Tests for ContractEmployee."""

    def test_create_valid_contractor(self):
        emp = ContractEmployee(201, "Carol", 45.00, hours_worked=120)
        assert emp.emp_id == 201
        assert emp.name == "Carol"
        assert emp.hourly_rate == 45.00
        assert emp.hours_worked == 120
        assert emp.calculate_salary() == 45.00 * 120
        assert emp.employee_type() == "Contract"

    def test_hourly_rate_negative_raises_error(self):
        with pytest.raises(ValueError, match="greater than zero"):
            ContractEmployee(201, "Carol", -10.00, hours_worked=40)

    def test_hours_worked_negative_raises_error(self):
        with pytest.raises(ValueError, match="cannot be negative"):
            ContractEmployee(201, "Carol", 45.00, hours_worked=-5)

    def test_hours_worked_exceeds_max_raises_error(self):
        with pytest.raises(ValueError, match="cannot exceed 744"):
            ContractEmployee(201, "Carol", 45.00, hours_worked=800)

    def test_calculate_salary_zero_hours(self):
        emp = ContractEmployee(202, "David", 50.00, hours_worked=0)
        assert emp.calculate_salary() == 0.0


class TestIntern:
    """Tests for Intern."""

    def test_create_valid_intern(self):
        emp = Intern(301, "Eve", stipend=1_200.00)
        assert emp.emp_id == 301
        assert emp.name == "Eve"
        assert emp.stipend == 1_200.00
        assert emp.calculate_salary() == 1_200.00
        assert emp.employee_type() == "Intern"

    def test_stipend_negative_raises_error(self):
        with pytest.raises(ValueError, match="greater than zero"):
            Intern(301, "Eve", stipend=-100.00)

    def test_stipend_zero_raises_error(self):
        with pytest.raises(ValueError, match="greater than zero"):
            Intern(301, "Eve", stipend=0)

    def test_calculate_salary(self):
        emp = Intern(302, "Frank", stipend=1_000.00)
        assert emp.calculate_salary() == 1_000.00


class TestEmployeeBase:
    """Tests for the abstract base class."""

    def test_cannot_instantiate_abstract_class(self):
        with pytest.raises(TypeError):
            Employee(999, "Abstract", 100.00)  # type: ignore

    def test_salary_setter_validates(self):
        class ConcreteEmployee(Employee):
            def calculate_salary(self):
                return self.salary

            def employee_type(self):
                return "Test"

        emp = ConcreteEmployee(1, "Test", 100.00)
        assert emp.salary == 100.00

        with pytest.raises(ValueError, match="greater than zero"):
            emp.salary = -50.00
