import pytest


@pytest.mark.parametrize('expected_values', [{2.0, "Nicholas", (1, 2, 3)}])
def test_set_one(element_in_set, expected_values):
    assert expected_values == element_in_set


def test_set_two(element_in_set):
    assert 'Nicholas' in element_in_set


@pytest.mark.parametrize('pass_value', ['orange'])
def test_set_three(set_is, pass_value):
    assert 'orange' in set_is.add_item(pass_value)


@pytest.mark.parametrize('pass_value', [{2.0, "Nicholas", (1, 2, 3)}])
def test_set_four(set_is, pass_value):
    assert set_is.value.issuperset(pass_value)


@pytest.mark.parametrize('pass_value', [{2.0, 'Green', "Nicholas", (1, 2, 3)}])
def test_set_five(element_in_set, pass_value):
    assert pass_value.difference(element_in_set)
