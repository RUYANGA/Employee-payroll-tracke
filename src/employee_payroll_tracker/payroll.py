"""Payroll module for salary computation, taxation, and payslip generation.


Functions:
    calculate_salary: Delegates to the employee's own calculation logic.
    apply_tax: Deducts a flat tax rate from gross salary.
    generate_payslip: Creates a formatted text payslip for an employee.
    process_payroll: Processes a list of employees and returns payslips.
"""

from typing import List

TAX_RATE = 0.20


def calculate_salary(employee) -> float:
    """Calculate the total gross salary for an *employee*.

    Args:
        employee: An Employee instance (or subclass).

    Returns:
        The gross salary computed by the employee's own logic.
    """
    return employee.calculate_salary()


def apply_tax(gross_salary: float, tax_rate: float = TAX_RATE) -> float:
    """Apply a flat tax rate and return the net (after-tax) salary.

    Args:
        gross_salary: Total salary before tax.
        tax_rate: Tax rate as a decimal (default 0.20).

    Returns:
        Net salary after tax deduction.
    """
    if gross_salary < 0:
        raise ValueError("Gross salary cannot be negative.")
    if not 0 <= tax_rate <= 1:
        raise ValueError("Tax rate must be between 0 and 1.")
    return round(gross_salary * (1 - tax_rate), 2)


def generate_payslip(employee) -> str:
    """Generate a formatted payslip string for an employee.

    Args:
        employee: An Employee instance.

    Returns:
        A multi-line string containing the complete payslip.
    """
    gross = calculate_salary(employee)
    net = apply_tax(gross)
    tax_amount = round(gross - net, 2)

    lines = [
        "=" * 54,
        f"         PAYSLIP — {employee.employee_type().upper()}",
        "=" * 54,
        f"  Employee  :  {employee.name}",
        f"  ID        :  {employee.emp_id}",
        f"  Type      :  {employee.employee_type()}",
        "-" * 54,
        f"  Gross Pay :  ${gross:>9.2f}",
        f"  Tax (20%) :  ${tax_amount:>9.2f}",
        "-" * 54,
        f"  Net Pay   :  ${net:>9.2f}",
        "=" * 54,
    ]
    return "\n".join(lines)


def process_payroll(employees: List) -> List[str]:
    """Process payroll for a list of employees.

    Args:
        employees: A list of Employee instances.

    Returns:
        A list of formatted payslip strings, one per employee.
    """
    return [generate_payslip(emp) for emp in employees]
