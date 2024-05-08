from typing import Any

from django import forms
from django.forms import ValidationError

from . import models


class ContactForm(forms.ModelForm):

    class Meta:
        model = models.Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category',
        )
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name here'
                }
            ),
        }

    def clean(self) -> dict[str, Any]:
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            self.add_error(
                'last_name',
                ValidationError(
                    'O primeiro nome não pode ser igual ao último nome',
                    code='invalid_names'
                )
            )

        return super().clean()

    def clean_first_name(self) -> str:
        first_name = self.cleaned_data['first_name']

        if len(first_name) < 3:
            self.add_error(
                'first_name',
                ValidationError(
                    'O nome deve ter pelo menos 3 letras',
                    code='invalid_name'
                )
            )

        return first_name
