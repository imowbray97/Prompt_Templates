from flask import Flask, render_template_string, request, redirect, url_for
import template_loader
import os

app = Flask(__name__)

@app.route('/')
def index():
    frameworks = template_loader.list_frameworks()
    return render_template_string('''<h1>Prompt Template Library</h1>
    <ul>
    {% for fw in frameworks %}
      <li><a href="{{ url_for('framework', framework=fw) }}">{{ fw }}</a></li>
    {% endfor %}
    </ul>
    ''', frameworks=frameworks)

@app.route('/<framework>')
def framework(framework):
    templates = template_loader.list_templates(framework)
    return render_template_string('''<h2>Framework: {{ framework }}</h2>
    <ul>
    {% for t in templates %}
      <li><a href="{{ url_for('template_view', framework=framework, template_name=t) }}">{{ t }}</a></li>
    {% endfor %}
    </ul>
    <a href="/">Back</a>
    ''', framework=framework, templates=templates)

@app.route('/<framework>/<template_name>', methods=['GET', 'POST'])
def template_view(framework, template_name):
    template_str = template_loader.load_template(framework, template_name)
    rendered = None
    variables = {}
    if request.method == 'POST':
        variables = {k: v for k, v in request.form.items()}
        rendered = template_loader.render_template(template_str, variables)
    return render_template_string('''<h3>Template: {{ template_name }}</h3>
    <form method="post">
      <textarea name="template" rows="10" cols="60" readonly>{{ template_str }}</textarea><br>
      <h4>Variables (enter values):</h4>
      {% for var in template_str|find_vars %}
        {{ var }}: <input name="{{ var }}" value="{{ request.form.get(var, '') }}"><br>
      {% endfor %}
      <input type="submit" value="Render">
    </form>
    {% if rendered %}
      <h4>Rendered Output:</h4>
      <pre>{{ rendered }}</pre>
    {% endif %}
    <a href="{{ url_for('framework', framework=framework) }}">Back</a>
    ''', framework=framework, template_name=template_name, template_str=template_str, rendered=rendered, request=request), 200, {'Content-Type': 'text/html'}

# Jinja2 filter to find variables in template
@app.template_filter('find_vars')
def find_vars_filter(template_str):
    import re
    return re.findall(r'{{\s*(\w+)\s*}}', template_str)

if __name__ == '__main__':
    app.run(debug=True) 