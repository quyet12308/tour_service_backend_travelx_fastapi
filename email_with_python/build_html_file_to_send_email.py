from string import Template

def render_template(template_file, **kwargs):
    # Đọc nội dung của tệp tin HTML
    with open(template_file, "r") as file:
        template_content = file.read()

    # Sử dụng string.Template để truyền giá trị vào tệp tin HTML
    template = Template(template_content)
    rendered_content = template.substitute(kwargs)

    return rendered_content

rendered_html = render_template("index.html", name="Hello abc")
print(rendered_html)