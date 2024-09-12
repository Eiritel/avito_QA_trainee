import requests
from conftest import default_payload


class TestCreateNewAdFailed:

    def test_create_with_negative_seller_id(self, item_url, default_payload, non_existent_negative_seller_id):
        ad_payload = default_payload.copy()
        ad_payload['sellerId'] = non_existent_negative_seller_id

        response = requests.post(item_url, json=ad_payload)
        assert response.status_code == 400, f"Ожидался статус 400, но получен {response.status_code}"

        error_response = response.json()
        assert "error" in error_response or "message" in error_response, "Ошибка должна содержать описание"

    def test_create_with_empty_name(self, item_url, empty_name, default_payload):
        ad_payload = default_payload.copy()
        ad_payload['name'] = empty_name

        response = requests.post(item_url, json=ad_payload)
        assert response.status_code == 400, "Ожидался статус 400 для пустого названия"

        error_response = response.json()
        assert "error" in error_response or "message" in error_response, "Ожидалось сообщение об ошибке"

    def test_create_with_negative_price(self, item_url, default_payload, negative_price):
        ad_payload = default_payload.copy()
        ad_payload['price'] = negative_price

        response = requests.post(item_url, json=ad_payload)
        assert response.status_code == 400, "Ожидался статус 400 для отрицательной цены"

        error_response = response.json()
        assert "error" in error_response or "message" in error_response, "Ожидалось сообщение об ошибке"

    def test_create_with_invalid_contact_count(self, item_url, default_payload, negative_contacts):
        ad_payload = default_payload.copy()
        ad_payload['contacts'] = negative_contacts

        response = requests.post(item_url, json=ad_payload)
        assert response.status_code == 400, f"Ожидался статус 400, но получен {response.status_code}"

        error_response = response.json()
        assert "error" in error_response or "message" in error_response, "Ожидалось сообщение об ошибке"

    def test_create_with_invalid_negative_like(self, item_url, default_payload, negative_like):
        ad_payload = default_payload.copy()
        ad_payload['like'] = negative_like

        response = requests.post(item_url, json=ad_payload)
        assert response.status_code == 400, f"Ожидался статус 400, но получен {response.status_code}"

        error_response = response.json()
        assert "error" in error_response or "message" in error_response, "Ожидалось сообщение об ошибке"

    def test_create_with_invalid_view_count(self, item_url, default_payload, negative_view_count):
        ad_payload = default_payload.copy()
        ad_payload['view'] = negative_view_count

        response = requests.post(item_url, json=ad_payload)
        assert response.status_code == 400, f"Ожидался статус 400, но получен {response.status_code}"

        error_response = response.json()
        assert "error" in error_response or "message" in error_response, "Ожидалось сообщение об ошибке"

    def test_create_with_incorrect_contacts_type(self, item_url, default_payload, negative_contacts_type):
        ad_payload = default_payload.copy()
        ad_payload['contacts'] = negative_contacts_type

        response = requests.post(item_url, json=ad_payload)
        assert response.status_code == 400, "Ожидался статус 400 для некорректного типа данных 'contacts'"

        error_response = response.json()
        assert "error" in error_response or "message" in error_response, "Ожидалось сообщение об ошибке"
