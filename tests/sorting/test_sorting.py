from src.sorting import sort_by
import pytest

jobs_list = [
    {"min_salary": 2000, "max_salary": 6000, "date_posted": "2020-0101"},
    {"min_salary": 1000, "max_salary": 5000, "date_posted": "2019-01-01"},
    {"min_salary": 3000, "max_salary": 7000, "date_posted": "2021-01-01"},
]

jobs_list_min = [
    {"min_salary": 1000, "max_salary": 5000, "date_posted": "2019-01-01"},
    {"min_salary": 2000, "max_salary": 6000, "date_posted": "2020-01-01"},
    {"min_salary": 3000, "max_salary": 7000, "date_posted": "2021-01-01"},
]

jobs_list_max_and_date = [
    {"min_salary": 3000, "max_salary": 7000, "date_posted": "2021-01-01"},
    {"min_salary": 2000, "max_salary": 6000, "date_posted": "2020-01-01"},
    {"min_salary": 1000, "max_salary": 5000, "date_posted": "2019-01-01"},
]


def test_sort_by_criteria():
    assert sort_by(jobs_list, "min_salary") == jobs_list_min
    assert sort_by(jobs_list, "max_salary") == jobs_list_max_and_date
    assert sort_by(jobs_list, "date_posted") == jobs_list_max_and_date

    with pytest.raises(
        TypeError, match="missing 1 required positional argument: 'criteria'"
    ):
        sort_by(jobs_list)


# agradecimentos ao pedro
# pr: https://github.com/tryber/sd-010-b-project-job-insights/pull/19
# agradecimentos ao ederson
# https://github.com/tryber/sd-010-b-project-job-insights/pull/47
