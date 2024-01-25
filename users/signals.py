from django.dispatch import receiver
from django.db.models.signals import post_save
from users.models import CustomUser
from django.core.mail import send_mail

@receiver(post_save, sender=CustomUser)
def send_welcome_message(sender, instance, created, **kwargs):
    if created:
        send_mail(
                "Welcome to Goodreads Clone , created by Saidkodirov",
                f"Hi , {instance.username}. Welcome to Goodreads Clone. Enjoy the books and reviews.",
                "stolibjon123@gmail.com",
                [instance.email]
                )   