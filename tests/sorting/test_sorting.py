from src.sorting import sort_by

# job_title,company,state,city,'min_salary','max_salary',job_desc,industry,rating,'date_posted',valid_until,job_type,id

jobs = [
    {
        'min_salary': 4000,
        'max_salary': 9000,
        'date_posted': '01-01-2021',
    },
    {
        'min_salary': 3000,
        'max_salary': 7000,
        'date_posted': '02-01-2021',
    },
    {
        'min_salary': 2000,
        'max_salary': 8000,
        'date_posted': '03-01-2021',
    },
    {
        'min_salary': 7000,
        'max_salary': 14000,
        'date_posted': '04-01-2021',
    },
]


def test_sort_by_criteria():
    sort_by(jobs, 'min_salary')
    assert jobs == [jobs[2], jobs[1], jobs[0], jobs[3]]

    sort_by(jobs, 'max_salary')
    assert jobs == [jobs[1], jobs[2], jobs[0], jobs[3]]

    sort_by(jobs, 'date_posted')
    assert jobs == [jobs[0], jobs[1], jobs[2], jobs[3]]
