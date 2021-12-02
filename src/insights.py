from src.jobs import read


def get_unique_job_types(path):
    result = read(path)
    array_jobs = set()
    for item in result:
        array_jobs.add(item['job_type'])
    return list(array_jobs)


def filter_by_job_type(jobs, job_type):
    jobs_list = []
    for item in jobs:
        if (job_type == item["job_type"]):
            jobs_list.append(item)
    return jobs_list


def get_unique_industries(path):
    result = read(path)
    ind = set()
    for item in result:
        if item["industry"]:
            ind.add(item["industry"])
    return ind


def filter_by_industry(jobs, industry):
    filter_industries = []
    industries = []
    for item in jobs:
        if(
            "industry" in item
            and item["industry"] != ''
            and item["industry"] != "invalid"
        ):
            filter_industries.append(item)

    for item in filter_industries:
        if item["industry"] == industry:
            industries.append(item)
    return industries


def get_max_salary(path):
    result = read(path)
    max_salary = []
    new_maxsalary = 0
    for item in result:
        if (
            "max_salary" in item
            and item["max_salary"] != ''
            and item["max_salary"] != "invalid"
        ):
            max_salary.append(item)
    for item2 in max_salary:
        if int(item2["max_salary"]) > new_maxsalary:
            new_maxsalary = int(item2["max_salary"])
    return new_maxsalary


def get_min_salary(path):
    result = read(path)
    minimal_salary = []
    new_minsalary = 10000000000
    for item in result:
        if (
            "min_salary" in item
            and item["min_salary"] != ''
            and item["min_salary"] != "invalid"
        ):
            minimal_salary.append(item)
    for item2 in minimal_salary:
        if int(item2["min_salary"]) < new_minsalary:
            new_minsalary = int(item2["min_salary"])
    return new_minsalary


def matches_salary_range(job, salary):
        if (
            "min_salary" not in job
            or "max_salary" not in job
            or not isinstance(job["min_salary"], int) # um typeof do python
            or not isinstance(job["max_salary"], int)
            or job["min_salary"] > job["max_salary"]
            or not isinstance(salary, int)
        ):
            raise ValueError("Um ou vários inputs estão errados")

        if job["min_salary"] <= salary <= job["max_salary"]:
            return True
        else:
            return False
#agradecimentos ao rafael gumieri


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
