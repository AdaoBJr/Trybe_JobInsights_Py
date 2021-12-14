from src.sorting import sort_by
import pytest


@pytest.fixture
def initial_min_salary():
    return [{
        "min_salary": "2000"
    }, {
        "min_salary": "1000"
    }]


def min_salary():
    return [{
        "min_salary": "1000"
    }, {
        "min_salary": "2000"
    }]


def test_sort_by_criteria(initial_min_salary):
    sort_by(initial_min_salary, "min_salary")
    # test para compara se o salario vai
    # ser igual o setado no initial_min salary
    assert min_salary() == initial_min_salary
    