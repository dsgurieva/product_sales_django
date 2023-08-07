from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import CatalogListView, ContactsFormView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CatalogListView.as_view(), name='home'),
    path('contacts/', ContactsFormView.as_view(), name='contacts'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('create/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
]

