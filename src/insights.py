from src.jobs import read


def get_unique_job_types(path):
    all_jobs = read(path)
    unique_job_types = set()

    for jobs in all_jobs:
        unique_job_types.add(jobs['job_type'])

    return list(unique_job_types)


def filter_by_job_type(jobs, job_type):
    jobs_list = []
    for job in jobs:
        if job['job_type'] == job_type:
            jobs_list.append(job)
    return jobs_list


def get_unique_industries(path):
    all_jobs = read(path)
    job_industry_list = []
    for job in all_jobs:
        if job["industry"] not in job_industry_list and job["industry"] != '':
            job_industry_list.append(job["industry"])

    return job_industry_list


def filter_by_industry(jobs, industry):
    industry_list = []
    for job in jobs:
        if job['industry'] == industry:
            industry_list.append(job)
    return industry_list


def get_max_salary(path):
    all_jobs = read(path)
    max_salary = []
    for job in all_jobs:
        if job["max_salary"] != '' and job["max_salary"] != 'invalid':
            max_salary.append(int(job["max_salary"]))
    return max(max_salary)


def get_min_salary(path):
    all_jobs = read(path)
    min_salary = []
    for job in all_jobs:
        if job["min_salary"] != '' and job["min_salary"] != 'invalid':
            min_salary.append(int(job["min_salary"]))
    return min(min_salary)


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError("no_matches_salary_range")
    if salary >= job["min_salary"] and salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    jobs_by_salary_range = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_by_salary_range.append(job)
        except ValueError:
            pass
    return jobs_by_salary_range


if __name__ == '__main__':
    print(get_unique_job_types('jobs.csv'))
