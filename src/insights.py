from src.jobs import read


def get_unique_job_types(path):
    # Using the function made on jobs.py
    file = read(path)
    # Making an array with unique items
    jobs = set()
    # Adds a "job_type" for each item on the jobs array
    for item in file:
        jobs.add(item["job_type"])
    # returns jobs array
    return jobs


def filter_by_job_type(jobs, job_type):
    # Create an array to list the jobs
    job_list = []
    # goes trought the array
    for job in jobs:
        # checking if the job type is in the list of job types
        if job_type == job["job_type"]:
            # adds the job to the list
            job_list.append(job)
    return job_list


def get_unique_industries(path):
    file = read(path)
    industries = set()
    for item in file:
        if item["industry"] != "":
            industries.add(item["industry"])
    return industries
    return []


def filter_by_industry(jobs, industry):
    job_list = []
    for job in jobs:
        if industry == job["industry"]:
            job_list.append(job)
    return job_list


def get_max_salary(path):
    file = read(path)
    max_salary = 0
    # checks if the "max_salary" is a number
    # also checks if it is bigger then "max_salary"
    for item in file:
        if (
            item["max_salary"].isnumeric()
            and int(item["max_salary"]) > max_salary
        ):
            max_salary = int(item["max_salary"])
    return max_salary


def get_min_salary(path):
    file = read(path)
    min_salary = 99999999999
    for item in file:
        if (
            item["min_salary"].isnumeric()
            and int(item["min_salary"]) < min_salary
        ):
            min_salary = int(item["min_salary"])
    return min_salary


def matches_salary_range(job, salary):
    if (
        # check if job has "min_salary" key on it
        "min_salary" not in job
        # check if job has "max_salary" key on it
        or "max_salary" not in job
        # checks if they are int numbers
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
        # checks if "min_salary" is smaller then "max_salary"
        or job["min_salary"] > job["max_salary"]
    ):
        # if any of them checks returns true it will spit an error
        raise ValueError
        # returns true after passing all the others checks
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    filtered_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_salary.append(job)
        except ValueError:
            pass
    return filtered_salary
