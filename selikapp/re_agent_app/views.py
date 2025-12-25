from django.shortcuts import render, redirect

from .models import Property, Mandat, Visite, ActionCommerciale, ChangeLog, BienImage
from .forms import BienForm, ContactForm, BienImageForm


def index(request):
    latest_biens = Property.objects.order_by('-bien_created_at')[:3]
    derniers_mandats = Mandat.objects.order_by('-created_at')[:5]
    dernieres_visites = Visite.objects.order_by('-created_at')[:5]
    dernieres_actions = ActionCommerciale.objects.order_by('-created_at')[:5]
    changelog = ChangeLog.objects.all()[:20]

    query = request.GET.get('q', '')
    if query:
        # basic search across title and address
        latest_biens = Property.objects.filter(
            # models.Q(titre__icontains=query) | models.Q(adresse__icontains=query)
        ).order_by('-property_created_at')[:10]

    context = {
        'latest_biens': latest_biens,
        'derniers_mandats': derniers_mandats,
        'dernieres_visites': dernieres_visites,
        'dernieres_actions': dernieres_actions,
        'changelog': changelog,
        'search_query': query,
    }
    return render(request, 're_agent_app/index.html', context)

def add_estate(request):
    if request.method == "POST":
        form = BienForm(request.POST)
        image_form = BienImageForm(request.POST, request.FILES)

        if form.is_valid():
            bien = form.save()

            files = request.FILES.getlist("bien_image")

            for idx, file in enumerate(files):
                BienImage.objects.create(
                    bien_parent=bien,
                    bien_image=file,
                    bien_image_vitrine=(idx == 0)  # First image = vitrine
                )

            return redirect("bien_detail", pk=bien.pk)

    else:
        form = BienForm()
        image_form = BienImageForm()

    return render(request, "re_agent_app/forms/bien_form.html", {
        "form": form,
        "image_form": image_form,
    })

def add_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect("contact_detail", pk=contact.pk)  # you must have a detail view
    else:
        form = ContactForm()

    return render(request, "re_agent_app/forms/contact_form.html", {"form": form})
