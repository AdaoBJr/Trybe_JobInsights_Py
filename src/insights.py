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
    jobs_list = read(path)
    set_unique_job = set()
    for job in jobs_list:
        if (job['job_type'] != ''):
            set_unique_job.add(job['job_type'])
    return set_unique_job


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
    list_job_match = []
    for job in jobs:
        if (job['job_type'] == job_type):
            list_job_match.append(job)
    return list_job_match


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
    jobs_list = read(path)
    set_unique_industry = set()
    for industry in jobs_list:
        if (industry['industry'] != ''):
            set_unique_industry.add(industry['industry'])
    return set_unique_industry


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
    list_industry_match = []
    for job in jobs:
        if (job['industry'] == industry):
            list_industry_match.append(job)
    return list_industry_match


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
    jobs_list = read(path)
    set_jobs = set()

    for job in jobs_list:
        if job['max_salary'].isdigit():
            salary = int(job['max_salary'])
            set_jobs.add(salary)

    max_salary = max(set_jobs)
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
    jobs_list = read(path)
    set_jobs = set()

    for job in jobs_list:
        if job['min_salary'].isdigit():
            salary = int(job['min_salary'])
            set_jobs.add(salary)

    min_salary = min(set_jobs)
    return min_salary


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
    # print('in_salary_range: ', in_salary_range)
    try:
        min_salary = int(job['min_salary'])
        max_salary = int(job['max_salary'])
        salary_in_range = min_salary <= salary <= max_salary

        if (max_salary < min_salary):
            raise ValueError

        return salary_in_range

    except (ValueError, TypeError, KeyError):
        raise ValueError


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
    jobs_salary_range = []
    for job in jobs:
        try:
            if (matches_salary_range(job, salary)):
                jobs_salary_range.append(job)
        except ValueError:
            pass
    return jobs_salary_range
