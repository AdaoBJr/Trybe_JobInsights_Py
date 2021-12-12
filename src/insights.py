from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    job_types = []
    for job in jobs:
        if job["job_type"] != "":
            job_types.append(job["job_type"])
        list_jobs = list(dict.fromkeys(job_types))
    return list_jobs


def filter_by_job_type(jobs, job_type):
    type_jpobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            # A função deve retornar uma lista
            # com todos os empregos onde a coluna
            # job_type corresponde ao parâmetro job_type
            type_jpobs.append(job)
    return type_jpobs


def get_unique_industries(path):
    all_jobs = read(path)
    industry = []
    for job in all_jobs:
        if job["industry"] != "":
            industry.append(job["industry"])
    list_industry = list(dict.fromkeys(industry))
    return list_industry


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
    all_jobs = read(path)
    salary = []
    for job in all_jobs:
        try:
            if job["max_salary"] != "":
                salary.append(int(job["max_salary"]))
        except ValueError:
            print("Error")
# https://www.programiz.com/python-programming/methods/built-in/max
    return max(salary)


def get_min_salary(path):
    all_jobs = read(path)
    salary = []
    for job in all_jobs:
        try:
            if job["min_salary"] != "":
                salary.append(int(job["min_salary"]))
        except ValueError:
            print("Error")
# https://www.datacamp.com/community/tutorials/exception-handling-python?utm_source=adwords_ppc&utm_medium=cpc&utm_campaignid=14989519638&utm_adgroupid=127836677279&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=278443377095&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=1031867&gclid=Cj0KCQiA2NaNBhDvARIsAEw55hg6FdiW_v7WXQmWIuijDxQzfGbSKXRYv3Dd9KIcaMNiPQVzmBRlJYAaAi3rEALw_wcB
# https://www.programiz.com/python-programming/methods/built-in/min
    return min(salary)


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
