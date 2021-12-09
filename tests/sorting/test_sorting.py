from src.sorting import sort_by

salary = [
    {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-02-03"},
    {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-02-04"},
    {"max_salary": 1600, "min_salary": 9, "date_posted": "2020-02-01"},
]

min_salary = [
    {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-02-03"},
    {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-02-04"},
    {"max_salary": 1600, "min_salary": 9, "date_posted": "2020-02-01"},
]


def test_sort_by_criteria():
    assert sort_by(salary, "max_salary") == min_salary
