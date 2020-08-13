from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
import sys

from scraper import get_data

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("template.html")


def get_template(name):
    data = get_data(name)

    template_vars = {'data': data, }

    html_out = template.render(template_vars)

    HTML(string=html_out).write_pdf('out.pdf', stylesheets=['style.css'])


if __name__ == "__main__":
    name = str(sys.argv[1])
    get_template(name)
