from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader

from scraper import get_data

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("template.html")

data = get_data('garyvee')

template_vars = {'data': data,
                 }
html_out = template.render(template_vars)
#print(html_out)
HTML(string=html_out).write_pdf('out.pdf',stylesheets=['style.css'])
