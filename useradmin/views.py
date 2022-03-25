from django.shortcuts import render

from allauth.account.views import LoginView, PasswordChangeView
from allauth.exceptions import ImmediateHttpResponse
from allauth.account.adapter import get_adapter
from allauth.account import signals

from useradmin.models import Login



class BeautysenLoginView(LoginView):
    # Login view extended to have the user connexion informations

    def form_valid(self, form):
        success_url = self.get_success_url()

        try:
            new_login = Login(email=form.cleaned_data['login'])
            new_login.save()
            return form.login(self.request, redirect_url=success_url)
        except ImmediateHttpResponse as e:
            return e.response

beautysen_login_view = BeautysenLoginView.as_view()
