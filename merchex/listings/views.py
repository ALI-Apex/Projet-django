from django.shortcuts import render
from listings.models import Band, Listing
from django.core.mail import send_mail
from django.shortcuts import redirect
from listings.forms import BandForm, ContactUsForm, ListingForm


def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", {"bands": bands})


def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, "listings/band_detail.html", {"band": band})


def band_create(request):
    if request.method == "POST":
        form = BandForm(request.POST)
        if form.is_valid():
            # crée une nouvelle band et la sauvegarder dans la BD
            band = form.save()
            """
                redirige vers la page de detail du groupe que
                nous venons de creer.
                Nous pouvons fournir les arguments du motif url
                comme arguments à la fonction de redirection
            """
            return redirect("band-detail", band.id)
    else:
        form = BandForm()

    return render(request, "listings/band_create.html", {"form": form})


def bands_update(request, id):
    # On recupère l'objet correspondand à l'ID
    band = Band.objects.get(id=id)

    if request.method == "POST":
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            band = form.save()
            # redirection
            return redirect("band-detail", band.id)
    else:
        # On creer  un formulaire dejà rempli avec l'objet recuperer
        form = BandForm(instance=band)
    # on retourne le rendu
    return render(request, "listings/bands_update.html", {"form": form})


def bands_delete(request, id):
    band = Band.objects.get(id=id)

    if request.method == "POST":
        # supprimer le groupe de la base de données
        band.delete()
        # redirection vers la liste de groupe pour confirmation de la suppression
        return redirect("band-list")
    return render(request, "listings/bands_delete.html", {"band": band})


def about(request):
    return render(request, "listings/about.html")


def listings_list(request):
    listings = Listing.objects.all()
    return render(request, "listings/listings_list.html", {"listings": listings})


def listings_detail(request, id):
    listing = Listing.objects.get(id=id)
    return render(request, "listings/listings_detail.html", {"listing": listing})


def Create_new_listing(request):
    # Si la methode de la requete est POST :
    if request.method == "POST":
        # On crer un formulaire remplie avec les valeures précedemment remplies
        form = ListingForm(request.POST)

        # Si le formulaire est valid :
        if form.is_valid():
            # On enregistre les données dans notre base de donnée
            listing = form.save()

            # on redirige vers une nouvelle page ici la page listing-detail
            return redirect("listing-detail", listing.id)
    # Sinon la methode de la requete est GET
    else:
        # On creer un formulaire vide
        form = ListingForm()

        # On retourne la page Create_new_listing
        return render(request, "listings/Create_new_listing.html", {"form": form})


def listings_update(request, id):
    # On recupère l'objet correspondand à l'ID
    listing = Listing.objects.get(id=id)

    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # redirection
            return redirect("listing-detail", listing.id)
    else:
        # On creer  un formulaire dejà rempli avec l'objet recuperer
        form = ListingForm(instance=listing)
    # on retourne le rendu
    return render(request, "listings/listings_update.html", {"form": form})


def listings_delete(request, id):
    listing = Listing.objects.get(id=id)

    if request.method == "POST":
        # supprimer le groupe de la base de données
        listing.delete()
        # redirection vers la liste de groupe pour confirmation de la suppression
        return redirect("listing-list")
    return render(request, "listings/listings_delete.html", {"listing": listing})


def contact(request):
    if request.method == "POST":
        # crées une instance de notre formulaire et le remplir avec des données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f"Message from {form.cleaned_data['name'] or 'anonyme'} via Merchex Contact Us Form",
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=["admin@merchex.xyz"],
            )
            return redirect("contact")

    else:
        # ceci doit etre une requete get donc crée un formulaire vide
        form = ContactUsForm()  # ajout d'un nouveau formulaire

    return render(
        request, "listings/contact.html", {"form": form}
    )  # passe ce formulaire au gabarit
