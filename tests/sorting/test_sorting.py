from src.sorting import sort_by

stub_jobs = [
    {
        "job_title": "Senior Salesforce Developer",
        "min_salary": 44587,
        "max_salary": 82162,
        "date_posted": "2020-05-08",
    },
    {
        "job_title": "ABA Therapist",
        "min_salary": 20000,
        "max_salary": 35000,
        "date_posted": "2020-05-07",
    },
    {
        "job_title": "Principal, Sr. Consultant – Creative Technologist",
        "min_salary": 64829,
        "max_salary": 104769,
        "date_posted": "2020-05-05",
    },
    {
        "job_title": "Doctor of Veterinary Medicine",
        "min_salary": 81991,
        "max_salary": 120117,
        "date_posted": "2020-05-02",
    },
]

senior_dev, aba_therapist, principal_consultant, doctor_veterinary = stub_jobs

result_min_salary_sort = [
    aba_therapist,
    senior_dev,
    principal_consultant,
    doctor_veterinary,
]
result_max_salary_sort = [
    doctor_veterinary,
    principal_consultant,
    senior_dev,
    aba_therapist,
]
result_date_posted_sort = [
    senior_dev,
    aba_therapist,
    principal_consultant,
    doctor_veterinary,
]


def test_sort_by_criteria():
    stub_jobs_copy = stub_jobs.copy()

    sort_by(stub_jobs_copy, "min_salary")
    assert stub_jobs_copy == result_min_salary_sort

    sort_by(stub_jobs_copy, "max_salary")
    assert stub_jobs_copy == result_max_salary_sort

    sort_by(stub_jobs_copy, "date_posted")
    assert stub_jobs_copy == result_date_posted_sort
