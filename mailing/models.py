from django.db import models
from django.db.models.functions import Concat

NULLABLE = {"blank": True, "null": True}

class Client(models.Model):
    email = models.EmailField(verbose_name="email", unique=True, help_text="your email address",)
    #first_name = models.CharField(max_length=50, verbose_name="client's first name", help_text="First name")
    #family_name = models.CharField(max_length=50, verbose_name="client's family name", help_text="Last name")
    #other_names = models.CharField(max_length=50, verbose_name="client's other names", help_text="other names if any")
    full_name = models.CharField(max_length=200, verbose_name="client's full name", help_text="Full name")
    comment = models.TextField(max_length=100, help_text="leave oyur comment here")

    class Meta:
        #full_name = ('first_name', 'family_name', 'other_names')
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return f"{self.email}, {self.full_name}: {self.comment}"

class Mailing_Message(models.Model):
    subject = models.CharField(max_length=100, verbose_name="Тема письма")
    body = models.TextField(verbose_name="Текст письма")

    def __str__(self):
        return f"{self.subject}, {self.body}"

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"


class Mailing(models.Model):
    STATUS_CHOICES = [
        ("created", "Created"),
        ("active", "active"),
        ("completed", "completed"),
    ]
    PERIODICITY_CHOICES = [
        ("daily", "Once a day"),
        ("weekly", "once a week"),
        ("monthly", "Once a month"),
    ]

    TYPE_CHOICES = [
        ("short_list", "only headers"),
        ("long_list", "headers and brief summary"),
        ("long_read", "full text in the mailing"),
    ]

    name = models.TextField(verbose_name="mailing name", **NULLABLE)
    type = models.TextField(verbose_name="mailing type", choices=TYPE_CHOICES, **NULLABLE)

    message = models.ForeignKey(Mailing_Message, on_delete=models.CASCADE, verbose_name="Message")
    client = models.ManyToManyField(Client, verbose_name="Clients")

    start_time = models.DateTimeField(verbose_name="Start of the mailing")
    end_time = models.DateTimeField(verbose_name="End of the mailing", **NULLABLE)

    periodicity = models.CharField(max_length=10, choices=PERIODICITY_CHOICES, verbose_name="How often")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name="Status")

    def __str__(self):
        return f"mailing: {self.name}, {self.status}"

    class Meta:
        verbose_name = "Mailing"
        verbose_name_plural = "Mailings"


class Last_Mailing_Attempt(models.Model):
    STATUS_CHOICES = [
        ("Not_Attempted", "Not sent yet"),
        ("Success", "Successful attempt"),
        ("failed", "Attempt failed"),
    ]

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name="Mailing")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name="Sent Status")
    server_response = models.TextField(verbose_name="Server response", **NULLABLE)

    def __str__(self):
        return f"Mailing attempt {self.id} for mailing {self.mailing.name}"

    class Meta:
        verbose_name = "Mailing status"
        verbose_name_plural = "Mailings status"

