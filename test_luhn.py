from luhn import is_valid, check_digit


def test_known():
    assert is_valid("79927398713")
    assert not is_valid("79927398710")
    assert check_digit("7992739871") == 3
