import sender_stand_request
import data

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

#Prueba1

def positive_assert(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
    user_response = sender_stand_request.post_new_user(user_body)
    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1
def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")

#Prueba2

def test_create_user_15_letter_in_first_name_get_success_response():
    positive_assert("Aaaaaaaaaaaaaaa")

#Prueba3

def negative_assert_symbol(first_name):
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)
    message = "Has introducido un nombre de usuario no válido. El nombre solo puede contener letras del alfabeto latino, la longitud debe ser de 2 a 15 caracteres."
    assert user_response.status_code == 400
    assert user_response.json()["message"] == message
    print(user_response.json())
def test_create_user_1_letter_in_first_name_get_error_response():
    negative_assert_symbol("A")

#Prueba4

def test_create_user_16_letter_in_first_name_get_error_response():
    negative_assert_symbol("Aaaaaaaaaaaaaaaa")

#Prueba5

def test_create_user_has_space_in_first_name_get_error_response():
    negative_assert_symbol("A Aaa")

#Prueba6

def test_create_user_has_special_symbol_in_first_name_get_error_response():
    negative_assert_symbol("\"№%@\",")

#Prueba7

def test_create_user_has_number_in_first_name_get_error_response():
    negative_assert_symbol("123")


def negative_assert_no_first_name(user_body):
    response = sender_stand_request.post_new_user(user_body)
    message = "No se han aprobado todos los parámetros requeridos"
    assert response.status_code == 400
    assert response.json()["message"] == message
    print(response.json())

#Prueba8

def test_create_user_no_first_name_get_error_response():
    user_body = data.user_body.copy()
    user_body.pop("firstName")
    negative_assert_no_first_name(user_body)


#Prueba9

def test_create_user_empty_first_name_get_error_response():
    user_body = get_user_body("")
    negative_assert_no_first_name(user_body)

#Prueba10

def test_create_user_number_type_first_name_get_error_response():
    user_body = get_user_body(12)
    response = sender_stand_request.post_new_user(user_body)
    assert response.status_code == 400
    