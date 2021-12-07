from src.sorting import sort_by
import pytest

jobs = [
    {"min_salary": 2500, "max_salary": 3500, "date_posted": "2021-12-01"},
    {"min_salary": 2000, "max_salary": 3000, "date_posted": "2021-11-01"},
    {"min_salary": 1500, "max_salary": 2500, "date_posted": "2021-10-01"},
]

order_by_min = [jobs[2], jobs[1], jobs[0]]
order_by_max = [jobs[0], jobs[1], jobs[2]]
order_by_date = [jobs[0], jobs[1], jobs[2]]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == order_by_min
    sort_by(jobs, "max_salary")
    assert jobs == order_by_max
    sort_by(jobs, "date_posted")
    assert jobs == order_by_date

    with pytest.raises(ValueError, match='invalid sorting'):
        sort_by(jobs, 'premium')
