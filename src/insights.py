from .jobs import read


def filterBy(column, jobs, searchParam):
    return filter(lambda val: val[column] == searchParam, jobs)


def get_unique_job_types(path):
    JOB_TYPE = "job_type"

    tmp = read(path)
    unique_jobs = set()

    for dic in tmp:
        unique_jobs.add(dic[JOB_TYPE])

    return list(unique_jobs)


def filter_by_job_type(jobs, job_type):
    JOB_TYPE = "job_type"
    filteredObj = filterBy(JOB_TYPE, jobs, job_type)
    return list(filteredObj)


def get_unique_industries(path):
    INDUSTRY_COLUMN = "industry"

    tmp = read(path)
    unique_industries = set()

    for dic in tmp:
        if dic[INDUSTRY_COLUMN]:
            unique_industries.add(dic[INDUSTRY_COLUMN])

    return list(unique_industries)


def filter_by_industry(jobs, industry):
    INDUSTRY = "industry"
    filteredObj = filterBy(INDUSTRY, jobs, industry)
    return list(filteredObj)


def get_max_salary(path):
    MAX_SALARY_COLUMN = "max_salary"
    tmp = read(path)
    highest_salary = float("-inf")
    for dic in tmp:
        try:
            current_iterated_salary = int(dic[MAX_SALARY_COLUMN])
            if current_iterated_salary > highest_salary:
                highest_salary = current_iterated_salary

        except Exception:
            highest_salary = highest_salary

    return highest_salary


def get_min_salary(path):
    MIN_SALARY_COLUMN = "min_salary"
    tmp = read(path)
    minimum_salary = float("inf")
    for dic in tmp:
        try:
            current_iterated_salary = int(dic[MIN_SALARY_COLUMN])
            if current_iterated_salary < minimum_salary:
                minimum_salary = current_iterated_salary

        except Exception:
            minimum_salary = minimum_salary

    return minimum_salary


def checkSalaryType(job, salary):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError()
    if (
        type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or type(salary) != int
    ):
        raise ValueError()


def matches_salary_range(job, salary):
    checkSalaryType(job, salary)
    MINIMUM_SALARY = "min_salary"
    MAXIMUM_SALARY = "max_salary"

    job_minimum = int(job[MINIMUM_SALARY])
    job_maximum = int(job[MAXIMUM_SALARY])
    salary = int(salary)
    if job_minimum > job_maximum:
        raise ValueError()

    if salary >= job_minimum and salary <= job_maximum:
        return True
    else:
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


if __name__ == "__main__":
    PATH = "src/jobs.csv"
    # print(get_unique_job_types(PATH))
    # print(get_unique_industries(PATH))
    # print(get_max_salary(PATH))
    # print(get_min_salary(PATH))
    # print(filter_by_job_type(read(PATH), "FULL_TIME"))
    # print(matches_salary_range({"max_salary": 1500, "min_salary": 0}, 0))
