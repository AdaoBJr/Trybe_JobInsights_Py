from src.jobs import read


def get_unique_job_types(path):
    result = read(path)
    job_types = set([row["job_type"] for row in result])
    return [job_type for job_type in job_types]


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    result = read(path)
    unique_industries = set([row["industry"] for row in result])
    return [industry for industry in unique_industries if industry != ""]


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    result = read(path)
    return max(
        [
            int(row["max_salary"])
            for row in result
            if row["max_salary"].isdigit()
        ]
    )


def get_min_salary(path):
    result = read(path)
    return min(
        [
            int(row["min_salary"])
            for row in result
            if row["min_salary"].isdigit()
        ]
    )


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or job["min_salary"] > job["max_salary"]
        or type(salary) != int
    ):
        raise ValueError("Valor inválido")
    return job["min_salary"] < salary < job["max_salary"]


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
