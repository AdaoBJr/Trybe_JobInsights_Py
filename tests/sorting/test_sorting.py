import pytest
from src.sorting import sort_by
from src.jobs import read

criteria_keys = [
    "date_posted",
    "max_salary",
    "min_salary",
]

jobs = read('src/jobs.csv')


def test_sort_by_criteria():
    with pytest.raises(ValueError,
                       match="invalid sorting criteria: date_create"):
        sort_by(jobs, 'date_create')
