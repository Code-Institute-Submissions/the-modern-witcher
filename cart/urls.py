from django.urls import path
from .views import view_cart, add_to_cart, amend_cart, view_payment, view_confirm

urlpatterns = [
    path('', view_cart, name="view_cart"),
    path('add_to_cart/<int:id>', add_to_cart, name="add_to_cart"),
    path('amend_cart/<int:id>', amend_cart, name="amend_cart"),
    path('payment/', view_payment, name="view_payment"),
    path('confirm/', view_confirm, name="view_confirm")
]
