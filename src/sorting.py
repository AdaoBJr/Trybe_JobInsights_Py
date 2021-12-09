import math
from datetime import date


def max_salary_key(job):
    """
    Gets max_salary as a sorting key.

    Missing information is treated as the lowest possible value.

    Parameters
    ----------
    job : dict
        Dict represeting a job from the dataset.

    Returns
    -------
    Job's max salary as an int, or -infinite.
    """
    try:
        return int(job["max_salary"])
    except (KeyError, TypeError, ValueError):
        return -math.inf


def min_salary_key(job):
    """
    Gets min_salary as a sorting key.

    Missing information is treated as the highest possible value.

    Parameters
    ----------
    job : dict
        Dict represeting a job from the dataset.

    Returns
    -------
    Job's min salary as an int, or infinite.
    """
    try:
        return int(job["min_salary"])
    except (KeyError, TypeError, ValueError):
        return math.inf


def date_posted_key(job):
    """
    Gets date_posted as a sorting key.

    Missing information is treated as the lowest possible value.

    Parameters
    ----------
    job : dict
        Dict represeting a job from the dataset.

    Returns
    -------
    Job's date_posted as a date object.
    """
    try:
        return date.fromisoformat(job["date_posted"])
    except (KeyError, TypeError, ValueError):
        return date.min


def sort_by(jobs, criteria):
    """
    Sorts jobs by a given criteria, in-place.

    Sorting must be descending, except for `min_salary` criteria.
    Jobs missing the criteria should end up last.
    Invalid criteria should raise ValueError.

    Parameters
    ----------
    jobs : list
        List of dicts representing the jobs.
    criteria : str
        One of `min_salary`, `max_salary` or `date_posted`.
    """
    criteria_keys = {
        "date_posted": date_posted_key,
        "max_salary": max_salary_key,
        "min_salary": min_salary_key,
    }

    try:
        key = criteria_keys[criteria]
    except KeyError:
        raise ValueError(f"invalid sorting criteria: {criteria}")

    reverse = criteria in ["max_salary", "date_posted"]

    jobs.sort(key=key, reverse=reverse)


# if __name__ == '__main__':
#     job_1 = {
#         "job_title": "backend dev",
#         "min_salary": 3000,
#         "max_salary": 10000,
#         "date_posted": "2021-08-12"
#     }

#     job_2 = {
#         "job_title": "frontend dev",
#         "min_salary": 2500,
#         "max_salary": 9000,
#         "date_posted": "2021-04-03"
#     }

#     job_3 = {
#         "job_title": "java dev",
#         "min_salary": 3500,
#         "max_salary": 12000,
#         "date_posted": "2021-03-08"
#     }

#     jobs = [job_1, job_2, job_3]

#     result_by_min_salary = [job_2, job_1, job_3]
#     result_by_max_salary = [job_3, job_1, job_2]
#     result_by_date_posted = [job_1, job_2, job_3]

#     teste = sort_by(jobs, 'max_salary')
#     print(teste)
#     print(jobs[0])
