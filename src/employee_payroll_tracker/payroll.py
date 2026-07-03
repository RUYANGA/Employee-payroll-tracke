"""Payroll module for salary computation, taxation, and payslip generation.


Functions:
    calculate_salary: Delegates to the employee's own calculation logic.
    apply_tax: Deducts a flat tax rate from gross salary.
    generate_payslip: Creates a formatted text payslip for an employee.
    process_payroll: Processes a list of employees and returns payslips.
"""

from typing import List

from employee_payroll_tracker.logger import get_logger

logger = get_logger(__name__)

TAX_RATE = 0.20


def calculate_salary(employee) -> float:
    """Calculate the total gross salary for an *employee*.

    Args:
        employee: An Employee instance (or subclass).

    Returns:
        The gross salary computed by the employee's own logic.
    """
    gross = employee.calculate_salary()
    logger.debug(
        "Gross salary for %s (ID: %d): %.2f", employee.name, employee.emp_id, gross
    )
    return gross


def apply_tax(gross_salary: float, tax_rate: float = TAX_RATE) -> float:
    """Apply a flat tax rate and return the net (after-tax) salary.

    Args:
        gross_salary: Total salary before tax.
        tax_rate: Tax rate as a decimal (default 0.20).

    Returns:
        Net salary after tax deduction.
    """
    if gross_salary < 0:
        logger.error("Rejected negative gross salary: %.2f", gross_salary)
        raise ValueError("Gross salary cannot be negative.")
    if not 0 <= tax_rate <= 1:
        logger.error("Rejected invalid tax rate: %.2f", tax_rate)
        raise ValueError("Tax rate must be between 0 and 1.")
    net = round(gross_salary * (1 - tax_rate), 2)
    tax_amount = round(gross_salary - net, 2)
    logger.info(
        "Applied tax: gross=%.2f, tax=%.2f (%.0f%%), net=%.2f",
        gross_salary,
        tax_amount,
        tax_rate * 100,
        net,
    )
    return net


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

    logger.info(
        "Generated payslip for %s (ID: %d) — gross=%.2f, net=%.2f",
        employee.name,
        employee.emp_id,
        gross,
        net,
    )

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
    if not employees:
        logger.warning("process_payroll called with empty employee list")
        return []

    logger.info("Processing payroll for %d employee(s)", len(employees))
    payslips = [generate_payslip(emp) for emp in employees]
    logger.info("Payroll complete — %d payslip(s) generated", len(payslips))
    return payslips
