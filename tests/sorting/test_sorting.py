from src.sorting import sort_by


def test_sort_by_criteria():
    critery = ['min_salary', 'max_salary', 'date_posted']
    jobs = [{"max_salary": 10000, "min_salary": 200, 'date_posted': '03-10-2019'}, {"max_salary": 1500, "min_salary": 0, 'date_posted': '02-10-2019'}]

    jobs_min_salary = [{"max_salary": 1500, "min_salary": 0, 'date_posted': '02-10-2019'}, {"max_salary": 10000, "min_salary": 200, 'date_posted': '03-10-2019'}]
    jobs_max_salary = [{"max_salary": 10000, "min_salary": 200, 'date_posted': '03-10-2019'}, {"max_salary": 1500, "min_salary": 0, 'date_posted': '02-10-2019'}]
    jobs_date_posted = [{"max_salary": 10000, "min_salary": 200, 'date_posted': '03-10-2019'}, {"max_salary": 1500, "min_salary": 0, 'date_posted': '02-10-2019'}]

    assert sort_by(jobs, critery[0]) == jobs_min_salary
    assert sort_by(jobs, critery[1]) == jobs_max_salary
    assert sort_by(jobs, critery[2]) == jobs_date_posted
