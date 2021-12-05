from src.sorting import sort_by
import pytest

CRITERIA = ['min_salary', 'max_salary', 'date_posted']

JOBS = [
    {"job_title": "Dev Front",
        "min_salary": 700,
        "max_salary": 3000,
        "date_posted": "2020-05-10", },
    {"job_title": "Dev Back",
        "min_salary": 600,
        "max_salary": 2000,
        "date_posted": "2020-05-09", },
    {"job_title": "DevOps",
        "min_salary": 500,
        "max_salary": 1000,
        "date_posted": "2020-05-08", },
]

order_by_min = [JOBS[2], JOBS[1], JOBS[0]]
order_by_max = [JOBS[0], JOBS[1], JOBS[2]]
order_date = [JOBS[0], JOBS[1], JOBS[2]]


def test_sort_by_criteria():
    sort_by(JOBS, 'min_salary')
    assert JOBS == order_by_min

    sort_by(JOBS, 'max_salary')
    assert JOBS == order_by_max

    sort_by(JOBS, 'date_posted')
    assert JOBS == order_date

    with pytest.raises(ValueError, match="invalid sorting criteria: tanajura"):
        sort_by(JOBS, 'tanajura')

# Ajuda de pedro para entender um teste que na minha opnião na faz sentido kkk