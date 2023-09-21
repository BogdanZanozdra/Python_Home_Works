import persons
import pytest


@pytest.fixture
def p1():
    return persons.Person('Истрин', 'Иван', 'Петрович', 25)


def test_name(p1):
    assert type(p1.name) == str


def test_age(p1):
    assert type(p1.get_age() == int)
    assert p1.get_age() > 0


if __name__ == '__main__':
    pytest.main(['--v'])




