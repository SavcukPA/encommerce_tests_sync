from faker import Faker

from utils.generators import get_random_str

fake = Faker()

# минимальная длина first_name
case_1 = {
    "payload": {
        "email": fake.email(),
        "password": fake.password(),
        "first_name": get_random_str(len=2, case_type="title"),
        "last_name": fake.last_name(),
    },
    "meta_info": {"ids": "first_name: len 2 symbol"},
}

case_2 = {
    "payload": {
        "email": fake.email(),
        "password": fake.password(),
        "first_name": get_random_str(len=256, case_type="title"),
        "last_name": fake.last_name(),
    },
    "meta_info": {"ids": "first_name: len 256 symbol"},
}


positive_user_registry_cases = (
    case_1,
    case_2,
)
