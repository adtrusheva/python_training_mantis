from fixture.project import Project
import random


def test_delete_project(app):
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    if len(app.soap.get_project_list(username, password)) == 0:
        app.project.add_project(Project(name="testone"))
    old_projects = app.soap.get_project_list(username, password)
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.soap.get_project_list(username, password)
    old_projects.remove(project)
    assert len(old_projects) == len(new_projects)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)