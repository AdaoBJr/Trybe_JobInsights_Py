from src.jobs import read


def get_unique_job_types(path):
    all_jobs = read(path)
    job_types = set()
    for jobs in all_jobs:
        job_types.add(jobs['job_type'])
    return job_types


def filter_by_job_type(jobs, job_type):
    job_types = [job for job in jobs if job['job_type'] == job_type]
    return job_types


def get_unique_industries(path):
    all_industry = read(path)
    industrys = set()
    for industry in all_industry:
        if industry != '':
            industrys.add(industry['industry'])
    return industrys


def filter_by_industry(jobs, industry):
    industry_type = [job for job in jobs if job['industry'] == industry]
    return industry_type


def get_max_salary(path):
    all_jobs = read(path)
    job_types = set()
    for jobs in all_jobs:
        salary = jobs['max_salary']
        if salary.isnumeric() and salary != '':
            job_types.add(int(salary))
    return max(job_types)


def get_min_salary(path):
    all_jobs = read(path)
    job_types = set()
    for jobs in all_jobs:
        salary = jobs['min_salary']
        if salary.isnumeric() and salary != '':
            job_types.add(int(salary))
    return min(job_types)


def matches_salary_range(job, salary):
    try:
        if type(salary) != int:
            raise ValueError("Salary deve ser um inteiro")

        if job["min_salary"] > job["max_salary"]:
            raise ValueError(
                "Salario minimo deve ser menor que salario máximo"
            )
        return job["min_salary"] <= salary <= job["max_salary"]
    except Exception:
        raise ValueError("Salary deve ser um inteiro")


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
