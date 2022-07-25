# rsp-backend-service-template

В `main.py` пишем обработчики на услуги:
```python

@worker.method
def some_method(msg: BaseMessage):
    """
    Данная функция будет обрабатывать услугу some_method сервиса rsp-backend-service
    """
    msg.ctx['asddd'] = 123
    print(msg.json())

```

Дефолтное поведение в случае если существует `msg.previous` – отправка контекста в предыдущий сервис-услугу. `msg.ctx` – контекст, который мы можем изменять для того чтоб пробросить данные в сервис-функцию выше или ниже.

Чтоб послать запрос в другой сервис необходимо вызвать функцию `ask`:
```python

@worker.method
def some_method(msg: BaseMessage):
    if msg.ctx['has_needed_data']:
        msg.ctx['данные, которые нужны сервису ниже'] = 'собственно данные'
        
        ask(msg, 'someService', 'some_method')
        return
```
