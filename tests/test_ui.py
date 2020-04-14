import pytest
from pages.page_subscriptions import PageSubscriptions


@pytest.mark.usefixtures("get_driver")
class TestFieldValidation:
    """
    Данный кейс содержит тесты на валидность полей ввода
    """
    @pytest.mark.parametrize("data", [
        ["mail@mail.mail", "User1", "2d"],
        ["mail@mail.mail", "User2", "0d"]
    ])
    def test_create_subscription_valid_data(self, data):
        """
        Данный тест:
            переходит на страницу подписок;
            создаёт подписку;
            проверяет, что подписка создана;
            проверяет, что данные в подписке и при её создании совпадают
        :param data: Список корректных данных для создания подписки
        """
        self.page_subscriptions = PageSubscriptions(self.driver)
        self.page_subscriptions.open_site("http://127.0.0.1:4000/ui")
        self.page_subscriptions.complete_fields(data[0], data[1], data[2])
        self.page_subscriptions.check_for_subscription_creation(1)
        self.page_subscriptions.check_data_in_subscription(data[0], data[1], data[2])

    @pytest.mark.parametrize("data", [
        ["mail", "User1", "2d"],
        ["mail@mail.mail", "User1", "2"],
        ["", "", ""]
    ])
    def test_create_subscription_invalid_data(self, data):
        """
        Данный тест:
            переходит на страницу подписок;
            создаёт подписку;
            проверяет, что подписка не создана;
        :param data: Список некорректных данных для создания подписки
        """
        self.page_subscriptions = PageSubscriptions(self.driver)
        self.page_subscriptions.open_site("http://127.0.0.1:4000/ui")
        self.page_subscriptions.complete_fields(data[0], data[1], data[2])
        self.page_subscriptions.check_for_no_subscription_creation()


@pytest.mark.usefixtures("get_driver")
class TestDataDuplication:
    """
    Данный кейс содержит тест на дублировние подписок
    """
    def test_create_same_data(self):
        """
        Данный тест:
            переходит на страницу подписок;
            создаёт 2 одинаковые подписки ;
            проверяет, что соднана только 1 подписка;
        """
        self.page_subscriptions = PageSubscriptions(self.driver)
        self.page_subscriptions.open_site("http://127.0.0.1:4000/ui")
        for i in range(2):
            self.page_subscriptions.complete_fields("mail@mail.mail", "User1", "5d")
        self.page_subscriptions.check_for_subscription_creation(1)


@pytest.mark.usefixtures("get_driver")
class TestDisplayingMoreFiveSubscription:
    """
    Данный кейс содержит тест на отображения 5 подписок
    """
    def test_create_over_five_subscriptions(self):
        """
        Данный тест:
            переходит на страницу подписок;
            создаёт 6 подписки ;
            проверяет, что отображаются только 5 подписок;
        """
        self.page_subscriptions = PageSubscriptions(self.driver)
        self.page_subscriptions.open_site("http://127.0.0.1:4000/ui")
        for i in range(6):
            self.page_subscriptions.complete_fields("mail@mail.mail", "User%d" % i, "5d")
        self.page_subscriptions.check_for_subscription_creation(5)
