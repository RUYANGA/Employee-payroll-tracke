"""CLI entry point for the Employee Payroll Tracker.

Creates sample employees across all three categories, processes the
payroll, and displays formatted payslips to the console.
"""

from employee_payroll_tracker.employee import (
    FullTimeEmployee,
    ContractEmployee,
    Intern,
)
from employee_payroll_tracker.payroll import process_payroll


def main() -> None:
    """Run the payroll demonstration with sample employees."""
    employees = [
        FullTimeEmployee(
            emp_id=101, name="Alice Johnson", base_salary=5_000.00, bonus=500.00
        ),
        FullTimeEmployee(
            emp_id=102, name="Bob Smith", base_salary=4_200.00, bonus=300.00
        ),
        ContractEmployee(
            emp_id=201, name="Carol Davis", hourly_rate=45.00, hours_worked=120
        ),
        ContractEmployee(
            emp_id=202, name="David Lee", hourly_rate=50.00, hours_worked=88
        ),
        Intern(emp_id=301, name="Eve Martin", stipend=1_200.00),
        Intern(emp_id=302, name="Frank Wilson", stipend=1_000.00),
    ]

    payslips = process_payroll(employees)

    for payslip in payslips:
        print(payslip)
        print()

    print(f"Processed {len(employees)} employee(s) successfully.")


if __name__ == "__main__":
    main()
