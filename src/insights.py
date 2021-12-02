from src.jobs import read


def get_unique_job_types(path):
    result = read(path)
    array_jobs = set()
    for item in result:
        array_jobs.add(item['job_type'])
    return list(array_jobs)


def filter_by_job_type(jobs, job_type):
    jobs_list = []
    for item in jobs:
        if (job_type == item["job_type"]):
            jobs_list.append(item)
    return jobs_list


def get_unique_industries(path):

    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    return []


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
    result = read(path)
    max_salary = []
    new_maxsalary = 0
    for item in result:
        if ("max_salary" in item 
        and item["max_salary"] != '' 
        and item["max_salary"] != "invalid"):
            max_salary.append(item)
    for item2 in max_salary:
        if int(item2["max_salary"]) > new_maxsalary:
            new_maxsalary = int(item2["max_salary"])
    return new_maxsalary


def get_min_salary(path):
    result = read(path)
    minimal_salary = []
    new_minsalary = 10000000000
    for item in result:
        if "min_salary" in item and item["min_salary"] != '' and item["min_salary"] != "invalid":
            minimal_salary.append(item)
    for item2 in minimal_salary:
        if int(item2["min_salary"]) < new_minsalary:
            new_minsalary = int(item2["min_salary"])
    return new_minsalary


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
