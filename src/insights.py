from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    out = [job["job_type"] for job in jobs]
    return set(out)


def filter_by_job_type(jobs, job_type):
    out = [job for job in jobs if job["job_type"] == job_type]
    return out


def get_unique_industries(path):
    jobs = read(path)
    out = [job["industry"] for job in jobs if job["industry"] != ""]
    return set(out)


def filter_by_industry(jobs, industry):
    out = [job for job in jobs if (job["industry"] == industry)]
    return out


def get_max_salary(path):
    csvJobs = read(path)
    out = [
        int(job["max_salary"])
        for job in csvJobs
        if job["max_salary"].isnumeric()
    ]
    return max(out)


def get_min_salary(path):
    csvJobs = read(path)
    out = [
        int(job["min_salary"])
        for job in csvJobs
        if job["min_salary"].isnumeric()
    ]
    return min(out)


def matches_salary_range(job, salary):

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError

    max_salary = job["max_salary"]
    min_salary = job["min_salary"]
    
    if type(min_salary) != int or type(max_salary) != int:
        raise ValueError
    elif min_salary > max_salary:
        raise ValueError
    elif not type(salary) == int:
        raise ValueError

    if min_salary <= salary and max_salary >= salary:
        return True
    return False


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
