from support.celery import app
from .service import send


@app.task
def send_spam_email(user_email):
    send(user_email)

# from celery import task
# from django.core.mail import send_mail
# from .models import Contact
#

# @task
# def order_created(order_id):
#     """
#     Задача для отправки уведомления по электронной почте при успешном создании заказа.
#     """
#     order = Order.objects.get(id=order_id)
#     subject = 'Order nr. {}'.format(order_id)
#     message = 'Dear {},\n\nYou have successfully placed an order.\
#                 Your order id is {}.'.format(order.first_name,
#                                              order.id)
#     mail_sent = send_mail(subject,
#                           message,
#                           'admin@myshop.com',
#                           [order.email])
#     return mail_sent
#
# # from celery import Celery
# #
# # app = Celery('tasks', broker='pyamqp://guest@localhost//')
# #
# # @app.task
# # def add(x, y):
# #     return x + y