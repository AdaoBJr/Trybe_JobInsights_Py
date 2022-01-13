from src.sorting import sort_by

job_list = [
        {
            "min_salary": 10,
            "max_salary": 100,
            "date_posted": "14-02-1997"
        },
        {
            "min_salary": 1000,
            "max_salary": 999999,
            "date_posted": "22-11-2004"
        },
        {
            "min_salary": 100,
            "max_salary": 1000,
            "date_posted": "02-06-2007"
        },
    ]

max_salary_sort = [
        {
            "min_salary": 1000,
            "max_salary": 999999,
            "date_posted": "22-11-2004"
        },
        {
            "min_salary": 100,
            "max_salary": 1000,
            "date_posted": "02-06-2007"
        },
        {
            "min_salary": 10,
            "max_salary": 100,
            "date_posted": "14-02-1997"
        }
    ]


def test_sort_by_criteria():

    new_job_list = job_list
    sort_by(new_job_list, "max_salary")

    assert new_job_list == max_salary_sort
