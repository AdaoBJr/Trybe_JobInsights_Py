from src.jobs import read


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
    jobs = read(path)

    job_types = set()

    # Source: https://app.betrybe.com/course/computer-science/
    # introducao-a-python/aprendendo-python/9c4e1d64-303d-
    # 492d-82a4-998b2c0218b9/conteudos/217980af-0946-4b04-9cc4
    # -5846af26ec27/estruturas-de-repeticao/e672a406-93bf
    # -4bbe-b95d-4eedff2f5723?use_case=side_bar
    for job in jobs:
        job_types.add(job["job_type"])

    # Source: https://www.geeksforgeeks.org/python-convert-set-into-a-list/
    return list(job_types)


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
    return []


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
    jobs = read(path)

    industries = set()

    for job in jobs:
        if job["industry"] != "":
            industries.add(job["industry"])

    return list(industries)


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
    jobs = read(path)

    salaries = set()

    for job in jobs:
        # Source: www.programiz.com/python-programming/methods/string/isnumeric
        if job["max_salary"].isnumeric():
            salaries.add(int(job["max_salary"]))

    # Source: www.tutorialspoint.com/python/list_max.htm
    return max(salaries)


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
    pass


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
    get_unique_job_types("src/jobs.csv")
