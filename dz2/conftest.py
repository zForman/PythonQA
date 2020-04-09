import pytest

data_dict = {"A1": "123", "A2": "456"}
set_values = {'10', 'string', 'False', 'Cucumber', 'Pen'}


@pytest.fixture(params=list(data_dict.items()))
def fixture_dict(request):
    return request.param


class TestClass:

    def __init__(self, key):
        self.key = key.keys()

    @staticmethod
    def extract_keys_dict(value):
        result = []
        for i in value.values():
            result.append(i)
        return result


@pytest.fixture
def fixture_return_dictionary():
    return TestClass(key=data_dict)


@pytest.fixture(params='python')
def fixture_return_string(request):
    return request.param


@pytest.fixture(params=set_values)
def fixture_return_set(request):
    return request.param
