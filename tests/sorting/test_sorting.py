from src.sorting import sort_by

jobs = [
    {
        'job_title': 'Data Engineer with Security Clearance',
        'company': 'Booz Allen Hamilton',
        'state': 'VA',
        'city': 'Arlington',
        'min_salary': '78824',
        'max_salary': '152227',
        'industry': 'Business Services',
        'rating': '3.7',
        'date_posted': '2020-05-02',
        'valid_until': '2020-06-06',
        'job_type': 'FULL_TIME',
        'id': '3320',
    },
    {
        'job_title': 'Data Engineer, Mid with Security Clearance',
        'company': 'Booz Allen Hamilton',
        'state': 'VA',
        'city': 'Herndon',
        'min_salary': '58824',
        'max_salary': '112227',
        'industry': 'Business Services',
        'rating': '3.7',
        'date_posted': '2020-05-07',
        'valid_until': '2020-06-06',
        'job_type': 'FULL_TIME',
        'id': '3321',
    },
    {
        'job_title': 'Data Modeler, Senior with Security Clearance',
        'company': 'Booz Allen Hamilton',
        'state': 'VA',
        'city': 'Springfield',
        'min_salary': '90454',
        'max_salary': '151998',
        'industry': 'Business Services',
        'rating': '3.7',
        'date_posted': '2020-04-28',
        'valid_until': '2020-06-06',
        'job_type': 'FULL_TIME',
        'id': '3322',
    },
    {
        'job_title': 'Data Engineer, Senior with Security Clearance',
        'company': 'Booz Allen Hamilton',
        'state': 'VA',
        'city': 'Herndon',
        'min_salary': '91443',
        'max_salary': '155868',
        'industry': 'Business Services',
        'rating': '3.7',
        'date_posted': '2020-06-02',
        'valid_until': '2020-06-06',
        'job_type': 'FULL_TIME',
        'id': '3323',
    },
]

def test_sort_by_criteria():
    sort_by(jobs, "date_posted")
    assert jobs == [jobs[3], jobs[1], jobs[0], jobs[2]]

    sort_by(jobs, "min_salary")
    assert jobs == [jobs[1], jobs[0], jobs[2], jobs[3]]

    sort_by(jobs, "max_salary")
    assert jobs == [jobs[3], jobs[0], jobs[2], jobs[1]]
