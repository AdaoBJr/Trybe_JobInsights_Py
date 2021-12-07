from src.jobs import read


def get_unique_job_types(path):
    job_list = read(path)
    job_types = set()
    for job in job_list:
        job_types.add(job["job_type"])
    return list(job_types)


def filter_by_job_type(jobs, job_type):
    selected_job = []
    for job in jobs:
        if job["job_type"] == job_type:
            selected_job.append(job)
    return selected_job


def get_unique_industries(path):
    industry_list = read(path)
    unique_industry = set()
    for industry in industry_list:
        if industry["industry"] != "":
            unique_industry.add(industry["industry"])
    return list(unique_industry)


def filter_by_industry(jobs, industry):
    selected_industry = []
    for ind in jobs:
        if ind["industry"] == industry:
            selected_industry.append(ind)
    return selected_industry


def get_max_salary(path):
    max_salary_list = read(path)
    max_salary = []
    for salary in max_salary_list:
        if salary["max_salary"] != "" and salary["max_salary"] != "invalid":
            max_salary.append(int(salary["max_salary"]))
    max_salary.sort()
    return max_salary[len(max_salary) - 1]


def get_min_salary(path):
    min_salary_list = read(path)
    min_salary = []
    for salary in min_salary_list:
        if salary["min_salary"] != "" and salary["min_salary"] != "invalid":
            min_salary.append(int(salary["min_salary"]))
    min_salary.sort()
    return min_salary[0]


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or not isinstance(job["min_salary"], int)
        or not isinstance(job["max_salary"], int)
        or job["min_salary"] > job["max_salary"]
        or not isinstance(salary, int)
    ):
        raise ValueError("Valores inválidos")
    if salary >= job["min_salary"] and salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    filtered_salaries = []
    for job in jobs:
        try:
            isValidJob = matches_salary_range(job, salary)
            if isValidJob:
                filtered_salaries.append(job)
        except ValueError:
            print("Error")
    return filtered_salaries
