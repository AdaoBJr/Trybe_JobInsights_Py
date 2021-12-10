from src.sorting import sort_by


fake_jobs = [
    {
        "job_title": "System Analyst 1",
        "min_salary": "1000",
        "max_salary": "2000",
        "date_posted": "2001-01-01",
    },
    {
        "job_title": "System Analyst 2",
        "min_salary": "2000",
        "max_salary": "3000",
        "date_posted": "2002-02-02",
    },
    {
        "job_title": "System Analyst 3",
        "min_salary": "3000",
        "max_salary": "4000",
        "date_posted": "2003-03-03",
    },
    {
        "job_title": "System Analyst 4",
        "min_salary": "4000",
        "max_salary": "5000",
        "date_posted": "2004-04-04",
    },
    {
        "job_title": "System Analyst 5",
        "min_salary": "5000",
        "max_salary": "6000",
        "date_posted": "2005-05-05",
    },
    {
        "job_title": "System Analyst 6",
        "min_salary": "6000",
        "max_salary": "7000",
        "date_posted": "2006-06-06",
    }
]


def test_sort_by_criteria():

    '''Verifying if max_salary is working properly'''
    sort_by(fake_jobs, "max_salary")
    assert fake_jobs[0]["max_salary"] == "7000"
    assert fake_jobs[1]["max_salary"] == "6000"
    assert fake_jobs[2]["max_salary"] == "5000"
    assert fake_jobs[3]["max_salary"] == "4000"
    assert fake_jobs[4]["max_salary"] == "3000"
    assert fake_jobs[5]["max_salary"] == "2000"

    '''Verifying if min_salary is working properly'''
    sort_by(fake_jobs, "min_salary")
    assert fake_jobs[0]["min_salary"] == "1000"
    assert fake_jobs[1]["min_salary"] == "2000"
    assert fake_jobs[2]["min_salary"] == "3000"
    assert fake_jobs[3]["min_salary"] == "4000"
    assert fake_jobs[4]["min_salary"] == "5000"
    assert fake_jobs[5]["min_salary"] == "6000"

    '''Verifying if date_posted is working properly'''
    sort_by(fake_jobs, "date_posted")
    assert fake_jobs[0]["date_posted"] == "2006-06-06"
    assert fake_jobs[1]["date_posted"] == "2005-05-05"
    assert fake_jobs[2]["date_posted"] == "2004-04-04"
    assert fake_jobs[3]["date_posted"] == "2003-03-03"
    assert fake_jobs[4]["date_posted"] == "2002-02-02"
    assert fake_jobs[5]["date_posted"] == "2001-01-01"
