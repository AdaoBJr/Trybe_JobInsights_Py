import pytest
from src.sorting import sort_by
from src.jobs import read

invalid_keys = [
    "date_create",
    None,
]

valid_keys = [
        "date_posted",
        "max_salary",
        "min_salary"
]

jobs = read('src/jobs.csv')


def test_sort_by_criteria():
    # result = sort_by(jobs, 'min_salary')
    # assert result != jobs

    for criteria in invalid_keys:
        with pytest.raises(ValueError,
                           match=f"invalid sorting criteria: {criteria}"):
            sort_by(jobs, criteria)
