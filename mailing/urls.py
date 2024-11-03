from django.urls import path, include
from mailing.apps import MailingConfig
from mailing.views import ClientListView, MailingListView, MailingDetailView, MailingUpdateView, MailingDeleteView, \
    MailingCreateView

app_name = MailingConfig.name

urlpatterns = [
    path("", ClientListView.as_view(), name="Client_list"),
    path("list_mailings/", MailingListView.as_view(), name="Mailing_list"),
    path('mailing/<int:pk>', MailingDetailView.as_view(), name='Mailing_detail'),
    path('mailing/create', MailingCreateView.as_view(), name='Mailing_create'),
    path('mailing/<int:pk>/update', MailingUpdateView.as_view(), name='Mailing_update'),
    path('mailing/<int:pk>/delete', MailingDeleteView.as_view(), name='Mailing_delete'),
]