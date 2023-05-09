from django.urls import path,include
from . import views
from .views import CategoryAPIView,ProductViewset
from rest_framework import routers
router = routers.SimpleRouter()
router.register('produit', ProductViewset, basename='produit')
urlpatterns = [
    path('', views.index,name='index'),
    path('listeCat/<int:id>',views.listeProduitCategorie,name='listeCat'),
    path('descArt/<int:id>',views.descriptionArt,name='description'),
    path('listeFournisseur',views.fournisseur,name='listeFour'),
    path('ajoutProd',views.ajoutProd,name='ajoutProduit'),
    path('register/',views.register, name = 'register'),
    path('api/category/', CategoryAPIView.as_view()),
    # path('api/produits', include(router.urls)),
]