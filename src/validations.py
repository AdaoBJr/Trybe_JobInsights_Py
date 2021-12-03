def valid_keys_in_job(job):
    if not('min_salary' in job.keys()):
        raise ValueError

    if not('max_salary' in job.keys()):
        raise ValueError

    return True


def valid_min_and_max_is_integer(job):
    if not(isinstance(job['min_salary'], int)):
        raise ValueError

    if not(isinstance(job['max_salary'], int)):
        raise ValueError

    return True


def valid_min_is_greather_than_max(job):
    if job['min_salary'] > job['max_salary']:
        raise ValueError

    return True


def valid_salary_is_an_integer(salary):
    if type(salary) != int:
        raise ValueError

    return True


# if not('min_salary' in job.keys()):
#     raise ValueError('min key not contain in jobs')

# if not('max_salary' in job.keys()):
#     raise ValueError('max key not contain in jobs')

# if not(isinstance(job['min_salary'], int)):
#     raise ValueError('min is not a integer')

# if not(isinstance(job['max_salary'], int)):
#     raise ValueError('max is not a integer')

# if job['min_salary'] > job['max_salary']:
#     raise ValueError('min value is greather than max value')

# if type(salary) != int:
#     raise ValueError('salary is not a integer')
