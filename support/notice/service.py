from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Ответ о приеме заявки',
        'Ваша заявка принята в работу',
        # 'vania.vanin2021@gmail.com',
        'admin@gmail.com',
        [user_email],
        fail_silently=False,
    )
