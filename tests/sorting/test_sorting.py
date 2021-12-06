import pytest
from src.sorting import sort_by
from pytest import fixture

jobs = [
    {
        "min_salary": 10,
        "max_salary": 50,
        "date_posted": "2020-10-01T00:00:00.000Z",
    },
    {
        "min_salary": 20,
        "max_salary": 60,
        "date_posted": "2019-10-01T00:00:00.000Z",
    },
    {
        "min_salary": 30,
        "max_salary": 70,
        "date_posted": "2018-10-01T00:00:00.000Z",
    },
]

valid_criterias = ["min_salary", "max_salary", "date_posted"]

expected_results = [
    [
        {
            "min_salary": 10,
            "max_salary": 50,
            "date_posted": "2020-10-01T00:00:00.000Z",
        },
        {
            "min_salary": 20,
            "max_salary": 60,
            "date_posted": "2019-10-01T00:00:00.000Z",
        },
        {
            "min_salary": 30,
            "max_salary": 70,
            "date_posted": "2018-10-01T00:00:00.000Z",
        },
    ],
    [
        {
            "min_salary": 30,
            "max_salary": 70,
            "date_posted": "2018-10-01T00:00:00.000Z",
        },
        {
            "min_salary": 20,
            "max_salary": 60,
            "date_posted": "2019-10-01T00:00:00.000Z",
        },
        {
            "min_salary": 10,
            "max_salary": 50,
            "date_posted": "2020-10-01T00:00:00.000Z",
        },
    ],
    [
        {
            "min_salary": 30,
            "max_salary": 70,
            "date_posted": "2018-10-01T00:00:00.000Z",
        },
        {
            "min_salary": 20,
            "max_salary": 60,
            "date_posted": "2019-10-01T00:00:00.000Z",
        },
        {
            "min_salary": 10,
            "max_salary": 50,
            "date_posted": "2020-10-01T00:00:00.000Z",
        },
    ],
]


# commit vazio


@fixture
def test_sort_by_criteria():
    with pytest.raises(ValueError):
        sort_by([], "not a valid criteria")
        sort_by("not a valid job", "min_salary")
        sort_by([{"still": "not", "a": "valid", "job": ""}], "max_salary")
    for criteria_index in range(len(valid_criterias)):
        criteria = valid_criterias[criteria_index]
        assert sort_by(jobs, criteria) == expected_results[criteria_index]
