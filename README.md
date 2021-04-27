# ToDo list

### Description:

    Простой ToDo List - можно заносить новые дела, помечать выполненные, искать по описанию

    Взаимодействие с сервисом происходит через понятный (надеюсь) интерфейс

    Список хранится в SQLite в оперативной памяти (лол)



### Create venv:
    make venv

### Run tests:
    make test
    
### Run linters:
    make lint
    
### Run formatters:
    make format
    
### Run Server:
    make up
    OR 
    FLASK_APP=todo_list/app.py flask run 
