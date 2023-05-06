from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *


def homePage(request):
    return render(request, 'R_Restaurants-master/RestaurantApp/RestaurantApplication/templates/dist/index.html')


# les fonctions CRUD pour toutes les classes
def get_utilisateur_list(request):
    user_list = Utilisateur.objects.all()
    return render(request, '', {'user_list': user_list})


def create_utilisateur(request):
    if request.method == 'Post':
        form = UtilisateurFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_utilisateur_list')
    else:
        form = UtilisateurFrom()
    return render(request, '', {'from': form})


def update_utilisateur(request, pk):
    utilisateur = get_object_or_404(Utilisateur, pk=pk)
    if request.method == 'POST':
        form = UtilisateurFrom(request.POST, instance=utilisateur)
        if form.is_valid():
            form.save()
            return redirect('listUser')
    else:
        form = UtilisateurFrom(instance=utilisateur)
    return render(request, '', {'form': form, 'utilisateur': utilisateur})


def delete_utilisateur(request, pk):
    utilisateur = get_object_or_404(Utilisateur, pk=pk)
    utilisateur.delete()

    return redirect('')


def utilisateur_login(request):
    if request.method == 'POST':
        emailUtilisateur = request.POST['emailUtilisateur']
        motDePass = request.POST['motDePass']
        user = authenticate(request, emailUtilisateur=emailUtilisateur, motDePass=motDePass)
        if user is not None:
            login(request, user)
            return redirect('')
        else:

            return render(request, '', {'Erreur': 'le mot de pass ou adress Email incorrect'})
    else:
        return render(request, '')


def utilisateur_register(request):
    if request.method == 'POST':
        form = UtilisateurFrom(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UtilisateurFrom()
        ## page d'utilisateur
    return render(request, '', {'form': form})


# Restaurant
# fonction de reccherche par ville
def ChercherParVille(request):
    if request.method == 'POST':
        chercher = request.POST['nomRestaurant']
        restaurant = Restaurant.objects.filter(name__icontains=chercher)
        return render(request, '', {'Restaurant': restaurant, 'search': chercher})
    return render(request, '')


# fonction de reccherche par type de cuisine
def ChercherParCuisine(request):
    if request.method == 'POST':
        chercher = request.POST['typeCuisine']
        restaurant = Restaurant.objects.filter(name__icontains=chercher)
        return render(request, '', {'Restaurant': restaurant, 'chercher': chercher})
    return render(request, '')


def listRestaurant(request):
    d = Restaurant.objects.all()

    return render(request, '', {'data': d})


def create_Restaurant(request):
    if request.method == 'Post':
        form = RestaurantFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listRestaurant')
    else:
        form = RestaurantFrom()
    return render(request, '', {'from': form})


def update_Restaurant(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = Restaurant(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('listRestaurant')
    else:
        form = RestaurantFrom(instance=restaurant)
    return render(request, '', {'form': form, 'restaurant': restaurant})


def delete_Restaurant(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    restaurant.delete()

    return redirect('')


# Adresse

def listAddress(request):
    for i in range(10):
        a = Addresses(None)
        a.save()
    d = Addresses.objects.all()
    return render(request, '', {'data': d})


def create_Address(request):
    if request.method == 'Post':
        form = AdressessFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = AdressessFrom()
    return render(request, '', {'from': form})


def update_Address(request, pk):
    adress = get_object_or_404(Addresses, pk=pk)
    if request.method == 'POST':
        form = AdressessFrom(request.POST, instance=adress)
        if form.is_valid():
            form.save()
            return redirect('listAdress')
    else:
        form = AdressessFrom(instance=adress)
    return render(request, '', {'form': form, 'adress': adress})


def delete_Address(request, pk):
    adress = get_object_or_404(Restaurant, pk=pk)
    adress.delete()

    return redirect('')


def create_note_restaurant(id_utilisateur, id_restaurant, note, commentaire):
    note_restaurant = NoteRestaurant.objects.create(
        idUtilisateur=id_utilisateur,
        idRestaurant=id_restaurant,
        note=note,
        commentaire=commentaire
    )
    return note_restaurant


def get_note_restaurant(note_restaurant_id):
    note_restaurant = get_object_or_404(NoteRestaurant, pk=note_restaurant_id)
    return note_restaurant


def update_note_restaurant(note_restaurant_id, id_utilisateur=None, id_restaurant=None, note=None, commentaire=None):
    note_restaurant = get_object_or_404(NoteRestaurant, pk=note_restaurant_id)
    if id_utilisateur:
        note_restaurant.idUtilisateur = id_utilisateur
    if id_restaurant:
        note_restaurant.idRestaurant = id_restaurant
    if note:
        note_restaurant.note = note
    if commentaire:
        note_restaurant.commentaire = commentaire
    note_restaurant.save()
    return note_restaurant


def delete_note_rcestaurant(note_restaurant_id):
    note_restaurant = get_object_or_404(NoteRestaurant, pk=note_restaurant_id)
    note_restaurant.delete()
