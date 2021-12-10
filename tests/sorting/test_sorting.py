from src.sorting import sort_by


jobs = [
    {
        'min_salary': 1500,
        'max_salary': 4500,
        'date_posted': '2021-08-09',
    },
    {
        'min_salary': 2000,
        'max_salary': 10000,
        'date_posted': '2021-02-11',
    },
    {
        'min_salary': 0,
        'max_salary': 2000,
        'date_posted': '2021-07-01',
    }
]


set_min_salary = [
    {
        'min_salary': 0,
        'max_salary': 2000,
        'date_posted': '2021-08-09',
    },
    {
        'min_salary': 1500,
        'max_salary': 4500,
        'date_posted': '2021-07-01',
    },
    {
        'min_salary': 2000,
        'max_salary': 10000,
        'date_posted': '2021-02-11',
    },
]


set_max_salary = [
    {
        'min_salary': 2000,
        'max_salary': 10000,
        'date_posted': '2021-02-11',
    },
    {
        'min_salary': 1500,
        'max_salary': 4500,
        'date_posted': '2021-07-01',
    },
    {
        'min_salary': 0,
        'max_salary': 2000,
        'date_posted': '2021-08-09',
    }
]


ordered_by_date_posted = [
    {
        'min_salary': 2000,
        'max_salary': 10000,
        'date_posted': '2021-02-11',
    },
    {
        'min_salary': 1500,
        'max_salary': 4500,
        'date_posted': '2021-07-01',
    },
    {
        'min_salary': 0,
        'max_salary': 2000,
        'date_posted': '2021-08-09',
    },
]


def test_sort_by_criteria():
    pass
    min_salary = "min_salary"
    sort_by(jobs, min_salary)
    assert jobs == set_min_salary

    max_salary = "max_salary"
    sort_by(jobs, max_salary)
    assert jobs == set_max_salary
