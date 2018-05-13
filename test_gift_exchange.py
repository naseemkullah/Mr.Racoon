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

def test_register_can_create_a_non_existing_registration_file():
    #given
    try:
        os.remove('test_family.json')
    except OSError:
        pass
    registration_info = ('Dirk Bogarde', None)

    #when
    x = gift_exchange.register(registration_info, 'test_family.json')

    #then
    assert 'Dirk Bogarde' in open('test_family.json').read()
    os.remove('test_family.json')

def test_register_cannot_input_partner_who_has_inputted_someone_else():
    #given
    data = {"bob": "suzy", "suzy": "bob", "Wilma": "Fred"}
    with open('test_family.json', 'w') as f:
        gift_exchange.json.dump(data, f)
    registration_info = ('Dirk Bogarde', 'Wilma')

    #when
    x = gift_exchange.register(registration_info, 'test_family.json')

    #then
    assert x == gift_exchange.RELATIONSHIP_ERROR

def test_register_cannot_claim_to_be_single_if_you_are_partner_of_someone():
    #given
    data = {"bob": "suzy", "suzy": "bob", "Wilma": "Fred"}
    with open('test_family.json', 'w') as f:
        gift_exchange.json.dump(data, f)
    registration_info = ('Fred', None)

    #when
    x = gift_exchange.register(registration_info, 'test_family.json')

    #then
    assert x == gift_exchange.RELATIONSHIP_ERROR

def test_register_cannot_input_partner_a_if_you_are_partner_of_someone_b():
    #given
    data = {"bob": "suzy", "suzy": "bob", "Wilma": "Fred"}
    with open('test_family.json', 'w') as f:
        gift_exchange.json.dump(data, f)
    registration_info = ('Fred', 'Cassandra')

    #when
    x = gift_exchange.register(registration_info, 'test_family.json')

    #then
    assert x == gift_exchange.RELATIONSHIP_ERROR

def test_register_user_registration_is_added_to_an_existing_registration_file():
    #given
    data = {"bob": "suzy", "suzy": "bob", "Wilma": "Fred"}
    with open('test_family.json', 'w') as f:
        gift_exchange.json.dump(data, f)
    registration_info = ('Dirk Bogarde', None)

    #when
    x = gift_exchange.register(registration_info, 'test_family.json')

    #then
    assert 'Dirk Bogarde' in open('test_family.json').read()
    assert 'suzy' in open('test_family.json').read()
    os.remove('test_family.json')

