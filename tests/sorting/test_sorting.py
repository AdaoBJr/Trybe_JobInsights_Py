import pytest
from src.sorting import sort_by

jobs = [
    {'min_salary': 3500, 'max_salary': 4000, 'date_posted': '01-03-2021'},
    {'min_salary': 0, 'max_salary': 1500, 'date_posted': '01-01-2021'},
    {'min_salary': 4000, 'max_salary': 7000, 'date_posted': '01-04-2021'},
    {'min_salary': 1500, 'max_salary': 3500, 'date_posted': '01-02-2021'},
]


def test_sort_by_criteria():

    min_salary_order = [
        {'min_salary': 0, 'max_salary': 1500, 'date_posted': '01-01-2021'},
        {'min_salary': 1500, 'max_salary': 3500, 'date_posted': '01-02-2021'},
        {'min_salary': 3500, 'max_salary': 4000, 'date_posted': '01-03-2021'},
        {'min_salary': 4000, 'max_salary': 7000, 'date_posted': '01-04-2021'},
    ]

    max_salary_order = [
        {'min_salary': 4000, 'max_salary': 7000, 'date_posted': '01-04-2021'},
        {'min_salary': 3500, 'max_salary': 4000, 'date_posted': '01-03-2021'},
        {'min_salary': 1500, 'max_salary': 3500, 'date_posted': '01-02-2021'},
        {'min_salary': 0, 'max_salary': 1500, 'date_posted': '01-01-2021'},
    ]

    date_posted_order = [
        {'min_salary': 4000, 'max_salary': 7000, 'date_posted': '01-04-2021'},
        {'min_salary': 3500, 'max_salary': 4000, 'date_posted': '01-03-2021'},
        {'min_salary': 1500, 'max_salary': 3500, 'date_posted': '01-02-2021'},
        {'min_salary': 0, 'max_salary': 1500, 'date_posted': '01-01-2021'},
    ]

    with pytest.raises(TypeError):
        sort_by(jobs)

    sort_by(jobs, 'min_salary')
    assert(jobs == min_salary_order)
    sort_by(jobs, 'max_salary')
    assert(jobs == max_salary_order)
    sort_by(jobs, 'date_posted')
    assert(jobs == date_posted_order)
