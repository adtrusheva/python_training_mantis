from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def add_project(self, project):
        wd = self.app.wd
        self.open_control_page()
        self.open_control_project_page()
        wd.find_element_by_css_selector(".form-inline.inline button[type=submit]").click()
        self.fill_form(project)
        wd.find_element_by_css_selector("input[type=submit]").click()
        self.project_cache = None

    def open_control_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("ul.nav-list li .fa-gears").click()

    def open_control_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Управление проектами").click()

    def fill_form(self, project):
        self.change_field_value("name", project.name)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.open_control_page()
            self.open_control_project_page()
            self.project_cache = []
            for element in wd.find_elements_by_css_selector('.widget-box:nth-of-type(2) table.table tbody tr'):
                url = element.find_element_by_css_selector('td:first-child a').get_attribute('href')
                id = url.split('=')[-1]
                name = element.find_element_by_css_selector('td:first-child a').text
                self.project_cache.append(Project(name=name, id=id))
        return list(self.project_cache)

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_project_by_id(id)
        wd.find_element_by_css_selector('#project-delete-form input[type=submit]').click()
        wd.find_element_by_css_selector('input[type=submit]').click()
        self.project_cache = None

    def open_project_by_id(self, id):
        wd = self.app.wd
        self.open_control_page()
        self.open_control_project_page()
        for element in wd.find_elements_by_css_selector('.widget-box:nth-of-type(2) table.table tbody tr'):
            project_link = element.find_element_by_css_selector('td:first-child a')
            url = project_link.get_attribute('href')
            id_in_url = url.split('=')[-1]
            if id_in_url == id:
                project_link.click()
                break
