from django.shortcuts import render
from django.views.generic import ListView

from mailing.models import Client


class ClientListView(ListView):
    model = Client
    template_name = "mailing/client_list.html"
    context_object_name = "client_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for product in context["client_list"]:
            product.active_version = product.versions.filter(is_current=True).first()
        return context
