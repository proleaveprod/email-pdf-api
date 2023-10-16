from jinja2 import Environment, FileSystemLoader
import ___post_example as post_example

#---------------------------------------------
#      Часть с основными данными формы
# 
# Добавляется шаблонизатором jinja2 в 
# form_template.html
#---------------------------------------------
basic_json = post_example.basic_data
# Удаление всех пробелов из названий
for param in list(basic_json):
    new_key = param.replace(' ','_')
    basic_json[new_key] = basic_json.pop(param)
#---------------------------------------------
#      Часть с данными тестирования
# 
# Здесь просто вставляю элементы таблицы
#---------------------------------------------
test_data = post_example.test_data

test_html = ''
for element in test_data:
    data = f'''
            <tr>
                <th scope="row">
                    {element}:
                </th>
                <td>
                    {test_data[element]}
                </td>
            </tr>
            '''
    test_html += data

test_json = { 'test_data': test_html}
#---------------------------------------------

# Преобразование шаблона в rendered.html
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("./templates/form_template.html")
rendered_data = template.render( basic_json | test_json)
rendered_file = open(file = 'templates/rendered.html', mode = 'w', encoding = 'utf-8')
rendered_file.write(rendered_data)
