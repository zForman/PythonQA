import pytest

string = "Hello, World!"
mixed_set = {2.0, "Nicholas", (1, 2, 3)}
data_dict = {"A1": "123", "A2": "456"}
data_list = ["apple", "banana", "cherry"]


# list
class TestListClass:
    def __init__(self, value):
        self.value = value

    def return_list_value(self, value):
        result = self.value
        result[1] = value
        return result


@pytest.fixture
def fixture_return_list_class():
    return TestListClass(data_list)


@pytest.fixture
def fixture_list():
    return data_list


# Dict
class TestDicClass:

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
    return TestDicClass(key=data_dict)


@pytest.fixture(params=list(data_dict.items()))
def fixture_dict(request):
    return request.param


# String
class TestClass:

    def __init__(self, string):
        self.string = string

    def strip_and_split(self):
        return self.string.replace(" ", "").split(',')

    def len_string(self):
        return len(self.string)


@pytest.fixture
def return_string():
    return len("Hello, World!")


@pytest.fixture
def lower_string():
    return string.lower()


@pytest.fixture
def fixture_test_class():
    return TestClass(string)


# Set
class TestSetClass:

    def __init__(self, value):
        self.value = value

    def add_item(self, item):
        result = []
        result += self.value
        result.append(item)
        return result


@pytest.fixture()
def set_is():
    return TestSetClass(mixed_set)


@pytest.fixture()
def element_in_set():
    return mixed_set
