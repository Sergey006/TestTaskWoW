from first_task.browser import Browser


class BaseComponent:

    def __init__(self, browser: Browser):
        self.browser = browser
