from src.sorting import sort_by

jobs_mock = [
    {
        "job_title": "job_1",
        "min_salary": 1500,
        "max_salary": 3500,
        "date_posted": "2021-01-01",
    },
    {
        "job_title": "job_2",
        "min_salary": 4500,
        "max_salary": 7500,
        "date_posted": "2021-03-01",
    },
    {
        "job_title": "job_3",
        "min_salary": 8500,
        "max_salary": 9500,
        "date_posted": "2021-06-01",
    },
    {
        "job_title": "job_4",
        "min_salary": 10500,
        "max_salary": 11500,
        "date_posted": "2021-09-01",
    },
    {
        "job_title": "job_5",
        "min_salary": 12500,
        "max_salary": 13500,
        "date_posted": "2021-12-01",
    }
]

jobs_by_date = [
    jobs_mock[4], jobs_mock[3], jobs_mock[2], jobs_mock[1], jobs_mock[0]
]

jobs_by_min_salary = [
    jobs_mock[0], jobs_mock[1], jobs_mock[2], jobs_mock[3], jobs_mock[4]
]

jobs_by_max_salary = [
    jobs_mock[4], jobs_mock[3], jobs_mock[2], jobs_mock[1], jobs_mock[0]
]

criteria_date = "date_posted"
criteria_min = "min_salary"
criteria_max = "max_salary"


def test_sort_by_criteria():
    # test by date
    sort_by(jobs_mock, criteria_date)
    assert jobs_mock == jobs_by_date

    # test by min_salary
    sort_by(jobs_mock, criteria_min)
    assert jobs_mock == jobs_by_min_salary

    # test by max_salary
    sort_by(jobs_mock, criteria_max)
    assert jobs_mock == jobs_by_max_salary
