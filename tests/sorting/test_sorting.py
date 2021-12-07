from src.sorting import sort_by

jobs_details_list = [
    {"min_salary": 100, "max_salary": 3000, "date_posted": "2021-01-01"},
    {"min_salary": 500, "max_salary": 1000, "date_posted": "2020-01-01"},
    {"min_salary": 300, "max_salary": 5000, "date_posted": "2019-01-01"},
]

min_salary = [
    {"min_salary": 1000, "max_salary": 4000, "date_posted": "2019-01-01"},
    {"min_salary": 2000, "max_salary": 5000, "date_posted": "2021-01-01"},
    {"min_salary": 3000, "max_salary": 6000, "date_posted": "2020-01-01"},
]

max_salary = [
    {"min_salary": 3000, "max_salary": 6000, "date_posted": "2020-01-01"},
    {"min_salary": 2000, "max_salary": 5000, "date_posted": "2021-01-01"},
    {"min_salary": 1000, "max_salary": 4000, "date_posted": "2019-01-01"},
]

date_posted = [
    {"min_salary": 3000, "max_salary": 6000, "date_posted": "2020-01-01"},
    {"min_salary": 2000, "max_salary": 5000, "date_posted": "2021-01-01"},
    {"min_salary": 1000, "max_salary": 4000, "date_posted": "2019-01-01"},
]


def test_sort_by_criteria():
    assert sort_by(jobs_details_list, 'min_salary') == min_salary
    assert sort_by(jobs_details_list, "max_salary") == max_salary
    assert sort_by(jobs_details_list, "date_posted") == date_posted
