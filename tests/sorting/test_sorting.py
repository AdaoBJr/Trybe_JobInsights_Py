from src.sorting import sort_by
import pytest


@pytest.fixture
def stock():
    return [
        {"max_salary": 15000, "min_salary": 1},
        {"max_salary": 10000, "min_salary": 200},
        {"max_salary": 1500, "min_salary": 0},
        {"max_salary": 10, "min_salary": 100},
        {"max_salary": 0, "min_salary": 10},
        {"max_salary": -1, "min_salary": 10},
    ]


min_salary_jobs = [
    {"max_salary": 1500, "min_salary": 0},
    {"max_salary": 15000, "min_salary": 1},
    {"max_salary": 0, "min_salary": 10},
    {"max_salary": -1, "min_salary": 10},
    {"max_salary": 10, "min_salary": 100},
    {"max_salary": 10000, "min_salary": 200},
]


def test_sort_by_criteria(stock):
    report = sort_by(stock, "min_salary")
    assert report == min_salary_jobs
