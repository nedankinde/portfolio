import urllib.request
from flask import Flask, request, url_for, render_template, redirect, jsonify

app = Flask(__name__)

all_projects = {
    'interpreter' : {
        'name': 'Odie: Interpreter',
        'source': 'https://github.com/koficenti/Odie',
        'readme': 'https://github.com/koficenti/Odie/raw/refs/heads/main/README.md',
    },
    'nice-WS' : {
        'name': 'Websocket Library',
        'source': 'https://github.com/koficenti/nice-ws',
        'readme': 'https://github.com/koficenti/nice-ws/raw/refs/heads/main/README.md',
    },
    'BASIC' : {
        'name': 'BASIC',
        'source': 'https://github.com/koficenti/BASIC',
        'readme': 'https://github.com/koficenti/BASIC/raw/refs/heads/main/README.md',
    },
    'TYPI': {
        'name': 'TYPI',
        'source': 'https://github.com/koficenti/typi',
        'readme': 'https://github.com/koficenti/typi/raw/refs/heads/main/README.md',
    },
    'svelte-portfolio': {
        'name': 'Svelte Portfolio',
        'demo': 'https://portfolio-eight-beta-90.vercel.app/',
        'source': 'https://github.com/koficenti/portfolio',
        'readme': 'https://github.com/koficenti/portfolio/raw/refs/heads/main/README.md',
    },
    'this-portfolio': {
        'name': 'Flask Portfolio',
        'demo': 'http://34.200.144.216/',
        'source': 'https://github.com/nedankinde/portfolio',
        'readme': 'https://github.com/nedankinde/portfolio/raw/refs/heads/main/README.md'
    }
}

def generate_breadcrumbs():
    path = request.path.strip('/').split('/')
    breadcrumbs = [{'name': 'Home', 'url': url_for('index')}]
    current_path = ''
    
    for part in path:
        current_path += f'/{part}'
        breadcrumbs.append({
            'name': part.capitalize(),
            'url': current_path
        })
    
    return breadcrumbs


@app.route('/')
def index():
    breadcrumbs = generate_breadcrumbs()
    component = render_template('components/about.html')
    return render_template('index.html', data=component, breadcrumbs=breadcrumbs, projects=all_projects)

@app.route('/projects')
def projects():
    breadcrumbs = generate_breadcrumbs()
    component = render_template('components/projects.html', projects=all_projects)
    return render_template('index.html', data=component, breadcrumbs=breadcrumbs, projects=all_projects)

@app.route('/projects/<project>')
def project(project):
    p = all_projects.get(project)
    if not p:
        return redirect(url_for('projects'))
    breadcrumbs = generate_breadcrumbs()
    readme = urllib.request.urlopen(p['readme']).read().decode('utf-8')
    component = render_template('components/project.html', project=p, readme='\n\n' + readme)
    return render_template('index.html', data=component, breadcrumbs=breadcrumbs, projects=all_projects, active_project=p)