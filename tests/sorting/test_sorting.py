from src.sorting import sort_by


def test_sort_by_criteria():
    # job data imported from here
    # https://github1s.com/tryber/sd-09-project-job-insights/pull/1
    job_1 = {
        "job_name": "Diesel Mechanic",
        "min_salary": 46298,
        "max_salary": 55893,
        "date_posted": "2021-09-09",
    }

    job_2 = {
        "job_name": "Ultrasound Technologist",
        "min_salary": 55069,
        "max_salary": 74745,
        "date_posted": "2021-02-02",
    }
    job_3 = {
        "job_name": "ABA Therapist",
        "min_salary": 20000,
        "max_salary": 35000,
        "date_posted": "2021-04-17",
    }

    jobs = [job_1, job_3, job_2]

    criteria_keys = ["min_salary", "max_salary", "date_posted"]

    criteria_results = [
        [job_3, job_1, job_2],
        [job_2, job_1, job_3],
        [job_1, job_3, job_2],
    ]

    # with pytest.raises(
    #     KeyError, match=f"invalid sorting criteria: {invalid_criteria_key}"
    # ):
    #     sort_by(jobs, invalid_criteria_key)

    for index, criteria_key in enumerate(criteria_keys):
        sort_by(jobs, criteria_key)
        assert (jobs == criteria_results[index]) is True
