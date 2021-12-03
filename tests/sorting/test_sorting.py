from src.sorting import sort_by
from src.jobs import read
from src.insights import get_min_salary


def test_sort_by_criteria():
    jobs = read('src/jobs.csv')
    criteria = "min_salary"

    sort_by(jobs, criteria)
    min_salary_jobs_sorted = jobs[0][criteria]

    assert type(jobs) is list
    assert min_salary_jobs_sorted == str(get_min_salary('src/jobs.csv'))
