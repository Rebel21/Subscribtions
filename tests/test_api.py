import pytest
from pages.api_module import ApiClient


@pytest.mark.usefixtures("clear_data_after_tests")
class TestCreate:
    """
    Данны кейс содержит тесты создания подписки
    """
    @pytest.mark.parametrize("data", [
        ["mail@mail.mail", "User1", "2d"],
        ["mail@mail.mail", "User2", "0d"]
    ])
    def test_create_subscription_valid_data(self, data):
        """
        Данный тест:
            отправляет POST запрос на создание подписки;
            проверяет код ответа 200;
            проверяет, что в ответе есть идентификато созданной записи и он не пустой.
        :param data: Список корректных данных для создания подписки
        """
        self.api_module = ApiClient()
        post_req = self.api_module.create_subscription(data[0], data[1], data[2])
        assert len(post_req.json()["id"]) > 0

    @pytest.mark.parametrize("data", [
        ["mail", "User1", "2d"],
        ["mail@mail.mail", "User2", "а"],
        ["", "", ""]
    ])
    def test_create_subscription_invalid_data(self, data):
        """
        Данный тест:
            отправляет POST запрос на создание подписки;
             проверяет код ответа 200;
             проверяет, что в ответе есть error
        :param data: Список не корректных данных для создания подписки
        """
        self.api_module = ApiClient()
        post_req = self.api_module.create_subscription(data[0], data[1], data[2])
        assert "error" in post_req.json()


@pytest.mark.usefixtures("clear_data_after_tests")
class TestView:
    """
    Данны кейс содержит тесты получения подписок
    """
    def test_get_subscriptions(self):
        """
        Данный тест :
            создает определённое количество подписок;
            отправляет GET запрос для получения списка подписок;
            проверяет код ответа 200;
            проверяет, что в ответ пришло то количество подписок, которое было создано на первом шаге
        """
        self.api_module = ApiClient()
        step = 0
        while step <= 4:
            self.api_module.create_subscription("mail@mail.mail", "User%d" % step, "%dd" % step)
            step += 1
        req = self.api_module.get_subscriptions()
        assert len(req.json()) == step


class TestDelete:
    """"
    Данный кейс содержит тесты удаления подписок
    """
    def test_delete_subscriptions(self):
        """
        Данный тест :
            создает определённое количество подписок;
            отправляет DELETE запрос для удаления списка подписок;
            проверяет код ответа 200;
            проверяет, что в ответ пришло то количество удалённых подписок, которое было создано на первом шаге
        """
        self.api_module = ApiClient()
        step = 0
        while step <= 4:
            self.api_module.create_subscription("mail@mail.mail", "User%d" % step, "%dd" % step)
            step += 1
        req = self.api_module.delete_subscriptions()
        assert req.json()["removed"] == step