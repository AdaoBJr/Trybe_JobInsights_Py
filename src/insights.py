from src.jobs import read


def get_unique_job_types(path):
    jobs = read(path)
    job_types = []
    for job in jobs:
        if job["job_type"] != "":
            job_types.append(job["job_type"])
        list_jobs = list(dict.fromkeys(job_types))
    return list_jobs


def filter_by_job_type(jobs, job_type):
    type_jpobs = []
    for job in jobs:
        if job["job_type"] == job_type:
            # A função deve retornar uma lista
            # com todos os empregos onde a coluna
            # job_type corresponde ao parâmetro job_type
            type_jpobs.append(job)
    return type_jpobs


def get_unique_industries(path):
    all_jobs = read(path)
    industry = []
    for job in all_jobs:
        if job["industry"] != "":
            industry.append(job["industry"])
    list_industry = list(dict.fromkeys(industry))
    return list_industry


def filter_by_industry(jobs, industry):
    filter_industry = []
    for job in jobs:
        # Loop in param jobs
        if job["industry"] == industry:
            filter_industry.append(job)
    return filter_industry


def get_max_salary(path):
    all_jobs = read(path)
    salary = []
    for job in all_jobs:
        try:
            if job["max_salary"] != "":
                salary.append(int(job["max_salary"]))
        except ValueError:
            print("Error")
# https://www.programiz.com/python-programming/methods/built-in/max
    return max(salary)


def get_min_salary(path):
    all_jobs = read(path)
    salary = []
    for job in all_jobs:
        try:
            if job["min_salary"] != "":
                salary.append(int(job["min_salary"]))
        except ValueError:
            print("Error")
# https://www.datacamp.com/community/tutorials/exception-handling-python?utm_source=adwords_ppc&utm_medium=cpc&utm_campaignid=14989519638&utm_adgroupid=127836677279&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=278443377095&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=1031867&gclid=Cj0KCQiA2NaNBhDvARIsAEw55hg6FdiW_v7WXQmWIuijDxQzfGbSKXRYv3Dd9KIcaMNiPQVzmBRlJYAaAi3rEALw_wcB
# https://www.programiz.com/python-programming/methods/built-in/min
    return min(salary)


def keys_exists(job):
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError


def is_value_int(job, salary):
    # https://www.w3schools.com/python/ref_func_isinstance.asp
    # https://www.datacamp.com/community/tutorials/exception-handling-python?utm_source=adwords_ppc&utm_medium=cpc&utm_campaignid=14989519638&utm_adgroupid=127836677279&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=278443377095&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=1031867&gclid=CjwKCAiA-9uNBhBTEiwAN3IlNCnWbEMCEcYREjDx0Ap423JronJf2EQyXgYasZCqscwTlCa7XUI2sRoCsFAQAvD_BwE
    if not isinstance(salary, int):
        raise ValueError
    if not isinstance(job["max_salary"], int):
        raise ValueError
    if not isinstance(job["min_salary"], int):
        raise ValueError


def matches_salary_range(job, salary):
    keys_exists(job)
    is_value_int(job, salary)
    if job["min_salary"] > job["max_salary"]:
        raise ValueError
    elif salary <= job["max_salary"] and salary >= job["min_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs.append(job)
        except ValueError:
            print("Value error")
    return jobs


""""
def test_salary(jobs, salary):
    add_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                add_jobs.append(job)
        except ValueError:
            print("Value error")
    return add_jobs
"""
