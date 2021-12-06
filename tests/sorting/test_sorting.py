from src.sorting import sort_by

jobs = [
    {
        "min_salary": 200,
        "max_salary": 500,
        "date_posted": '2021-12-01',
    },
    {
        "min_salary": 100,
        "max_salary": 300,
        "date_posted": '2021-12-10',
    },
    {
        "min_salary": 700,
        "max_salary": 1000,
        "date_posted": '2021-12-03',
    }
]

asc = [
    {
        "min_salary": 100,
        "max_salary": 300,
        "date_posted": '2021-12-10',
    },
    {
        "min_salary": 200,
        "max_salary": 500,
        "date_posted": '2021-12-01',
    },
    {
        "min_salary": 700,
        "max_salary": 1000,
        "date_posted": '2021-12-03',
    },
]

desc = [
    {
        "min_salary": 700,
        "max_salary": 1000,
        "date_posted": '2021-12-03',
    },
    {
        "min_salary": 200,
        "max_salary": 500,
        "date_posted": '2021-12-01',
    },
    {
        "min_salary": 100,
        "max_salary": 300,
        "date_posted": '2021-12-10',
    },
]

date = [
    {
        "min_salary": 100,
        "max_salary": 300,
        "date_posted": '2021-12-10',
    },
    {
        "min_salary": 700,
        "max_salary": 1000,
        "date_posted": '2021-12-03',
    },
    {
        "min_salary": 200,
        "max_salary": 500,
        "date_posted": '2021-12-01',
    },
]


def test_sort_by_criteria():
    # testa se os valores estão ordenados de forma ascendente
    sort_by(jobs, "max_salary")
    assert jobs == asc
    # testa se os valores estão ordenados de forma descendente
    sort_by(jobs, "min_salary")
    assert jobs == desc
    # testa se os valores estão ordenados por data
    sort_by(jobs, "date_posted")
    assert jobs == date
