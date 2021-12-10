# import jobs

from src import jobs


def get_unique_job_types(path):
    job_set = set()
    jobs_read = jobs.read(path)
    for job in jobs_read:
        job_set.add(job["job_type"])
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
    return job_set


# print(get_unique_job_types("jobs.csv"))


def filter_by_job_type(jobs, job_type):
    filtered_jobs = [job for job in jobs if job["job_type"] == job_type]
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
    return filtered_jobs


# print(filter_by_job_type("jobs.csv", "fulltime"))


def get_unique_industries(path):
    job_set = set()
    jobs_read = jobs.read(path)
    for job in jobs_read:
        if job["industry"]:
            print(job["industry"])
            job_set.add(job["industry"])
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
    return job_set


# print(get_unique_industries("jobs.csv"))


def filter_by_industry(jobs, industry):
    filtered_jobs = [job for job in jobs if job["industry"] == industry]
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
    return filtered_jobs


def get_max_salary(path):
    job_set = set()
    jobs_read = jobs.read(path)
    for job in jobs_read:
        if job["max_salary"].isnumeric():
            job_set.add(int(job["max_salary"]))
    return max(job_set)
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
    pass


# print(get_max_salary("jobs.csv"))


def get_min_salary(path):
    job_set = set()
    jobs_read = jobs.read(path)
    for job in jobs_read:
        if job["min_salary"].isnumeric():
            job_set.add(int(job["min_salary"]))
    return min(job_set)
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
    try:
        if type(salary) != int:
            raise ValueError("Salary not a number")
        if job["min_salary"] > job["max_salary"]:
            raise ValueError("Error")
        return job["min_salary"] <= salary <= job["max_salary"]
    except Exception:
        raise ValueError("Except valueError")
    pass


# print(matches_salary_range(
#         {"max_salary": 10000, "min_salary": 200},
#         1000
#     ))

# Cristian
def filter_by_salary_range(jobs, salary):
    results = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                results.append(job)
        except ValueError:
            pass
    return results
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
    pass


# print(filter_by_salary_range(
#     [
#             {"max_salary": 0, "min_salary": 10},
#             {"max_salary": 10, "min_salary": 100},
#             {"max_salary": 10000, "min_salary": 200},
#             {"max_salary": 15000, "min_salary": 0},
#             {"max_salary": 1500, "min_salary": 0},
#             {"max_salary": -1, "min_salary": 10},
#     ],
#     [
#         0, 1, 5, 1000, 2000, -1, -2, None, "", [], {}, lambda: 1
#     ]))
