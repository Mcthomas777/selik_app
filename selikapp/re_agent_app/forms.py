from django import forms
from .models import Bien, Contact

class BienForm(forms.ModelForm):
    class Meta:
        model = Bien
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
