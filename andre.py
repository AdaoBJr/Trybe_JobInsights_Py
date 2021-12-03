# import csv

# with open("src/jobs.csv", "r") as f:
#     reader = csv.DictReader(f)
#     get_higher_salaries = []
#     for job in reader:
#         if job["max_salary"] != "":
#             if job["max_salary"].isdigit():
#                 get_higher_salaries.append(int(job["max_salary"]))
#     print(max(get_higher_salaries))
