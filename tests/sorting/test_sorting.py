from src.sorting import sort_by

jobs = [
    {"min_salary": 700, "max_salary": 3000, "date_posted": "2020-05-10", },
    {"min_salary": 600, "max_salary": 2000, "date_posted": "2020-05-09", },
    {"min_salary": 500, "max_salary": 1000, "date_posted": "2020-05-08", },
]

min_salary = [
    {"min_salary": 1000, "max_salary": 4000, "date_posted": "2020-05-10", },
    {"min_salary": 2000, "max_salary": 5000, "date_posted": "2020-05-09", },
    {"min_salary": 3000, "max_salary": 6000, "date_posted": "2020-05-08", },
]

max_salary = [
    {"min_salary": 3000, "max_salary": 6000, "date_posted": "2020-05-10", },
    {"min_salary": 2000, "max_salary": 5000, "date_posted": "2020-05-09", },
    {"min_salary": 1000, "max_salary": 4000, "date_posted": "2020-05-08", },
]

# da pra fazer isso com sort????


def test_sort_by_criteria():
    assert sort_by(jobs, "min_salary") == min_salary
    assert sort_by(jobs, "max_salary") == max_salary
    assert sort_by(jobs, "date_posted") == jobs
