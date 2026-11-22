import re

from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button


class CoursesListToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.title = Text(page, "courses-list-toolbar-title-text", "Title")
        self.create_course_button = Button(
            page,
            "courses-list-toolbar-create-course-button",
            "Create button",
        )

    def check_visible(self) -> None:
        self.title.check_visible()
        self.title.check_have_text('Courses')

        self.create_course_button.check_visible()

    def click_create_course_button(self) -> None:
        self.create_course_button.click()
        self.check_current_url(expected_url=re.compile(".*/#/courses/create"))
