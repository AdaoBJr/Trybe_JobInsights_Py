from src.sorting import sort_by
import pytest


def test_sort_by_criteria():
    VALID_JOBS = [
        {
            "min_salary": "1000",
            "max_salary": "5000",
            "date_posted": "2019-05-08",
        },
        {"min_salary": "0", "max_salary": "2000", "date_posted": "2018-05-08"},
        {
            "min_salary": "350",
            "max_salary": "120",
            "date_posted": "2017-05-08",
        },
        {
            "min_salary": "5001",
            "max_salary": "7000",
            "date_posted": "2020-05-08",
        },
    ]
    MIN_SALARY_CRITERIA = "min_salary"
    MAX_SALARY_CRITERIA = "max_salary"
    DATE_POSTED_CRITERIA = "date_posted"
    INVALID_CRITERIA = ""

    sort_by(VALID_JOBS, MIN_SALARY_CRITERIA)
    assert VALID_JOBS[0][MIN_SALARY_CRITERIA] == "0"

    sort_by(VALID_JOBS, MAX_SALARY_CRITERIA)
    assert VALID_JOBS[0][MAX_SALARY_CRITERIA] == "7000"

    sort_by(VALID_JOBS, DATE_POSTED_CRITERIA)
    assert VALID_JOBS[0][DATE_POSTED_CRITERIA] == "2020-05-08"

    with pytest.raises(
        ValueError, match=f"invalid sorting criteria: {INVALID_CRITERIA}"
    ):
        sort_by(VALID_JOBS, INVALID_CRITERIA)
