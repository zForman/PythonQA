import pytest
expected_value = ["apple", "banana", "cherry"]


def test_list_one(fixture_list):
    assert expected_value == fixture_list


def test_list_two(fixture_return_list_class):
    assert fixture_return_list_class.value[-1] == expected_value[-1]


def test_list_three(fixture_return_list_class):
    assert fixture_return_list_class.value[-1]*2 == 'cherrycherry'


@pytest.mark.parametrize('expected_value', ['apple', 'banana', 'cherry'])
def test_list_four(fixture_list, expected_value):
    assert expected_value in fixture_list


def test_list_five(fixture_return_list_class):
    assert fixture_return_list_class.return_list_value('coconut') == ['apple', 'coconut', 'cherry']
