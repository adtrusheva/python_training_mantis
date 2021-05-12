from fixture.project import Project
from data.add_project import testdata
import pytest


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project):
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    old_projects = app.soap.get_project_list(username, password)
    app.project.add_project(project)
    new_projects = app.soap.get_project_list(username, password)
    old_projects.append(project)
    assert len(old_projects) == len(new_projects)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
