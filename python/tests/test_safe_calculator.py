import pytest
from safe_calculator import SafeCalculator


def test_divide_should_not_raise_any_error_when_authorized():
    # TODO: write a test that fails due to the bug in SafeCalculator.add
    authorizer = Authorizer()
    safeCalculator = SafeCalculator(authorizer)
    safeCalculator.add(1,2)
    pass

class Authorizer:

    def authorize(self):
        return True
