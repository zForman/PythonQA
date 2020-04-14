import pytest


def test_string_one(fixture_test_class):
    assert fixture_test_class.strip_and_split()[0] == 'Hello'
    assert fixture_test_class.strip_and_split()[1] == 'World!'


def test_string_two(lower_string):
    assert lower_string == 'Hello, World!'.lower()


def test_string_three(return_string):
    assert return_string == 13


def test_string_four(fixture_test_class):
    assert 'llo' in fixture_test_class.string


@pytest.mark.parametrize('string_value', ['Hello, World!'])
def test_string_five(string_value, fixture_test_class):
    assert fixture_test_class.string == string_value
