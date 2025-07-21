import os
import jinja2

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'templates')

def list_frameworks():
    return [d for d in os.listdir(TEMPLATES_DIR) if os.path.isdir(os.path.join(TEMPLATES_DIR, d))]

def list_templates(framework):
    framework_dir = os.path.join(TEMPLATES_DIR, framework)
    if not os.path.isdir(framework_dir):
        return []
    return [f for f in os.listdir(framework_dir) if f.endswith('.md')]

def load_template(framework, template_name):
    path = os.path.join(TEMPLATES_DIR, framework, template_name)
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def render_template(template_str, variables):
    template = jinja2.Template(template_str)
    return template.render(**variables) 