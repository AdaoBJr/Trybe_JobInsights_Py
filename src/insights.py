from src.jobs import read


def get_unique_job_types(path):
    unique_types = [
        item["job_type"] for item in read(path) if item["job_type"] != " "
    ]

    # https://pt.stackoverflow.com/questions/192567/removendo-elementos-duplicados-em-uma-lista-com-python
    return sorted(set(unique_types))


def filter_by_job_type(jobs, job_type):
    filtered_jobs = [item for item in jobs if item["job_type"] == job_type]
    return filtered_jobs


def get_unique_industries(path):
    unique_industries = [
        item["industry"] for item in read(path) if item["industry"] != ""
    ]

    # https://pt.stackoverflow.com/questions/192567/removendo-elementos-duplicados-em-uma-lista-com-python
    return sorted(set(unique_industries))


def filter_by_industry(jobs, industry):
    filtered_jobs = [item for item in jobs if item["industry"] == industry]
    return filtered_jobs


def get_max_salary(path):
    salaries = [
        int(item["max_salary"])
        for item in read(path)
        if item["max_salary"].isnumeric()
    ]
    return max(salaries)


def get_min_salary(path):
    salaries = [
        int(item["min_salary"])
        for item in read(path)
        if item["min_salary"].isnumeric()
    ]
    return min(salaries)


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) != int
        or type(job["max_salary"]) != int
        or int(job["min_salary"]) > int(job["max_salary"])
    ):
        raise ValueError
    else:
        try:
            if int(job["min_salary"]) <= int(salary) <= int(job["max_salary"]):
                return True
            else:
                return False
        except ValueError as err:
            return err


# print(matches_salary_range({"max_salary": 10000, "min_salary": 200}, 0))


def filter_by_salary_range(jobs, salary):
    if type(salary) == int:
        range_salaries = [
            item
            for item in jobs
            if int(item["min_salary"]) <= salary <= int(item["max_salary"])
        ]
    else:
        range_salaries = []
    return range_salaries
