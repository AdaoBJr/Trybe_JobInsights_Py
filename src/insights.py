from src.jobs import read

def get_unique_job_types(path):
    job_list = read(path)
    job_types = set();
    for job in job_list:
        job_types.add(job["job_type"])
    return list(job_types)

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


def filter_by_job_type(jobs, job_type):
    selected_job = []
    for job in jobs:
        if job["job_type"] == job_type:
            selected_job.append(job)
    return selected_job
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
    industry_list = read(path)
    unique_industry = set();
    for industry in industry_list:
        if industry["industry"] != '':
            unique_industry.add(industry["industry"])
    return list(unique_industry)

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


def filter_by_industry(jobs, industry):
    selected_industry = []
    for ind in jobs:
        if ind["industry"] == industry:
            selected_industry.append(ind)
    return selected_industry
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
    max_salary_list = read(path)
    max_salary = [];
    for salary in max_salary_list:
        if salary["max_salary"] != "" and salary["max_salary"] != "invalid":
            max_salary.append(int(salary["max_salary"]))
    max_salary.sort()
    return max_salary[len(max_salary)-1]
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


def get_min_salary(path):
    min_salary_list = read(path)
    min_salary = [];
    for salary in min_salary_list:
        if salary["min_salary"] != "" and salary["min_salary"] != "invalid":
            min_salary.append(int(salary["min_salary"]))
    min_salary.sort()
    return min_salary[0]
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
    if (
        "min_salary" not in job or
        "max_salary" not in job or
        not isinstance(job["min_salary"], int) or
        not isinstance(job["max_salary"], int) or
        job["min_salary"] > job["max_salary"] or
        not isinstance(salary, int)
    ):
        raise ValueError("Valores inválidos")
    if salary >= job["min_salary"] and salary <= job["max_salary"]:
        return True
    else:
        return False
    



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
    filtered_salaries = []
    for job in jobs:
        try:
            isValidJob = matches_salary_range(job, salary)
            if isValidJob:
                filtered_salaries.append(job)
        except ValueError: 
            print("Error")
    return filtered_salaries
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
