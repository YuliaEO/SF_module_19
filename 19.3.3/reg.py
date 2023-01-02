import json

import 

status = 'available'

res_get = requests.get(f'https://petstore.swagger.io/v2/pet/findByStatus', params={'status': 'available'},
                       =={'accept': 'application/json'})

if 'application/json' in .headers['Content-Type']:
    res_get.json()
else:
    res_get.text

print(f'Статус ответа от сервера на GET запрос: {res_get.status_code}')

= = {
    "id": 0,
    "category": {
        "id": 0,
        "name": "string"
    },
    "name": "doggie",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 0,
            "name": "string"
        }
    ],
    "status": "available"
}

= = {'accept': 'application/json', 'Content-Type': 'application/json'}
res_post_addNewPet = requests.post(f'https://petstore.swagger.io/v2/pet', data=json.dumps(info_pet, ensure_ascii=False),
                                   headers 1=header1)

print(f'Статус ответа от сервера на POST запрос добавление питомца: {res_post_addNewPet.status_code}')
print('Карточка питомца:')
print(res_post_addNewPet.json())



= = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "valenok"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
= = {'accept': 'application/json', 'Content-Type': 'application/json'}
res_put_UpdatedUser = requests.put(f'https://petstore.swagger.io/v2/pet', data=json.dumps(info_new, ensure_ascii=False),
                                   headers 1=header1)
print(f'Статус ответа от сервера на PUT запрос изменение питомца: {res_put_UpdatedUser.status_code}')
print('Карточка питомца:')
print(res_put_UpdatedUser.json())

info_new_pet2 = res_put_UpdatedUser.json()
id_pet = info_new_pet2.get("id")


= = {'accept': 'application/json'}
res_del_DelNewPet = requests.delete(f'https://petstore.swagger.io/v2/pet/{id_pet}', headers=header3)

print(f'Статус ответа от сервера на DEL запрос удаление питомца: {res_del_DelNewPet.status_code}')
