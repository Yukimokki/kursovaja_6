from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailing.forms import MailingForm
from mailing.models import Client, Mailing


def home(request):
    mailings = Mailing.objects.all()
    context = {"mailings": mailings}
    return render(request, "mailing/home.html", context)


class ClientListView(ListView):
    model = Client
    template_name = "mailing/client_list.html"
    context_object_name = "client_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MailingListView(ListView):
    model = Mailing
    template_name = "mailing/mailing_list.html"


class MailingDetailView(DetailView):
    model = Mailing
    template_name = "mailing/Mailing_detail.html"


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:Mailing_list")


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:Mailing_list")


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy("mailing:Mailing_list")
