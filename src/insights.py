from src import jobs
# import jobs


def get_unique_job_types(path):
    jobs_list = jobs.read(path)
    return list(set([job['job_type'] for job in jobs_list]))


# print(get_unique_job_types('src/jobs.csv'))


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job['job_type'] == job_type]


def get_unique_industries(path):
    jobs_list = jobs.read(path)
    industries = set([
        job['industry'] for job in jobs_list if job['industry'] != ''])
    return list(industries)


# print(get_unique_industries('src/jobs.csv'))


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job['industry'] == industry]

# SOURCE https://pt.stackoverflow.com/questions/257905/retornando-
# somente-o-maior-valor-de-uma-lista-python


def get_max_salary(path):
    jobs_list = jobs.read(path)
    salary = set([
        job['max_salary'] for job in jobs_list if job['max_salary'].isdigit()])
    max_salary = max(int(num) for num in salary)
    return max_salary


# print(get_max_salary('src/jobs.csv'))


def get_min_salary(path):
    jobs_list = jobs.read(path)
    salary = set([
        job['min_salary'] for job in jobs_list if job['min_salary'].isdigit()])
    min_salary = min(int(num) for num in salary)
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
