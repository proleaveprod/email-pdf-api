from jinja2 import Environment, FileSystemLoader

name = 'Sasha'

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("/pdf_former/src/pdf_template.html")

pdf_template = template.render({'sas': name})

print("HTML file was created")

