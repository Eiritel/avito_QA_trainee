import requests
from conftest import default_payload


class TestRetrieveAdById:

    def test_successful_retrieval_with_valid_id(self, item_url, valid_id):
        response = requests.get(f'{item_url}/{valid_id}')

        assert response.status_code == 200, f"Ожидался статус код 200, но был {response.status_code}"

        ad_data = response.json()
        assert any(ad['id'] == valid_id for ad in ad_data), f"Объявление с id {valid_id} не найдено"

    def test_retrieval_with_invalid_id(self, item_url, invalid_id):
        response = requests.get(f'{item_url}/{invalid_id}')

        assert response.status_code == 404, f"Ожидался статус 404, но получен {response.status_code}"


class TestRetrieveAdsBySellerId:

    def test_successful_fetch_with_valid_seller(self, seller_url, existing_seller_id):
        response = requests.get(seller_url.format(seller_id=existing_seller_id))

        assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}"

        ads = response.json()
        for ad in ads:
            assert ad['sellerId'] == int(
                existing_seller_id), f"Продавец в объявлении {ad['id']} отличается от {existing_seller_id}"

    def test_fetch_for_seller_with_no_ads(self, seller_url, without_items_seller_id):
        response = requests.get(seller_url.format(seller_id=without_items_seller_id))

        assert response.status_code == 200, f"Ожидался статус 200, но был {response.status_code}"

        ads = response.json()
        assert ads == [], "Ожидался пустой список, но вернулись данные."


class TestCreateNewAd:

    def test_create_ad_with_valid_data(self, item_url, default_payload):
        response = requests.post(item_url, json=default_payload)

        assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}"

    def test_create_with_non_existent_positive_seller(self, item_url, default_payload, non_existent_positive_seller_id):
        ad_payload = default_payload.copy()
        ad_payload['sellerId'] = non_existent_positive_seller_id

        response = requests.post(item_url, json=ad_payload)
        assert response.status_code == 200, "Объявление с несуществующим sellerId должно быть создано"
