from src.sorting import sort_by
jobs = [
    {
        "min_salary": 800,
        "max_salary": 1000,
        "date_posted": "2022-05-08",
    },
    {
        "min_salary": 500,
        "max_salary": 800,
        "date_posted": "2022-05-10",
    },
    {
        "min_salary": 200,
        "max_salary": 1200,
        "date_posted": "2022-05-05",
    },
]

result_min_salary_sort = [
    jobs[0],
    jobs[1],
    jobs[2],
]
result_max_salary_sort = [
    jobs[2],
    jobs[0],
    jobs[1],
]
result_date_posted_sort = [
    jobs[1],
    jobs[0],
    jobs[2],
]


def test_sort_by_criteria():
    # sort_by(jobs, "min_salary")
    # assert jobs == result_min_salary_sort

    sort_by(jobs, "max_salary")
    assert jobs == result_max_salary_sort

    # sort_by(jobs, "date_posted")
    # assert jobs == result_date_posted_sort
