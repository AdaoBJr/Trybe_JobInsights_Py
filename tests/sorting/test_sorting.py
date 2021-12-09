from src.sorting import sort_by


def test_sort_by_criteria():

    job_1 = {
        "job_title": "backend dev",
        "min_salary": 3000,
        "max_salary": 10000,
        "date_posted": "2021-08-12"
    }

    job_2 = {
        "job_title": "frontend dev",
        "min_salary": 2500,
        "max_salary": 9000,
        "date_posted": "2021-04-03"
    }

    job_3 = {
        "job_title": "java dev",
        "min_salary": 3500,
        "max_salary": 12000,
        "date_posted": "2021-03-08"
    }

    jobs = [job_1, job_2, job_3]

    result_by_min_salary = [job_2, job_1, job_3]
    result_by_max_salary = [job_3, job_1, job_2]
    result_by_date_posted = [job_1, job_2, job_3]

    sort_by(jobs, "min_salary")
    assert jobs == result_by_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == result_by_max_salary

    sort_by(jobs, "date_posted")
    assert jobs == result_by_date_posted
