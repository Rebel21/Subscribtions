import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class PageSubscriptions:

    EMAIL = (By.XPATH, '//input[@data-test="new-subs-email"]')
    NAME = (By.XPATH, '//input[@data-test="new-subs-name"]')
    TIMER = (By.XPATH, '//input[@data-test="new-subs-time"]')
    SUB_BUTTON = (By.XPATH, '//button[@data-test="new-subs-submit"]')
    SUBSCRIPTIONS = (By.XPATH, '//tr[@data-test="subs-table-row"]')
    SUB_MARKER_TIMER = (By.XPATH, '//*[@data-icon="times"]')
    SUB_MARKER_CHECK = (By.XPATH, '//*[@data-icon="check"]')
    SUB_EMAIL = (By.XPATH, '//td[@data-test="subs-table-email"]')
    SUB_NAME = (By.XPATH, '//th[@data-test="subs-table-name"]')
    CLEAR_BUTTON = (By.XPATH, '//button[@data-test="clear-button"]')

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def open_site(self, url):
        """
        Метод открывает сайт
        :param url: адрес сайта
        """
        self.driver.get(url)
        return

    def complete_fields(self, email, name, timer):
        """
        Метод заполняет все поля подписки
        :param email: Адрес электронной почты
        :param name: Имя пользователя
        :param timer: Срок подписки, например "7d" - 7 дней
        """
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.NAME).send_keys(name)
        self.driver.find_element(*self.TIMER).clear()
        self.driver.find_element(*self.TIMER).send_keys(timer)
        self.driver.find_element(*self.SUB_BUTTON).click()
        return

    def check_for_subscription_creation(self, num):
        """
        Метод проверяет, создалась ли новая подписка
        """
        time.sleep(1)
        assert len(self.driver.find_elements(*self.SUBSCRIPTIONS)) == num
        return

    def check_for_no_subscription_creation(self):
        """
        Метод проверяет, что подписка не создалась
        """
        try:
            self.driver.find_elements(*self.SUBSCRIPTIONS)
        except NoSuchElementException:
            return
        return

    def check_data_in_subscription(self, email, name, timer):
        """
        Метод сравнивает данные, введённые при создании подписки с отображаемымми в созданной подписке
        :param email: Адрес электронной почты
        :param name: Имя пользователя
        :param timer: Срок подписки
        """
        assert email == self.driver.find_element(*self.SUB_EMAIL).text
        assert name == self.driver.find_element(*self.SUB_NAME).text
        if timer == "0d":
            self.driver.find_element(*self.SUB_MARKER_TIMER)
        else:
            self.driver.find_element(*self.SUB_MARKER_CHECK)
        return

    def delete_subscriptions(self):
        """
         Метод очищает подписки пользователя
        """
        self.driver.find_element(*self.CLEAR_BUTTON).click()
        return