from django.forms import forms

from .models import Utilisateur, Addresses, Restaurant, NoteRestaurant


class UtilisateurFrom(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['id', 'email']

        def save(self, commit=True):
            user = super(UtilisateurFrom, self).save(commit=False)
            user.emailUtilisateur = self.cleaned_data['email']
            if commit:
                user.save()


class RestaurantFrom(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['Nom Restaurant', 'Adresse Restaurant', 'Type Cuisine']

        def save(self, commit=True):
            restaurant = super(RestaurantFrom, self).save(commit=False)
            Restaurant.nomRestaurant = self.cleaned_data['Nom Restaurant']
            if commit:
                restaurant.save()


class AdressessFrom(forms.ModelForm):
    class Meta:
        model = Addresses
        fields = ['regione', 'quartie', 'code Postal']


class NoteRestaurantForm(forms.Model):
    class Meta:
        model = NoteRestaurant
        fields = ['idUtilisateur', 'idRestaurant', 'note', 'commentaire']
