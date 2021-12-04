from src.jobs import read


def get_unique_job_types(path):
    unique_types = [
        item["job_type"] for item in read(path) if item["job_type"] != " "
    ]

    # https://pt.stackoverflow.com/questions/192567/removendo-elementos-duplicados-em-uma-lista-com-python
    return sorted(set(unique_types))


def filter_by_job_type(jobs, job_type):
    filtered_jobs = [item for item in jobs if item["job_type"] == job_type]
    return filtered_jobs


def get_unique_industries(path):
    unique_industries = [
        item["industry"] for item in read(path) if item["industry"] != ""
    ]

    # https://pt.stackoverflow.com/questions/192567/removendo-elementos-duplicados-em-uma-lista-com-python
    return sorted(set(unique_industries))


def filter_by_industry(jobs, industry):
    filtered_jobs = [item for item in jobs if item["industry"] == industry]
    return filtered_jobs


def get_max_salary(path):
    salaries = [
        int(item["max_salary"])
        for item in read(path)
        if item["max_salary"] != ""
    ]
    return max(salaries)


def get_min_salary(path):
    salaries = [
        int(item["min_salary"])
        for item in read(path)
        if item["min_salary"] != ""
    ]
    return min(salaries)

print(get_min_salary("src/jobs.csv"))
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
