import jobs
# from src import jobs


def get_unique_job_types(path):
    jobs_list = jobs.read(path)
    types = set()
    for job in jobs_list:
        if job['job_type'] != "":
            types.add(job['job_type'])
    return types


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    return []


def get_unique_industries(path):
    jobs_list = jobs.read(path)
    industrys = set()
    for job in jobs_list:
        if job['industry'] != "":
            industrys.add(job["industry"])
    return industrys


print(get_unique_industries("src/jobs.csv"))
