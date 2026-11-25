from playwright.sync_api import Page
import allure

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.title = Text(page, "create-course-toolbar-title-text", "Title")
        self.create_button = Button(
            page,
            "create-course-toolbar-create-course-button",
            "Create button",
        )

    @allure.step("Check visible create course toolbar view, is_create_course_disabled = {is_create_course_disabled}")
    def check_visible(self, is_create_course_disabled: bool = True) -> None:
        self.title.check_visible()
        self.title.check_have_text(text='Create course')

        self.create_button.check_visible()

        if is_create_course_disabled:
            self.create_button.check_disabled()
        else:
            self.create_button.check_enabled()

    def click_create_course_button(self) -> None:
        self.create_button.click()
