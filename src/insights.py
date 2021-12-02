# from jobs import read
from src.jobs import read


def get_unique_by_column(path, column):
    all_jobs = read(path)
    unique_by_column = set()

    for job in all_jobs:
        if not (job[column] == "" or job[column] == "invalid"):
            unique_by_column.add(job[column])

    return list(unique_by_column)


def filter_by_column(jobs, filter, column_name):
    return [job for job in jobs if filter == job[column_name]]


def analizer_all_salary(job, salary):
    if not ("min_salary" in job.keys() and "max_salary" in job.keys()):
        return {"message": "not found key in job"}

    if not (
        isinstance(salary, int)
        and isinstance(job["min_salary"], int)
        and isinstance(job["max_salary"], int)
    ):
        return {"message": "isn't a valid integer"}

    if job["max_salary"] < job["min_salary"]:
        return {"message": "max_salary less than min_salary"}

    return {}

# -------------------------------------------------------------------------------------------


def get_unique_job_types(path):
    return get_unique_by_column(path, "job_type")


def filter_by_job_type(jobs, job_type):

    # https://stackoverflow.com/questions/18425225/getting-the-name-of-a-variable-as-a-string
    column_name = f"{job_type=}".split("=")[0]

    return filter_by_column(jobs, job_type, column_name)


def get_unique_industries(path):
    return get_unique_by_column(path, "industry")


def filter_by_industry(jobs, industry):
    column_name = f"{industry=}".split("=")[0]
    return filter_by_column(jobs, industry, column_name)


def get_max_salary(path):
    all_unique_salary = get_unique_by_column(path, "max_salary")

    # https://pt.stackoverflow.com/questions/257905/retornando-somente-o-maior-valor-de-uma-lista-python
    max_salary = max(all_unique_salary, key=int)

    return int(max_salary)


def get_min_salary(path):
    all_unique_salary = get_unique_by_column(path, "min_salary")

    min_salary = min(all_unique_salary, key=int)

    return int(min_salary)


def matches_salary_range(job, salary):
    result = analizer_all_salary(job, salary)

    if "message" in result.keys():
        raise ValueError(result["message"])

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    jobs_filtreds = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_filtreds.append(job)
        except ValueError:
            pass
    return jobs_filtreds


if __name__ == "__main__":
    # print(get_unique_job_types('jobs.csv'))
    # print(get_max_salary('jobs.csv'))
    print(matches_salary_range({"min_salary": 0, "max_salary": 100}, 50))
