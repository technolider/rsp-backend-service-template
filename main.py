from dotenv import load_dotenv

load_dotenv()

from worker_init import worker

from src.base_message import BaseMessage


@worker.method
def some_method(msg: BaseMessage):
    """
    Данная функция будет обрабатывать услугу some_method сервиса rsp-backend-service
    """
    msg.ctx['asddd'] = 123
    print(msg.json())  # ask(msg, 'someService', 'some_method')


if __name__ == '__main__':
    worker.run()
