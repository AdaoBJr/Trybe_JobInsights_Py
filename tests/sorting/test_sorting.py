# import pytest
from src.sorting import sort_by

jobs = [
    {
        "min_salary": 10,
        "max_salary": 50,
        "date_posted": "2020-10-01",
    },
    {
        "min_salary": 20,
        "max_salary": 60,
        "date_posted": "2018-10-01",
    },
    {
        "min_salary": 30,
        "max_salary": 70,
        "date_posted": "2019-10-01",
    },
]

valid_criterias = ["min_salary", "max_salary", "date_posted"]

expected_results = [
    [
        {
            "min_salary": 10,
            "max_salary": 50,
            "date_posted": "2020-10-01",
        },
        {
            "min_salary": 20,
            "max_salary": 60,
            "date_posted": "2019-10-01",
        },
        {
            "min_salary": 30,
            "max_salary": 70,
            "date_posted": "2018-10-01",
        },
    ],
    [
        {
            "min_salary": 30,
            "max_salary": 70,
            "date_posted": "2018-10-01",
        },
        {
            "min_salary": 20,
            "max_salary": 60,
            "date_posted": "2019-10-01",
        },
        {
            "min_salary": 10,
            "max_salary": 50,
            "date_posted": "2020-10-01",
        },
    ],
    [
        {
            "min_salary": 10,
            "max_salary": 50,
            "date_posted": "2020-10-01",
        },
        {
            "min_salary": 30,
            "max_salary": 70,
            "date_posted": "2019-10-01",
        },
        {
            "min_salary": 20,
            "max_salary": 60,
            "date_posted": "2018-10-01",
        },
    ],
]


# commit vazio


def test_sort_by_criteria():
    for criteria_index in range(len(valid_criterias)):
        criteria = valid_criterias[criteria_index]
        assert sort_by(jobs, criteria) == expected_results[criteria_index]
