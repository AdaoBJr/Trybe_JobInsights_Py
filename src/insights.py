# from jobs import read
from src.jobs import read


# fabio

def get_unique_by_column(path, column):
    all_jobs = read(path)
    unique_by_column = set()

    for job in all_jobs:
        if not (job[column] == '' or job[column] == 'invalid'):
            unique_by_column.add(job[column])

    return list(unique_by_column)


def filter_by_column(jobs, filter, column_name):
    return [
        job for job in jobs if filter == job[column_name]
    ]


def get_unique_job_types(path):
    return get_unique_by_column(path, 'job_type')


def filter_by_job_type(jobs, job_type):

    # https://stackoverflow.com/questions/18425225/getting-the-name-of-a-variable-as-a-string
    column_name = f'{job_type=}'.split('=')[0]

    return filter_by_column(jobs, job_type, column_name)


def get_unique_industries(path):
    return get_unique_by_column(path, 'industry')


def filter_by_industry(jobs, industry):
    column_name = f'{industry=}'.split('=')[0]
    return filter_by_column(jobs, industry, column_name)


def get_max_salary(path):
    all_unique_salary = get_unique_by_column(path, 'max_salary')

# https://pt.stackoverflow.com/questions/257905/retornando-somente-o-maior-valor-de-uma-lista-python
    max_salary = max(all_unique_salary, key=int)

    return int(max_salary)


def get_min_salary(path):
    all_unique_salary = get_unique_by_column(path, 'min_salary')

    min_salary = min(all_unique_salary, key=int)

    return int(min_salary)


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


if __name__ == '__main__':
    # print(get_unique_job_types('jobs.csv'))
    print(get_max_salary('jobs.csv'))
