from src.sorting import sort_by
import pytest


mockJobs = [
    {
        "max_salary": "112227",
        "min_salary": "58824",
        "date_posted": "2020-05-02",
    },
    {
        "max_salary": "11227",
        "min_salary": "5882",
        "date_posted": "2020-05-07",
    },
    {
        "max_salary": "151998",
        "min_salary": "90454",
        "date_posted": "2020-04-28",
    },
]


def test_sort_by_criteria():

    result2 = sort_by(mockJobs, "min_salary")
    assert result2[0] == mockJobs[1]

    result1 = sort_by(mockJobs, "max_salary")
    assert result1[0] == mockJobs[2]

    result3 = sort_by(mockJobs, "date_posted")
    assert result3[0] == mockJobs[2]

    with pytest.raises(ValueError):
        sort_by(mockJobs, "testes")
