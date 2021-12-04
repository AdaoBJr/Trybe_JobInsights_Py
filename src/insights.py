from src.jobs import read


def get_unique_job_types(path):
    dict_from_jobs = read(path)
    jobs_types = set()
    for job in dict_from_jobs:
        jobs_types.add(job["job_type"])
    return jobs_types


def filter_by_job_type(jobs, job_type):
    filter_job_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            filter_job_type.append(job)
    return filter_job_type


def get_unique_industries(path):
    dict_from_jobs = read(path)
    list_of_industries = set()
    for industry in dict_from_jobs:
        if industry["industry"]:
            list_of_industries.add(industry["industry"])
    return list_of_industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


def get_max_salary(path):
    dict_from_jobs = read(path)
    max_salary = 0
    for job in dict_from_jobs:
        if(
            job["max_salary"].isnumeric()
            and int(job["max_salary"]) > max_salary
        ):
            max_salary = int(job["max_salary"])
    return max_salary


def get_min_salary(path):
    dict_from_jobs = read(path)
    min_salary = []
    for job in dict_from_jobs:
        if job["min_salary"] != "" and job["min_salary"] != "invalid":
            min_salary.append(int(job["min_salary"]))
    return min(min_salary)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []


if __name__ == "__main__":
    print(get_unique_job_types("src/jobs.csv"))
    print(get_min_salary("src/jobs.csv"))
