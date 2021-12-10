from src import jobs
import csv


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    job_csv = jobs.read(path)
    job_type_list = set()
    for job in job_csv:
        job_type_list.add(job["job_type"])
    return sorted(job_type_list)


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    result_jobs = []
    for value in jobs:
        if(value["job_type"] == job_type):
            result_jobs.append(value)
    return result_jobs


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
    result_industries = []
    with open(path) as file:
        data_csv = csv.DictReader(file, delimiter=",", quotechar='"')
        for value in data_csv:
            if(value["industry"] != ""):
                result_industries.append(value["industry"])
    result_set = set(result_industries)
    return list(result_set)


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
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    job_csv = jobs.read(path)
    max_salary = 0
    for job in job_csv:
        if (
            job["max_salary"].isnumeric() and
            int(job["max_salary"]) > max_salary
        ):
            max_salary = int(float(job["max_salary"]))
    return max_salary


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    job_csv = jobs.read(path)
    min_salary = []
    for job in job_csv:
        if (
            job["min_salary"] != "" and
            job["min_salary"].isnumeric()
        ):
            min_salary.append(int(job["min_salary"]))

    return min(min_salary)


def matches_salary_range(job, salary):
    """Checks if if a given salary is in the salary range of a given job

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
    try:
        if type(salary) != int:
            raise ValueError("salary not int")
        if job["min_salary"] > job["max_salary"]:
            raise ValueError("Salary min not maior que salry máx")
        return job["min_salary"] <= salary <= job["max_salary"]
    except Exception:
        raise ValueError("Salary not int")


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
    filter_by_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job,salary):
                filter_by_salary.append(job)
        except ValueError:
            pass
    return filter_by_salary
