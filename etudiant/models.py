from django.db import models

# Create your models here.
	
class Etudiant(models.Model):	
    METIERS = [('APD' , 'APD'),('DBE' ,'DBE'),('ABD' ,('ABD'))]

    nom	=	models.CharField(max_length=200)	

    prenom	=	models.CharField(max_length=200)

    age = models.PositiveIntegerField()

    est_inscrit = models.BooleanField()

    metiers =   models.CharField(max_length=20,choices=METIERS)

    created_at	=	models.DateTimeField(auto_now_add=True)	
    
    def __str__(self):	
	
         return	f"{self.nom} {self.prenom}"

# Create your models here.
