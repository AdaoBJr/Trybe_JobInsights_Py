from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    jobs_array = set()
    for job in jobs_list:
        jobs_array.add(job["job_type"])

    return jobs_array


def filter_by_job_type(jobs, job_type):
    jobs_types_array = [
            job for job in jobs
            if job["job_type"] == job_type
            ]
    return jobs_types_array


def get_unique_industries(path):
    jobs_list = read(path)
    indrustries_array = set()
    for industries in jobs_list:
        indrustries_array.add(industries["industry"])
# https://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings
    indrustries_array = list(filter(None, indrustries_array))
    return indrustries_array


def filter_by_industry(jobs, industry):
    industry_array = [
            job for job in jobs
            if job["industry"] == industry
            ]
    return industry_array


def get_max_salary(path):
    jobs_list = read(path)
    max_salary_array = set()
    for salary in jobs_list:
        if salary["max_salary"] != '' and salary["max_salary"].isnumeric():
            max_salary_array.add(int(salary["max_salary"]))
    return max(max_salary_array)


def get_min_salary(path):
    jobs_list = read(path)
    min_salary_array = set()
    for salary in jobs_list:
        if salary["min_salary"] != '' and salary["min_salary"].isnumeric():
            min_salary_array.add(int(salary["min_salary"]))
    return min(min_salary_array)


def matches_salary_range(job, salary):
    try:
        if type(salary) != int:
            raise ValueError("Salário não é um número inteiro")
        if job["min_salary"] > job["max_salary"]:
            raise ValueError("Salário min não pode ser maior que Salário máx")
        return job["min_salary"] <= salary <= job["max_salary"]
    except Exception:
        raise ValueError("Salário não é um número inteiro")


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
