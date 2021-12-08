from src.sorting import sort_by


job_list = [
    {'min_salary': 1000, 'max_salary': 5000, 'date_posted': '2008-02-11'},
    {'min_salary': 1100, 'max_salary': 4000, 'date_posted': '2007-01-10'},
    {'min_salary': 900, 'max_salary': 6000, 'date_posted': '2009-03-12'},
]


def test_sort_by_criteria():
    mock_job_list_min_salary = [
        {'min_salary': 900, 'max_salary': 6000, 'date_posted': '2009-03-12'},
        {'min_salary': 1000, 'max_salary': 5000, 'date_posted': '2008-02-11'},
        {'min_salary': 1100, 'max_salary': 4000, 'date_posted': '2007-01-10'},
    ]

    mock_job_list_date_posted = [
        {'min_salary': 900, 'max_salary': 6000, 'date_posted': '2009-03-12'},
        {'min_salary': 1000, 'max_salary': 5000, 'date_posted': '2008-02-11'},
        {'min_salary': 1100, 'max_salary': 4000, 'date_posted': '2007-01-10'},
    ]

    sort_by(job_list, 'min_salary')
    assert job_list == mock_job_list_min_salary

    sort_by(job_list, 'date_posted')
    assert(job_list == mock_job_list_date_posted)
