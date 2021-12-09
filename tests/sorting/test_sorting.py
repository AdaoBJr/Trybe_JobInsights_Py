from src.sorting import sort_by

list_jobs = [
    {"date_posted": "2019-01-06", "max_salary": 4500, "min_salary": 1500},
    {"date_posted": "2020-01-06", "max_salary": 5500, "min_salary": 2500},
    {"date_posted": "2021-01-06", "max_salary": 6500, "min_salary": 3500},
]

list_salary_min = [
   list_jobs[0],
   list_jobs[1],
   list_jobs[2]
]

list_salary_max = [
   list_jobs[2],
   list_jobs[1],
   list_jobs[0]
]

list_date = [
   list_jobs[2],
   list_jobs[1],
   list_jobs[0]
]


def test_sort_by_criteria():
    sort_by(list_jobs, "max_salary")
    assert list_jobs == list_salary_max

    sort_by(list_jobs, "min_salary")
    assert list_jobs == list_salary_min

    sort_by(list_jobs, "date_posted")
    assert list_jobs == list_date
