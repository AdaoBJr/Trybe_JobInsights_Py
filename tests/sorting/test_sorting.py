import pytest
from src.sorting import sort_by


invalid_keys = [
    "date_create",
    None,
]

# Source https://github.com/tryber/sd-010-b-project-job-insights/pull/64/files
jobs = [
        {"max_salary": 94648, "min_salary": 82243,
                              "date_posted": '2020-04-30'},
        {"max_salary": 107487, "min_salary": 62576,
                               "date_posted": '2020-05-05'},
        {"max_salary": 118794, "min_salary": 81591,
                               "date_posted": '2020-04-28'},
    ]

expected_min_salary = [
    {"max_salary": 107487, "min_salary": 62576, "date_posted": '2020-05-05'},
    {"max_salary": 118794, "min_salary": 81591, "date_posted": '2020-04-28'},
    {"max_salary": 94648, "min_salary": 82243, "date_posted": '2020-04-30'},
]

expected_max_salary = [
    {"max_salary": 118794, "min_salary": 81591, "date_posted": '2020-04-28'},
    {"max_salary": 107487, "min_salary": 62576, "date_posted": '2020-05-05'},
    {"max_salary": 94648, "min_salary": 82243, "date_posted": '2020-04-30'},
]

expected_date_post = [
    {"max_salary": 107487, "min_salary": 62576, "date_posted": '2020-05-05'},
    {"max_salary": 94648, "min_salary": 82243, "date_posted": '2020-04-30'},
    {"max_salary": 118794, "min_salary": 81591, "date_posted": '2020-04-28'},
]


def test_sort_by_criteria():
    sort_by(jobs, 'min_salary')
    assert jobs == expected_min_salary

    sort_by(jobs, 'max_salary')
    assert jobs == expected_max_salary

    sort_by(jobs, 'date_posted')
    assert jobs == expected_date_post

    for criteria in invalid_keys:
        with pytest.raises(ValueError,
                           match=f"invalid sorting criteria: {criteria}"):
            sort_by(jobs, criteria)
