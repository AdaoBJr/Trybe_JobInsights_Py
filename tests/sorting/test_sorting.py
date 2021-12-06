from src.sorting import sort_by


# a função sort_by não traz nenhum result. Logo não foi necessário atribuir seu
# resultado a nenhum variável.
jobs = [
    {
        "min_salary": 200,
        "max_salary": 500,
        "date_posted": "2021-12-01",
    },
    {
        "min_salary": 100,
        "max_salary": 300,
        "date_posted": "2021-12-10",
    },
    {
        "min_salary": 700,
        "max_salary": 1000,
        "date_posted": "2021-12-03",
    },
]

min_salary = [
    {
        "min_salary": 100,
        "max_salary": 300,
        "date_posted": "2021-12-10",
    },
    {
        "min_salary": 200,
        "max_salary": 500,
        "date_posted": "2021-12-01",
    },
    {
        "min_salary": 700,
        "max_salary": 1000,
        "date_posted": "2021-12-03",
    },
]

max_salary = [
    {
        "min_salary": 700,
        "max_salary": 1000,
        "date_posted": "2021-12-03",
    },
    {
        "min_salary": 200,
        "max_salary": 500,
        "date_posted": "2021-12-01",
    },
    {
        "min_salary": 100,
        "max_salary": 300,
        "date_posted": "2021-12-10",
    },
]

date_posted = [
    {
        "min_salary": 100,
        "max_salary": 300,
        "date_posted": "2021-12-10",
    },
    {
        "min_salary": 700,
        "max_salary": 1000,
        "date_posted": "2021-12-03",
    },
    {
        "min_salary": 200,
        "max_salary": 500,
        "date_posted": "2021-12-01",
    },
]


def test_sort_by_criteria():
    sort_by(jobs, "min_salary")
    assert jobs == min_salary

    sort_by(jobs, "max_salary")
    assert jobs == max_salary

    sort_by(jobs, "date_posted")
    assert jobs == date_posted
