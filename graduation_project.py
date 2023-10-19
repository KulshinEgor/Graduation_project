import configuration
import data
import requests


# Создание нового заказа
def post_new_order():
    return requests.post(url=configuration.URL + configuration.create_order,
                         json=data.order_body).json()  # Нужно дописать функцию


response_new_order = post_new_order()
print(response_new_order)

# Получение трэк номер заказа
def track_order():
    track_orders = requests.post(url=configuration.URL + configuration.create_order,
                                 json=data.order_body).json()['track']
    return track_orders


def get_orders():
    return requests.get(configuration.URL + configuration.order_track + str(track_order())).status_code


response_get_orders = get_orders()
print(response_get_orders)