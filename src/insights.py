from src.jobs import read

# from jobs import read


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
        adsadasasd
    """
    unique_job = set()
    jobs = read(path)
    for job in jobs:
        unique_job.add(job["job_type"])
    list_of_jobs = list(unique_job)
    return list_of_jobs


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
    filter_jobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            filter_jobs.append(job)
    return filter_jobs


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
    unique_industry = set()
    jobs = read(path)
    for job in jobs:
        if not job["industry"] == "":
            unique_industry.add(job["industry"])
    list_of_industries = list(unique_industry)
    return list_of_industries


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
    filter_industries = []
    for job in jobs:
        if job["industry"] == industry:
            filter_industries.append(job)
    return filter_industries


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
    max_salary = set()
    jobs = read(path)
    for job in jobs:
        if not (job["max_salary"] == "" or job["max_salary"] == "invalid"):
            max_salary.add(int(job["max_salary"]))
    list_of_salaries = list(max_salary)
    return max(list_of_salaries)


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
    min_salary = set()
    jobs = read(path)
    for job in jobs:
        if not (job["min_salary"] == "" or job["min_salary"] == "invalid"):
            min_salary.add(int(job["min_salary"]))
    list_of_salaries = list(min_salary)
    return min(list_of_salaries)


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
    try:
        if not isinstance(salary, int):
            raise ValueError("salary not interger")
        elif job["min_salary"] > job["max_salary"]:
            raise ValueError("min_salary greater than max_salary")
        elif job["min_salary"] <= salary <= job["max_salary"]:
            return True
        else:
            return False
    except KeyError:
        raise ValueError(
            "job['min_salary'] or job['max_salary'] doesn't exists"
        )
    except TypeError:
        raise ValueError("job['min_salary'] or job['max_salary'] not interger")


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


if __name__ == "__main__":
    # print(get_unique_job_types("jobs.csv"))
    # print(get_unique_industries("jobs.csv"))
    # print(get_max_salary("jobs.csv"))
    invalid_types = [None, "", [], {}, lambda: 1]
    for invalid in invalid_types:
        print(
            matches_salary_range(
                {
                    "min_salary": 0,
                    "max_salary": 1500,
                },
                invalid,
            )
        )
