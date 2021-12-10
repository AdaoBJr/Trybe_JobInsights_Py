from src.sorting import sort_by
from operator import itemgetter

jobs = [
    {
        "max_salary": 10000,
        "min_salary": 1000,
        "date_posted": "2021-01-01",
    },
    {
        "max_salary": 15000,
        "min_salary": 1500,
        "date_posted": "2021-01-02",
    },
    {
        "max_salary": 3500,
        "min_salary": 350,
        "date_posted": "2021-01-03",
    },
]

jobs_by_min_salary = sorted(jobs, key=itemgetter("min_salary"))
jobs_by_max_salary = sorted(jobs, key=itemgetter("max_salary"), reverse=True)
jobs_by_date_posted = sorted(jobs, key=itemgetter("date_posted"), reverse=True)


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == jobs_by_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == jobs_by_max_salary

    sort_by(jobs, "date_posted")
    assert jobs == jobs_by_date_posted
