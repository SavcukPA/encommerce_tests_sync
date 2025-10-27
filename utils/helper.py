import logging
from enum import Enum

import allure
from httpx import Response
from pydantic import BaseModel
from pydantic_core.core_schema import JsonType

log = logging.getLogger(__name__)


import allure
import logging
from httpx import Response

logger = logging.getLogger(__name__)


class ResponseType(Enum):

    JSON = "json"
    PYDANTIC_MODEL = "pydantic_model"


class Helper:

    response_type = ResponseType

    @staticmethod
    def basic_assert(
        response: Response,
        expected_code: int = 200,
        pydantic_model=None,
        response_type: ResponseType = ResponseType.JSON,
    ):

        actual_code = response.status_code
        reason = response.reason_phrase or "No reason phrase"

        if actual_code != expected_code:
            error_msg = (
                f"Status code assertion failed.\n"
                f"Expected status code: {expected_code}\n"
                f"Actual: {actual_code} {reason}\n"
                f"URL: {response.url}\n"
                f"Method: {response.request.method}\n"
                f"Response text: {response.text}..."
            )

            allure.attach(
                error_msg,
                name=f"HTTP Error {actual_code}",
                attachment_type=allure.attachment_type.TEXT,
            )
            logger.error(error_msg)
            if pydantic_model:
                pydantic_model.model_validate(response.json())
            if response_type == ResponseType.PYDANTIC_MODEL:
                return pydantic_model(**response.json())
            if response_type == ResponseType.JSON:
                return response.json()

            raise AssertionError(error_msg)

        logger.info(f"Status code check passed: {actual_code} for {response.url}")
