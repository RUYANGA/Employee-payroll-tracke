"""Unit tests for the utils module."""

import pytest
from employee_payroll_tracker.utils import (
    format_currency,
    validate_positive_number,
    validate_non_negative_number,
)


class TestFormatCurrency:
    """Tests for format_currency."""

    def test_format_whole_number(self):
        assert format_currency(1_234.00) == "$1,234.00"

    def test_format_with_cents(self):
        assert format_currency(99.95) == "$99.95"

    def test_format_zero(self):
        assert format_currency(0.00) == "$0.00"

    def test_format_large_number(self):
        assert format_currency(1_000_000.50) == "$1,000,000.50"


class TestValidatePositiveNumber:
    """Tests for validate_positive_number."""

    def test_valid_positive(self):
        validate_positive_number(100.00, "Salary")

    def test_zero_raises_error(self):
        with pytest.raises(ValueError, match="Salary must be greater than zero"):
            validate_positive_number(0, "Salary")

    def test_negative_raises_error(self):
        with pytest.raises(ValueError, match="Value must be greater than zero"):
            validate_positive_number(-5.00)


class TestValidateNonNegativeNumber:
    """Tests for validate_non_negative_number."""

    def test_valid_positive(self):
        validate_non_negative_number(100.00, "Bonus")

    def test_valid_zero(self):
        validate_non_negative_number(0, "Bonus")

    def test_negative_raises_error(self):
        with pytest.raises(ValueError, match="Bonus cannot be negative"):
            validate_non_negative_number(-5.00, "Bonus")
