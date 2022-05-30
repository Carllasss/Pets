# Pets-API

Endpoint | Parameters
------------ | -------------
GET /pets |**query parameters:** <br> *limit*: integer(optional, default=0) <br> *offset*: integer(optional, default=20) <br> *has_photos*: boolean(optional) *in progress*
DELETE /pets |**request body** <br> "ids": [list of ids]
POST /pets | *name*: str(required) <br> *type*: str(required) <br> *age*: integer(optional, default=20)
POST /pets/{id}/photo | **form data** <br> file: binary

### Развертывание на docker
Для развертывания используйте: `docker-compose -f docker-compose.yml up`

### Тесты
Для тестирования используйте: 'manage.py test'

### CLI
Выгружает список питомцев в *stdout* в *JSON* формате
Пример: `python manage.py get --has_photos=False`
Необязательный параметр: *has_photos: boolean*

### Версии
*Docker version 20.10.14*

*docker-compose version 2.4.1*

*Python 3.10.2*


