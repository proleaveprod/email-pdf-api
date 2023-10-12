from jinja2 import Environment, FileSystemLoader

name = 'Sasha'

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("pdf_template.html")

pdf_template = template.render({'sas': name})

print("pdf_template was updated")