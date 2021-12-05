from jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    all_jobs = read(path)
    job_type = set()
    for cur in all_jobs:
        job_type.add(cur["job_type"])
    return job_type


print(get_unique_job_types("src/jobs.csv"))