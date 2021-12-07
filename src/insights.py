from src import jobs
# import jobs


def get_unique_job_types(path):
    jobs_list = jobs.read(path)
    return list(set([job['job_type'] for job in jobs_list]))


# print(get_unique_job_types('src/jobs.csv'))


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job['job_type'] == job_type]


def get_unique_industries(path):
    jobs_list = jobs.read(path)
    industries = set([
        job['industry'] for job in jobs_list if job['industry'] != ''])
    return list(industries)


# print(get_unique_industries('src/jobs.csv'))


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job['industry'] == industry]

# SOURCE https://pt.stackoverflow.com/questions/257905/retornando-
# somente-o-maior-valor-de-uma-lista-python


def get_max_salary(path):
    jobs_list = jobs.read(path)
    salary = set([
        job['max_salary'] for job in jobs_list if job['max_salary'].isdigit()])
    max_salary = max(int(num) for num in salary)
    return max_salary


# print(get_max_salary('src/jobs.csv'))


def get_min_salary(path):
    jobs_list = jobs.read(path)
    salary = set([
        job['min_salary'] for job in jobs_list if job['min_salary'].isdigit()])
    min_salary = min(int(num) for num in salary)
    return min_salary


def matches_salary_range(job, salary):
    try:
        if job['min_salary'] <= int(salary) <= job['max_salary']:
            return True
        elif job['min_salary'] > job['max_salary']:
            raise ValueError
        else:
            return False
    except(KeyError, TypeError, NameError, ValueError):
        raise ValueError


# print(matches_salary_range({"min_salary": "100", "max_salary": "1000"}, {}))


def filter_by_salary_range(jobs, salary):
    list = []
    for job in jobs:
        try:
            result = matches_salary_range(job, salary)
            if result is True:
                list.append(job)
        except ValueError:
            pass
    return list

# jobss = [
#         {"max_salary": 0, "min_salary": 10},
#         {"max_salary": 10, "min_salary": 100},
#         {"max_salary": 10000, "min_salary": 200},
#         {"max_salary": 15000, "min_salary": 0},
#         {"max_salary": 1500, "min_salary": 0},
#         {"max_salary": -1, "min_salary": 10},
#     ]
# print(filter_by_salary_range(jobss, 1000))
