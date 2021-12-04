from src.jobs import read


def get_unique_job_types(path):
    all_jobs = read(path)
    # pq não funciona?
    # print(set(job['job_type'] for job in all_jobs))
    # console.append(job['job_type'] for job in all_jobs)
    console = set()
    for job in all_jobs:
        console.add(job["job_type"])
    return console


def filter_by_job_type(jobs, job_type):
    list = []
    for job in jobs:
        if job["job_type"] == job_type:
            list.append(job)
    return list


def get_unique_industries(path):
    all_jobs = read(path)
    console = set()
    for job in all_jobs:
        if job["industry"]:
            console.add(job["industry"])
    return console


def filter_by_industry(jobs, industry):
    industries = []
    for job in jobs:
        if job["industry"] == industry:
            industries.append(job)
    return industries


def get_max_salary(path):
    all_jobs = read(path)
    max_salary = 0

    for job in all_jobs:
        if (
            job["max_salary"].isnumeric()
            and int(job["max_salary"]) > max_salary
        ):
            max_salary = int(job["max_salary"])
    return max_salary


def get_min_salary(path):
    all_jobs = read(path)
    min_salary = 90000

    for job in all_jobs:
        if (
            job["min_salary"].isnumeric()
            and int(job["min_salary"]) < min_salary
        ):
            min_salary = int(job["min_salary"])
    return min_salary


# def verify_max_and_min_salary(job):

#     if "min_salary" not in job or "max_salary" not in job:
#         raise ValueError("Uma das chaves não existem")

#     if isinstance(job["min_salary"], )

# if not job["min_salary"].isnumeric() or not job["max_salary"].isnumeric:
#     raise ValueError("Não é inteiro")

#     if job["min_salary"] > job["max_salary"]:
#         raise ValueError("Salário mínimo maior")


def matches_salary_range(job, salary):
    # Requisito reestruturado com ajuda do Bux;

    # verify_max_and_min_salary(job)

    try:
        if type(salary) != int:
            raise ValueError("Salary deve ser um inteiro")

        if job["min_salary"] > job["max_salary"]:
            raise ValueError(
                "Salario minimo deve ser menor que salario máximo"
            )
        return job["min_salary"] <= salary <= job["max_salary"]
    except Exception:
        raise ValueError("Salary deve ser um inteiro")

    # if type(salary) != int:
    #     raise ValueError("Salary deve ser um inteiro")

    # if job["min_salary"] < job["max_salary"]:
    #     return True

    # return False


# matches_salary_range({"min_salary": "2000", "max_salary": "5000"}, 6000)


def filter_by_salary_range(jobs, salary):
    filtered_jobs = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_jobs.append(job)
        except ValueError:
            pass
    return filtered_jobs
