from src.jobs import read


def get_unique_job_types(path):
    # """Checks all different job types and returns a list of them

    # Must call `read`

    # Parameters
    # ----------
    # path : str
    #     Must be passed to `read`

    # Returns
    # -------
    # list
    #     List of unique job types
    # """
    list = read(path)
    job_type = set()
    for rows in list:
        job_type.add(rows['job_type'])
    return job_type


def filter_by_job_type(jobs, job_type):
    # """Filters a list of jobs by job_type

    # Parameters
    # ----------
    # jobs : list
    #     List of jobs to be filtered
    # job_type : str
    #     Job type for the list filter

    # Returns
    # -------
    # list
    #     List of jobs with provided job_type
    # """
    listOfAllJobs = []
    for job in jobs:
        if (job_type == job["job_type"]):
            listOfAllJobs.append(job)
    return listOfAllJobs


def get_unique_industries(path):
    # """Checks all different industries and returns a list of them

    # Must call `read`

    # Parameters
    # ----------
    # path : str
    #     Must be passed to `read`

    # Returns
    # -------
    # list
    #     List of unique industries
    # """
    list = read(path)
    industries = set()
    for rows in list:
        if rows["industry"] != "":
            industries.add(rows["industry"])
    return industries


def filter_by_industry(jobs, industry):
    # """Filters a list of jobs by industry

    # Parameters
    # ----------
    # jobs : list
    #     List of jobs to be filtered
    # industry : str
    #     Industry for the list filter

    # Returns
    # -------
    # list
    #     List of jobs with provided industry
    # """

    list = []
    for rows in jobs:
        if rows["industry"] == industry:
            list.append(rows)
    return list


def get_max_salary(path):
    # """Get the maximum salary of all jobs

    # Must call `read`

    # Parameters
    # ----------
    # path : str
    #     Must be passed to `read`

    # Returns
    # -------
    # int
    #     The maximum salary paid out of all job opportunities
    # """
    list = read(path)
    max_salary = []
    for rows in list:
        if rows["max_salary"] != "invalid" and rows["max_salary"].isnumeric():
            max_salary.append(int(rows["max_salary"]))
    return max(max_salary)


def get_min_salary(path):
    # """Get the minimum salary of all jobs

    # Must call `read`

    # Parameters
    # ----------
    # path : str
    #     Must be passed to `read`

    # Returns
    # -------
    # int
    #     The minimum salary paid out of all job opportunities
    # """
    list = read(path)
    min_salary = []
    for rows in list:
        if rows["min_salary"] != "invalid" and rows["min_salary"].isnumeric():
            min_salary.append(int(rows["min_salary"]))
    return min(min_salary)


def matches_salary_range(job, salary):
    # Checks if a given salary is in the salary range of a given job

    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) and type(job["max_salary"]) != int
        or type(salary) != int
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError("Error")

    if salary >= job["min_salary"] and salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list.append(job)
        except ValueError:
            print("Salary range error")
    return list
