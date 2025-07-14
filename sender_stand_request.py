import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

'''
response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())
'''

def get_users_table():
    response = requests.get(configuration.URL_SERVICE + configuration.GET_USER_LIST_PATH,
                         # inserta la dirección URL completa
                         json= {},   # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados
    print(str(response.text))
    return response

print(get_users_table())

