"""Unit tests for the payroll module."""

import pytest
from employee_payroll_tracker.employee import FullTimeEmployee, Intern
from employee_payroll_tracker.payroll import (
    calculate_salary,
    apply_tax,
    generate_payslip,
    process_payroll,
)


class TestCalculateSalary:
    """Tests for calculate_salary."""

    def test_delegates_to_employee(self):
        emp = FullTimeEmployee(101, "Alice", 5_000.00, bonus=500.00)
        assert calculate_salary(emp) == 5_500.00


class TestApplyTax:
    """Tests for apply_tax."""

    def test_default_tax_rate(self):
        net = apply_tax(1_000.00)
        assert net == 800.00

    def test_custom_tax_rate(self):
        net = apply_tax(1_000.00, tax_rate=0.10)
        assert net == 900.00

    def test_zero_tax_rate(self):
        net = apply_tax(1_000.00, tax_rate=0.0)
        assert net == 1_000.00

    def test_full_tax_rate(self):
        net = apply_tax(1_000.00, tax_rate=1.0)
        assert net == 0.0

    def test_negative_gross_raises_error(self):
        with pytest.raises(ValueError, match="cannot be negative"):
            apply_tax(-100.00)

    def test_tax_rate_too_high_raises_error(self):
        with pytest.raises(ValueError, match="between 0 and 1"):
            apply_tax(1_000.00, tax_rate=1.5)

    def test_tax_rate_negative_raises_error(self):
        with pytest.raises(ValueError, match="between 0 and 1"):
            apply_tax(1_000.00, tax_rate=-0.1)

    def test_rounding(self):
        net = apply_tax(99.99, tax_rate=0.20)
        assert net == 79.99


class TestGeneratePayslip:
    """Tests for generate_payslip."""

    def test_contains_employee_info(self):
        emp = Intern(301, "Eve", stipend=1_200.00)
        slip = generate_payslip(emp)
        assert "Eve" in slip
        assert "301" in slip
        assert "Intern" in slip
        assert "1200.00" in slip

    def test_contains_tax_deduction(self):
        emp = FullTimeEmployee(101, "Alice", 5_000.00)
        slip = generate_payslip(emp)
        assert "Tax" in slip
        assert "Net Pay" in slip
        assert "Gross Pay" in slip

    def test_contains_separator_lines(self):
        emp = FullTimeEmployee(101, "Alice", 5_000.00)
        slip = generate_payslip(emp)
        assert slip.startswith("=")
        assert slip.endswith("=")


class TestProcessPayroll:
    """Tests for process_payroll."""

    def test_returns_list_of_payslips(self):
        employees = [
            FullTimeEmployee(101, "Alice", 5_000.00),
            Intern(301, "Eve", stipend=1_200.00),
        ]
        results = process_payroll(employees)
        assert len(results) == 2
        assert all(isinstance(s, str) for s in results)

    def test_empty_list(self):
        assert process_payroll([]) == []
