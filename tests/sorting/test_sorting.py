from src.sorting import sort_by


jobs = [
    {
        "id": 1,
        "max_salary": 10000,
        "min_salary": 200,
        "date_posted": "2021-11-08"
    },
    {
        "id": 2,
        "max_salary": 15000,
        "min_salary": 2000,
        "date_posted": "2021-11-12"
    },
    {
        "id": 3,
        "max_salary": 3500,
        "min_salary": 1500,
        "date_posted": "2021-11-15"
    },
]

expected_min_salary_asc = [
    {
        "id": 1,
        "max_salary": 10000,
        "min_salary": 200,
        "date_posted": "2021-11-08"
    },
    {
        "id": 3,
        "max_salary": 3500,
        "min_salary": 1500,
        "date_posted": "2021-11-15"
    },
    {
        "id": 2,
        "max_salary": 15000,
        "min_salary": 2000,
        "date_posted": "2021-11-12"
    },
]

expected_max_salary_desc = [
    {
        "id": 2,
        "max_salary": 15000,
        "min_salary": 2000,
        "date_posted": "2021-11-12"
    },
    {
        "id": 1,
        "max_salary": 10000,
        "min_salary": 200,
        "date_posted": "2021-11-08"
        },
    {
        "id": 3,
        "max_salary": 3500,
        "min_salary": 1500,
        "date_posted": "2021-11-15"
    },
]

expected_date_posted_desc = [
    {
        "id": 3,
        "max_salary": 3500,
        "min_salary": 1500,
        "date_posted": "2021-11-15",
    },
    {
        "id": 2,
        "max_salary": 15000,
        "min_salary": 2000,
        "date_posted": "2021-11-12",
    },
    {
        "id": 1,
        "max_salary": 10000,
        "min_salary": 200,
        "date_posted": "2021-11-08",
    },
]


def test_sort_by_criteria():
    criteria_keys = ["date_posted", "max_salary", "min_salary"]

    sort_by(jobs, criteria_keys[2])
    assert expected_min_salary_asc == jobs

    sort_by(jobs, criteria_keys[1])
    assert expected_max_salary_desc == jobs

    sort_by(jobs, criteria_keys[0])
    assert expected_date_posted_desc == jobs
