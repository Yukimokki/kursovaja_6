from django.urls import path, include
from mailing.views import ClientListView

urlpatterns = [
    path("", ClientListView.as_view(), name="Client_list"),
]