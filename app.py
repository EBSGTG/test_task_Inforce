from flask import Flask, request, render_template, redirect, url_for
from flask_migrate import Migrate
from config import Config
from models import db, Project

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/add_project', methods=['POST', 'GET'])
def create_project():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        stack = request.form['stack']
        status = request.form['status']
        private = 'private' in request.form
        accepted = 'accepted' in request.form

        new_project = Project(
            name=name,
            description=description,
            stack=stack,
            status=status,
            private=private,
            accepted=accepted,
            creator_id=1
        )
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('list_projects'))

    return render_template("create_project.html")




@app.route('/projects', methods=['GET'])
def list_projects():
    projects = Project.query.all()
    return render_template('list_projects.html', projects=projects)


if __name__ == '__main__':
    app.run(debug=True)
