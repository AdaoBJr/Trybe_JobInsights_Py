from src.jobs import read


def get_unique_job_types(path):
  job_types = read(path)

  return set([job["job_type"] for job in job_types])


def filter_by_job_type(jobs, job_type):
  return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
  jobs_list = read(path)
  return set([job["industry"] for job in jobs_list if job["industry"]])


def filter_by_industry(jobs, industry):
  return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
  jobs_list = read(path)
  return max([
    int(job["max_salary"])
    for job
    in jobs_list
    if job["max_salary"] and job["max_salary"].isnumeric()
  ])


def get_min_salary(path):
  jobs_list = read(path)
  return min([
    int(job["min_salary"])
    for job
    in jobs_list
    if job["min_salary"] and job["min_salary"].isnumeric()
  ])


def matches_salary_range(job, salary):
  if ("min_salary" not in job or "max_salary" not in job):
    raise ValueError
  
  if (
    type(job["min_salary"]) != int or
    type(job["max_salary"]) != int or
    type(salary) != int
  ): 
    raise ValueError

  if job["min_salary"] > job["max_salary"]:
    raise ValueError

  return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
  filter_list = []
  for job in jobs:
      try:
          if matches_salary_range(job, salary):
              filter_list.append(job)
      except ValueError:
          pass
  return filter_list