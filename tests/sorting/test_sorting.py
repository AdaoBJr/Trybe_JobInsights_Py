from src.sorting import sort_by
import pytest


@pytest.fixture()
def jobs():
    return [
        {"max_salary": 10000, "min_salary": 200, "date_posted": "2020-05-02"},
        {"max_salary": 15000, "min_salary": 100, "date_posted": "2021-05-02"},
        {"max_salary": 1500, "min_salary": 0, "date_posted": "2020-10-01"},
        {"max_salary": 2000, "min_salary": 500, "date_posted": ""},
        {"max_salary": "", "min_salary": 600, "date_posted": "2021-04-01"},
        {"max_salary": 2500, "min_salary": "", "date_posted": "2021-02-01"},
    ]


def test_sort_by_criteria(jobs):

    except_sort_by_min_salary = [
        jobs[2],
        jobs[1],
        jobs[0],
        jobs[3],
        jobs[4],
        jobs[5],
    ]

    except_sort_by_max_salary = [
        jobs[1],
        jobs[0],
        jobs[5],
        jobs[3],
        jobs[2],
        jobs[4],
    ]

    except_sort_by_date_posted = [
        jobs[1],
        jobs[4],
        jobs[5],
        jobs[2],
        jobs[0],
        jobs[3],
    ]

    sort_by(jobs, "min_salary")
    assert jobs == except_sort_by_min_salary
    sort_by(jobs, "max_salary")
    assert jobs == except_sort_by_max_salary
    sort_by(jobs, "date_posted")
    assert jobs == except_sort_by_date_posted
