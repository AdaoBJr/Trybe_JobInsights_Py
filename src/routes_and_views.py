from markdown import markdown
from flask import Flask, Blueprint, render_template, request

from .jobs import read
from .insights import (
    get_unique_industries,
    get_unique_job_types,
    filter_by_salary_range,
    filter_by_industry,
    filter_by_job_type,
    get_min_salary,
    get_max_salary,
)
from .more_insights import (
    get_job,
    slice_jobs,
    get_int_from_args,
    build_jobs_urls,
)

bp = Blueprint("client", __name__, template_folder="templates")

PATH = "src/jobs.csv"


@bp.route("/")
def index():
    with open("README.md", encoding="UTF-8") as file:
        md = markdown(file.read())
    return render_template("index.jinja2", md=md)


@bp.route("/jobs")
def list_jobs():
    first_job = get_int_from_args("first_job", 0)
    amount = get_int_from_args("amount", 20)
    salary = get_int_from_args("salary", None)
    industry = request.args.get("industry", None)
    job_type = request.args.get("job_type", None)

    jobs = read(PATH)
    if industry:
        jobs = filter_by_industry(jobs, industry)
    if job_type:
        jobs = filter_by_job_type(jobs, job_type)
    if salary:
        jobs = filter_by_salary_range(jobs, salary)

    jobs = slice_jobs(jobs, first_job, amount)

    build_jobs_urls(jobs)

    ctx = {
        "jobs": jobs,
        "industries": sorted(get_unique_industries(PATH)),
        "job_types": sorted(get_unique_job_types(PATH)),
        "previous_job_type": job_type,
        "previous_first": first_job,
        "previous_amount": amount,
        "previous_industry": industry,
        "previous_salary": salary,
        "min_salary": get_min_salary(PATH),
        "max_salary": get_max_salary(PATH),
    }

    return render_template("list_jobs.jinja2", ctx=ctx)


@bp.route("/job/<index>")
def job(index):
    jobs = read(PATH)
    job = get_job(jobs, index)
    return render_template("job.jinja2", job=job)


def init_app(app: Flask):
    app.register_blueprint(bp)
