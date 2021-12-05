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


def test_sort_by_criteria():
    with pytest.raises(ValueError, match="invalid sorting criteria: tanajura"):
        sort_by(JOBS, 'tanajura')
