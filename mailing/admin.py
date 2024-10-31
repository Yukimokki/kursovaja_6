from django.contrib import admin
from mailing.models import Mailing, Mailing_Message, Last_Mailing_Attempt, Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("email", "full_name", "comment")
    list_filter = ("full_name",)
    search_fields = ("email", "full_name")


@admin.register(Mailing_Message)
class Mailing_MessageAdmin(admin.ModelAdmin):
    list_display = ("subject", "body")
    list_filter = ("subject",)
    search_fields = ("subject",)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "start_time", "end_time", "periodicity", "status",)
    list_filter = ("name", "start_time", "end_time",)
    search_fields = ("name",)

@admin.register(Last_Mailing_Attempt)
class Last_Mailing_AttemptAdmin(admin.ModelAdmin):
    list_display = ("mailing", "status", "server_response")
    list_filter = ("status",)
    search_fields = ("mailing", "server_response",)