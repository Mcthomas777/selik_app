from django.contrib import admin
from .models import Property, Contact, Mandat, Visite, ActionCommerciale, ChangeLog


@admin.register(Property)
class BienAdmin(admin.ModelAdmin):

    list_display = (
        "bien_titre",
        "bien_type_tansaction",
        "bien_type",
        "bien_surface",
        "bien_prix",
        "bien_status",
        "bien_diffusé",
        "bien_négociateur",
    )

    list_filter = (
        "bien_type_tansaction",
        "bien_type",
        "bien_info_complémentaire",
        "bien_status",
        "bien_diffusé",
        "bien_charge_honoraire",
        "bien_négociateur",
    )

    search_fields = (
        "bien_titre",
        "bien_numéro_clé",
        "bien_adresse",
        "bien_complement_adresse",
    )

    autocomplete_fields = ("bien_négociateur", "bien_contacts")

    ordering = ("-bien_prix",)

    filter_horizontal = ("bien_contacts",)

    fieldsets = (
        ("Informations Générales", {
            "fields": (
                ("bien_type_tansaction", "bien_type"),
                ("bien_info_complémentaire", "bien_status"),
                "bien_titre",
                "bien_description",
                ("bien_surface", "bien_surface_terrain"),
                ("bien_négociateur", "bien_diffusé"),
                "bien_numéro_clé",
            )
        }),

        ("Informations Financières", {
            "fields": (
                ("bien_prix_hors_honoraires", "bien_honoraires"),
                ("bien_taux_commision", "bien_prix"),
                ("bien_charge_honoraire",),
                ("bien_taxe_foncière", "bien_taxe_habitation"),
                "bien_charge_mensuelle",
            )
        }),

        ("Localisation & Contacts", {
            "fields": (
                "bien_adresse",
                "bien_complement_adresse",
                "bien_contacts",
            )
        }),
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "contact_name",
        "contact_first_name",
        "contact_type",
        "contact_email",
        "contact_telephone",
        "contact_status",
        "contact_created_at",
    )
    
    list_filter = (
        "contact_type",
        "contact_status",
        "contact_cr_type_search",
        "contact_cr_type_estatse",
        "contact_nego",
    )

    search_fields = (
        "contact_name",
        "contact_first_name",
        "contact_email",
        "contact_telephone",
    )

    ordering = ("-contact_created_at",)

    fieldsets = (
        ("Identité du contact", {
            "fields": (
                "contact_type",
                ("contact_first_name", "contact_name"),
                "contact_nego",
                "contact_status",
            )
        }),
        ("Coordonnées", {
            "fields": (
                "contact_email",
                "contact_telephone",
                "contact_adress",
                "contact_complement_adress",
            )
        }),
        ("Informations complémentaires", {
            "fields": ("contact_commentar",)
        }),
        ("Critères de recherche", {
            "fields": (
                "contact_cr_type_search",
                "contact_cr_type_estatse",
                "contact_cr_budget",
                "contact_cr_room_number",
                "contact_cr_bedroom_number",
                "contact_cr_surface",
                "contact_cr_surface_terrain",
            )
        }),
    )


@admin.register(Mandat)
class MandatAdmin(admin.ModelAdmin):
    list_display = ('reference', 'client', 'date_start', 'created_at')

@admin.register(Visite)
class VisiteAdmin(admin.ModelAdmin):
    list_display = ('bien', 'date', 'visiteur')

@admin.register(ActionCommerciale)
class ActionCommercialeAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date', 'bien')

@admin.register(ChangeLog)
class ChangeLogAdmin(admin.ModelAdmin):
    list_display = ('object_type', 'object_id', 'action', 'user', 'timestamp')
    readonly_fields = ('object_type', 'object_id', 'action', 'user', 'changes', 'timestamp')
