import pytest

BASE_URL = "https://qa-internship.avito.com/api/1"


@pytest.fixture(scope='function')
def default_payload():
    return {
        "name": "Телефон",
        "price": 85566,
        "sellerId": 3452,
        "statistics": {
            "contacts": 32,
            "like": 35,
            "viewCount": 14
        }
    }


@pytest.fixture(scope='function')
def item_url():
    return f"{BASE_URL}/item"


@pytest.fixture(scope='function')
def seller_url():
    return f"{BASE_URL}/{{seller_id}}/item"


@pytest.fixture(scope='function')
def valid_id():
    return "07d2b4fc-4e4c-4427-bbb0-74a67fa5ce38"


@pytest.fixture(scope='function')
def invalid_id():
    return "123456789"


@pytest.fixture(scope='function')
def existing_seller_id():
    return 3452


@pytest.fixture(scope='function')
def without_items_seller_id():
    return 9999


@pytest.fixture(scope='function')
def non_existent_positive_seller_id():
    return 999999999


@pytest.fixture(scope='function')
def non_existent_negative_seller_id():
    return -1


@pytest.fixture(scope='function')
def empty_name():
    return " "


@pytest.fixture(scope='function')
def negative_price():
    return -100


@pytest.fixture(scope='function')
def negative_contacts():
    return -5


@pytest.fixture(scope='function')
def negative_like():
    return -10


@pytest.fixture(scope='function')
def negative_view_count():
    return -15


@pytest.fixture(scope='function')
def negative_contacts_type():
    return "everyone"
