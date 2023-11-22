from safe_calculator import SafeCalculator

class DummyAuthorizer:
    def authorize(self):
        return True

def test_divide_should_not_raise_any_error_when_authorized():
    # TODO: write a test that fails due to the bug in
    # SafeCalculator.add

    authorizer = DummyAuthorizer()
    calculator = SafeCalculator(authorizer)

    result = calculator.add(2, 3)

    assert result == 5