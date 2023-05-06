from django.db import models


class Addresses(models.Model):
    regione = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    quartie = models.CharField(max_length=100)
    code_postal = models.IntegerField()

    def __init__(self, Aregione, Aville, Aquartie, acode_postal):
        self.regione = Aregione
        self.ville = Aville
        self.quartie = Aquartie
        self.code_postal = acode_postal


class Utilisateur(models.Model):
    nomUtilisateur = models.CharField(max_length=100)
    prenomUtilisateur = models.CharField(max_length=100)
    adresseUtilisateur = models.CharField(max_length=100)
    emailUtilisateur = models.CharField(max_length=100)
    motDePass = models.CharField(max_length=100)
    telephoneUtilisateur = models.IntegerField()

    def __init__(self, nom, prenom, adresse, email, mdp, telephone):
        self.nomUtilisateur = nom
        self.prenomUtilisateur = prenom
        self.adresseUtilisateur = adresse
        self.emailUtilisateur = email
        self.motDePass = mdp
        self.telephoneUtilisateur = telephone


class Restaurant(models.Model):
    nomRestaurant = models.CharField(max_length=100)
    adresseRestaurant = models.CharField(max_length=100)
    typeCuisine = models.CharField(max_length=100)

    def __init__(self, nomRestaurant, adresseRestaurant):
        self.nomRestaurant = nomRestaurant
        self.adresseRestaurant = adresseRestaurant


class NoteRestaurant(models.Model):
    idUtilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    idRestaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    note = models.CharField(max_length=100)
    commentaire = models.TextField()

    def __init__(self, idUtilisateur, idRestaurant, note, commentaire):
        self.idUtilisateur = idUtilisateur
        self.idRestaurant = idRestaurant
        self.note = note
        self.commentaire = commentaire
