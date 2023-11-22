import pytest
from safe_calculator import SafeCalculator
from unittest.mock import MagicMock


def test_divide_should_not_raise_any_error_when_authorized():
    # TODO: write a test that fails due to the bug in SafeCalculator.add
    authorizer = Authorizer()
    safeCalculator = SafeCalculator(authorizer)
    assert(safeCalculator.add(1,2) == 3)

class Authorizer:

    def authorize(self):
        return True
