import click
import template_loader
import json

@click.group()
def cli():
    pass

@cli.command()
def frameworks():
    """List available frameworks."""
    for fw in template_loader.list_frameworks():
        click.echo(fw)

@cli.command()
@click.argument('framework')
def templates(framework):
    """List templates for a framework."""
    for t in template_loader.list_templates(framework):
        click.echo(t)

@cli.command()
@click.argument('framework')
@click.argument('template_name')
def show(framework, template_name):
    """Show the raw Markdown of a template."""
    click.echo(template_loader.load_template(framework, template_name))

@cli.command()
@click.argument('framework')
@click.argument('template_name')
@click.option('--vars', default='{}', help='JSON string of variables to render the template with.')
def render(framework, template_name, vars):
    """Render a template with variables (as JSON)."""
    template_str = template_loader.load_template(framework, template_name)
    variables = json.loads(vars)
    click.echo(template_loader.render_template(template_str, variables))

if __name__ == '__main__':
    cli() 