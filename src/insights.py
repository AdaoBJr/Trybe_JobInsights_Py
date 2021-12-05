from src.jobs import read
# from jobs import read


def get_unique_job_types(path):
    job_types = set()
    read_path = read(path)
    for job in read_path:
        job_types.add(job["job_type"])

    return job_types


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
    industries = set()
    read_path = read(path)
    for industry in read_path:
        if industry["industry"] != '':
            industries.add(industry["industry"])

    return industries


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
    read_path = read(path)
    salary_list = []
    for salary in read_path:
        if salary["max_salary"].isnumeric():
            convertInNumber = int(salary["max_salary"], base=10)
            salary_list.append(convertInNumber)

    highest_salary = max(salary_list)
    return highest_salary


def get_min_salary(path):
    read_path = read(path)
    salary_list = []
    for salary in read_path:
        if salary["min_salary"] != '':
            salary_list.append(int(salary["min_salary"]))

    lowest_salary = min(salary_list)
    return lowest_salary


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
