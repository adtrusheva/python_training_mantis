from fixture.project import Project
from data.add_project import testdata
import pytest


@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_add_project(app, project):
    app.session.login("administrator", "root")
    old_projects = app.project.get_project_list()
    app.project.add_project(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert len(old_projects) == len(new_projects)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
