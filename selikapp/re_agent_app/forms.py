from django import forms

from .constants import (
    PROPERTY_STATUS_CHOICES,
    TRANSACTION_TYPE_CHOICES,
    MANDATS_STATUS_CHOICES,
    PROPERTY_TYPE_CHOICES,
)

from .models import Property, Contact, BienImage, Negociator, City
from .widgets import MultipleFileInput


class BienImageForm(forms.Form):
    bien_image = forms.FileField(
        widget=MultipleFileInput(attrs={"class": "form-control", "multiple": True}),
        required=False
    )


class BienForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = "__all__"  # include everything

        widgets = {
            # General Information
            "bien_type_tansaction": forms.Select(attrs={"class": "form-select"}),
            "bien_type": forms.Select(attrs={"class": "form-select"}),
            "bien_info_complémentaire": forms.Select(attrs={"class": "form-select"}),

            "bien_surface": forms.NumberInput(attrs={"class": "form-control"}),
            "bien_surface_terrain": forms.NumberInput(attrs={"class": "form-control"}),

            "bien_négociateur": forms.Select(attrs={"class": "form-select"}),
            "bien_status": forms.Select(attrs={"class": "form-select"}),

            "bien_titre": forms.TextInput(attrs={"class": "form-control"}),
            "bien_numéro_clé": forms.TextInput(attrs={"class": "form-control"}),
            "bien_diffusé": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "bien_description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),

            # Financial
            "bien_prix_hors_honoraires": forms.NumberInput(attrs={"class": "form-control"}),
            "bien_honoraires": forms.NumberInput(attrs={"class": "form-control"}),
            "bien_taux_commision": forms.NumberInput(attrs={"class": "form-control"}),
            "bien_prix": forms.NumberInput(attrs={"class": "form-control"}),
            "bien_charge_honoraire": forms.Select(attrs={"class": "form-select"}),

            "bien_taxe_foncière": forms.NumberInput(attrs={"class": "form-control"}),
            "bien_taxe_habitation": forms.NumberInput(attrs={"class": "form-control"}),
            "bien_charge_mensuelle": forms.NumberInput(attrs={"class": "form-control"}),

            # Contacts & Localisation
            "bien_contacts": forms.SelectMultiple(attrs={"class": "form-select"}),
            "bien_adresse": forms.TextInput(attrs={"class": "form-control"}),
            "bien_complement_adresse": forms.TextInput(attrs={"class": "form-control"}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

        widgets = {
            # Base Info
            "contact_type": forms.Select(attrs={"class": "form-select"}),
            "contact_first_name": forms.TextInput(attrs={"class": "form-control"}),
            "contact_name": forms.TextInput(attrs={"class": "form-control"}),

            "contact_nego": forms.Select(attrs={"class": "form-select"}),
            "contact_email": forms.EmailInput(attrs={"class": "form-control"}),
            "contact_telephone": forms.TextInput(attrs={"class": "form-control"}),
            "contact_status": forms.Select(attrs={"class": "form-select"}),

            "contact_adress": forms.TextInput(attrs={"class": "form-control"}),
            "contact_complement_adress": forms.TextInput(attrs={"class": "form-control"}),

            "contact_commentar": forms.Textarea(attrs={"class": "form-control", "rows": 4}),

            # Criteria
            "contact_cr_type_search": forms.Select(attrs={"class": "form-select"}),
            "contact_cr_type_estatse": forms.Select(attrs={"class": "form-select"}),

            "contact_cr_budget": forms.NumberInput(attrs={"class": "form-control"}),
            "contact_cr_room_number": forms.NumberInput(attrs={"class": "form-control"}),
            "contact_cr_bedroom_number": forms.NumberInput(attrs={"class": "form-control"}),
            "contact_cr_surface": forms.NumberInput(attrs={"class": "form-control"}),
            "contact_cr_surface_terrain": forms.NumberInput(attrs={"class": "form-control"}),
        }


class Filtering_1(forms.Form):
    negociators = forms.ModelMultipleChoiceField(
        queryset=Negociator.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Négociateurs",
        required=False
    )
    property_status = forms.ChoiceField(
        choices=PROPERTY_STATUS_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Statut bien",
        initial='actif',
    )
    mandat = forms.MultipleChoiceField(
        choices=MANDATS_STATUS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Mandats",
        initial='en_cours',
    )
    transaction_type = forms.ChoiceField(
        choices=TRANSACTION_TYPE_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Type de transaction",
    )
    property_type = forms.MultipleChoiceField(
        choices=PROPERTY_TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Type ",
    )
    city = forms.ModelMultipleChoiceField(
        queryset=City.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Villes",
        required=False
    )
    price_min = forms.DecimalField()
    price_max = forms.DecimalField()
    number_room_min = forms.IntegerField()
    number_room_max = forms.IntegerField()
    number_bedroom_min = forms.IntegerField()
    number_bedroom_max = forms.IntegerField()
    surface_min = forms.FloatField()
    surface_max = forms.FloatField()
    surface_terrain_min = forms.FloatField()
    surface_terrain_max = forms.FloatField()





