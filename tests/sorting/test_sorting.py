from src.sorting import sort_by

jobs = [
    {"date_posted": "2021-05-01", "max_salary": 0, "min_salary": 500},
    {"date_posted": "2021-05-02", "max_salary": 500, "min_salary": 0},
    {"date_posted": "2021-05-03", "max_salary": 7000, "min_salary": 2000},
    {"date_posted": "2021-05-04", "max_salary": 1000, "min_salary": 2500},
    {"date_posted": "2021-05-05", "max_salary": 5, "min_salary": 10},
]
maxSalaryLista = [
    jobs[2],
    jobs[3],
    jobs[1],
    jobs[4],
    jobs[0],
]
minSalaryLista = [
    jobs[1],
    jobs[4],
    jobs[0],
    jobs[2],
    jobs[3],
]

dateLista = [
    jobs[4],
    jobs[3],
    jobs[2],
    jobs[1],
    jobs[0],
]


def test_sort_by_criteria():

    sort_by(jobs, "max_salary")
    assert jobs == maxSalaryLista

    sort_by(jobs, "min_salary")
    assert jobs == minSalaryLista

    sort_by(jobs, "date_posted")
    assert jobs == dateLista
