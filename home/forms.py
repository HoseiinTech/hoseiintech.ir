from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.core.mail import EmailMessage

from home.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username",)


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=300,
        required=True,
        widget=forms.TextInput(attrs={
            "class": "input form-control",
            "id": "nameContact",
            "placeholder": "نام و نام خانوادگی",
            "autocomplete": "on",
            "oninvalid": "setCustomValidity('لطفا نام و نام خانوادگی خود را وارد کنید.')",
            "onkeyup": "setCustomValidity('')"
        }))
    email = forms.EmailField(
        max_length=250,
        required=True,
        widget=forms.EmailInput(attrs={
            "class": "input form-control",
            "id": "emailContact",
            "placeholder": "ایمیل",
            "autocomplete": "on",
            "oninvalid": "setCustomValidity('ایمیل نادرست است.')",
            "onkeyup": "setCustomValidity('')",
        }))
    message = forms.CharField(
        max_length=300,
        required=True,
        widget=forms.Textarea(attrs={
            "class": "textarea form-control",
            "id": "messageContact",
            "placeholder": "پیام ...",
            "rows": "4",
            "oninvalid": "setCustomValidity('لطفا پیام خود را وارد کنید.')",
            "onkeyup": "setCustomValidity('')",
        }))

    def send_email(self):
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        message = self.cleaned_data.get('message')
        EmailMessage(
            f"پیام از طرف {name} (hoseiintech.ir)",  # subject
            f"""
            {message}
            ------------------
            این پیام با ایمیل {email} ارسال شده است.
            """,  # message
            email,  # from email
            ['mahmodian8713@gmail.com'],  # to email
            reply_to=[email],
        ).send()

