import logging

import allure

from clients.base_client import BaseClient
from services.auth.endpoints import Endpoints

from faker import Faker

from services.auth.models.register import User

fake = Faker()

logger = logging.getLogger(__name__)


class Auth(BaseClient):

    __endpoints = Endpoints

    def __init__(self, client):
        super().__init__(client=client)

    @allure.step("Регистрация нового пользователя")
    def registry_user(
        self,
        payload: dict,
    ) -> dict:
        """
        Регистрация нового пользователя

        Args:
            payload: Данные для регистрации пользователя
                Пример: {
                    "email": "user@example.com",
                    "password": "password123",
                    "first_name": "John",
                    "last_name": "Doe"
                }

        Returns:
            dict: Ответ API с данными пользователя

        Raises:
            AssertionError: Если статус код не 201
        """
        try:
            response = self.post(
                url=f"{self.host}{self.__endpoints.register}",
                json=payload,
            )
            self.basic_assert(response=response, expected_code=201, pydantic_model=User)
            return response.json()
        except Exception as e:
            logger.error(f"User registration failed: {e}")
            raise
