# from src.sorting import sort_by
from src.sorting import sort_by

jobs = [
    {
        "min_salary": 1500,
        "max_salary": 15000,
        "date_posted": "2020-11-04"
    },
    {
        "min_salary": 1000,
        "max_salary": 30000,
        "date_posted": "2019-10-03"
    },
    {
        "min_salary": 2000,
        "max_salary": 40000,
        "date_posted": "2021-12-05"
    },
]


def test_sort_by_criteria(): 
    sort_by(jobs, "min_salary")
    print("aaaaaMIN", jobs)
    assert jobs[0] == {
        "min_salary": 1000,
        "max_salary": 30000,
        "date_posted": "2019-10-03"
    }
    assert jobs[1] == {
        "min_salary": 1500,
        "max_salary": 15000,
        "date_posted": "2020-11-04"
    }
    assert jobs[2] == {
        "min_salary": 2000,
        "max_salary": 40000,
        "date_posted": "2021-12-05"
    }
    sort_by(jobs, "max_salary")
    print("aaaaaMAX", jobs)
    assert jobs[0] == {
        "min_salary": 2000,
        "max_salary": 40000,
        "date_posted": "2021-12-05"
    }
    assert jobs[1] == {
        "min_salary": 1000,
        "max_salary": 30000,
        "date_posted": "2019-10-03"
    }
    assert jobs[2] == {
        "min_salary": 1500,
        "max_salary": 15000,
        "date_posted": "2020-11-04"
    }
    sort_by(jobs, "date_posted")
    print("aaaaaDATE", jobs)
    assert jobs[0] == {
        "min_salary": 2000,
        "max_salary": 40000,
        "date_posted": "2021-12-05"
    }
    assert jobs[1] == {
        "min_salary": 1500,
        "max_salary": 15000,
        "date_posted": "2020-11-04"
    }
    assert jobs[2] == {
        "min_salary": 1000,
        "max_salary": 30000,
        "date_posted": "2019-10-03"
    }
