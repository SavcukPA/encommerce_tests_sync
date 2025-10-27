from pprint import pprint
import data
import pytest
import uuid
import validators
import services
from data.auth_cases.user_register_cases import positive_user_registry_cases
from faker import Faker


fake = Faker()


class TestAuth:

    @pytest.mark.parametrize(
        "cases",
        data.positive_user_registry_cases,
        ids=[case["meta_info"]["ids"] for case in data.positive_user_registry_cases],
    )
    @pytest.mark.users
    @pytest.mark.regression
    def test_registry_user(
        self,
        http_client,
        cases,
    ):
        pprint(cases["payload"])
        auth = services.Auth(client=http_client)
        res = auth.registry_user(payload=cases["payload"])
        assert validators.uuid(res["id"]) is True
        assert res["first_name"] == cases["payload"]["first_name"]
        assert res["last_name"] == cases["payload"]["last_name"]
        assert res["email"] == cases["payload"]["email"]
