from src.sorting import sort_by

jobs = [
    {"max_salary": 0, "min_salary": 10},
    {"max_salary": 10, "min_salary": 100},
    {"max_salary": 10000, "min_salary": 200},
    {"max_salary": 15000, "min_salary": 0},
    {"max_salary": 1500, "min_salary": 0},
    {"max_salary": -1, "min_salary": 10},
]


def test_sort_by_criteria():
    report = sort_by(jobs, "min_salary")
    assert {"max_salary": 0, "min_salary": 10} in report
