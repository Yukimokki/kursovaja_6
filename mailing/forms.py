from django.forms import ModelForm, BooleanField
from mailing.models import Mailing


class MailingForm(ModelForm):
    class Meta:
        model = Mailing
        fields = "__all__"