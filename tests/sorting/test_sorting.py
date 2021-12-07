from src.sorting import sort_by

jobs = [
    {"min_salary": 2500, "max_salary": 5000, "date_posted": "2021-12-07"},
    {"min_salary": 2000, "max_salary": 5500, "date_posted": "2021-12-06"},
    {"min_salary": 3000, "max_salary": 6000, "date_posted": "2021-12-08"},
]

jobs_sorted_by_min_salary = [
    jobs[1],
    jobs[0],
    jobs[2],
]

jobs_sorted_by_max_salary = [
    jobs[2],
    jobs[1],
    jobs[0],
]

jobs_sorted_by_date_posted = [
    jobs[2],
    jobs[0],
    jobs[1],
]


def test_sort_by_criteria():
    assert sort_by(jobs, "min_salary") == jobs_sorted_by_min_salary
    assert sort_by(jobs, "max_salary") == jobs_sorted_by_max_salary
    assert sort_by(jobs, "date_posted") == jobs_sorted_by_date_posted
