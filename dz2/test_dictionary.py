import pytest


def test_dict_one(fixture_dict):
    string = []
    for a in fixture_dict:
        string.append(a)
    assert string in ['A1', '123'] or ['A2', '456']


def test_dict_two(fixture_return_dictionary):
    assert fixture_return_dictionary.extract_keys_dict({"A1": "123", "A2": "456"}) == ['123', '456']


@pytest.mark.parametrize('dict_val', {"A1": "123", "A2": "456"})
def test_dict_three(dict_val, fixture_return_dictionary):
    assert dict_val in fixture_return_dictionary.key
