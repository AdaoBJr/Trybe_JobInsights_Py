from src.jobs import read


def get_unique_job_types(path):
    read_file = read(path)
    unique_job_types = []
    for row in read_file:
        if row["job_type"] not in unique_job_types and row["job_type"] != "":
            unique_job_types.append(row["job_type"])

    return unique_job_types


def filter_by_job_type(jobs, job_type):
    job_type_filtered = []
    for row in jobs:
        if row["job_type"] == job_type:
            job_type_filtered.append(row)

    return job_type_filtered


def get_unique_industries(path):
    read_file = read(path)
    unique_industries = []
    for row in read_file:
        if row["industry"] not in unique_industries and row["industry"] != "":
            unique_industries.append(row["industry"])

    return unique_industries


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
    read_file = read(path)
    max_salary = []
    for row in read_file:
        if row["max_salary"] != "" and row["max_salary"].isdigit():
            max_salary.append(int(row["max_salary"]))

    return max(max_salary)


def get_min_salary(path):
    read_file = read(path)
    min_salary = []
    for row in read_file:
        if row["min_salary"] != "" and row["min_salary"].isdigit():
            min_salary.append(int(row["min_salary"]))

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
