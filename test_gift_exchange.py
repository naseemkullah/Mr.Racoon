import gift_exchange
import os

def test_giftgiving_requires_a_registration_file():

    #given
    try:
        os.remove('test_family.json')
    except OSError:
        pass
    #when
    x = gift_exchange.giftgiving('test_family.json')
    #then
    assert x == gift_exchange.NO_FILE_ERROR

def test_giftgiving_requires_more_than_one_member():

    #given
    data = {"bob": "suzy"}
    with open('test_family.json', 'w') as f:
        gift_exchange.json.dump(data, f)
    #when
    x = gift_exchange.giftgiving('test_family.json')
    #then
    assert x == gift_exchange.MEMBER_COUNT_ERROR
    os.remove('test_family.json')

def test_giftgiving_requires_more_than_one_couple():

    #given
    data = {"bob": "suzy", "suzy": "bob"}
    with open('test_family.json', 'w') as f:
        gift_exchange.json.dump(data, f)
    #when
    x = gift_exchange.giftgiving('test_family.json')
    #then
    assert x == gift_exchange.LONE_COUPLE_ERROR
    os.remove('test_family.json')

def test_giftgiving_requires_more_than_one_couple_and_another_person():

    #given
    data = {"bob": "suzy", "suzy": "bob", "joe": None}
    with open('test_family.json', 'w') as f:
        gift_exchange.json.dump(data, f)
    #when
    x = gift_exchange.giftgiving('test_family.json')
    #then
    assert x == gift_exchange.THIRD_WHEEL_ERROR
    os.remove('test_family.json')

def test_register_requires_a_name():

    #given
    registration_info = None
    #when
    x = gift_exchange.register(registration_info, 'test_family.json')
    #then
    assert x == gift_exchange.NO_NAME_ERROR
