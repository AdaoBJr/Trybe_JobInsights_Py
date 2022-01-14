from src.sorting import sort_by
from pytest import fixture


@fixture
def jobs():
    return [
        {"max_salary": 100, "min_salary": 90, "date_posted": "2020-05-12"},
        {"max_salary": 1500, "min_salary": 1000, "date_posted": "2019-01-02"},
        {"max_salary": 500, "min_salary": 400, "date_posted": "2009-02-16"},
        {
            "max_salary": 12000,
            "min_salary": 10000,
            "date_posted": "2021-08-15",
        },
    ]


def test_sort_by_criteria(jobs):
    jobs_unordered = [*jobs]
    sort_by(jobs, "min_salary")
    assert jobs == sorted(
        jobs_unordered, key=lambda value: value["min_salary"]
    )

    sort_by(jobs, "max_salary")
    assert jobs == sorted(
        jobs_unordered, key=lambda value: value["max_salary"], reverse=True
    )

    sort_by(jobs, "date_posted")
    assert jobs == sorted(
        jobs_unordered, key=lambda value: value["date_posted"], reverse=True
    )
