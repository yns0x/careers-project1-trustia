from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_produits, name='liste_produits'),
    path('creer/', views.creer_produit, name='creer_produit'),
    path('<int:pk>/modifier/', views.modifier_produit, name='modifier_produit'),
    path('<int:pk>/supprimer/', views.supprimer_produit, name='supprimer_produit'),
]