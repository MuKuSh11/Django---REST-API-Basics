from django.urls import path
from .views import overview
from .views import add_data
from .views import modify_data
from .views import patch_data
from .views import get_all
from .views import delete_data

urlpatterns = [
    path('', overview, name="overview"),
    path('add/', add_data, name="addData"),
    path('modify/<int:id>', modify_data, name="modifyData"),
    path('patch/<int:id>', patch_data, name="patchData"),
    path('all/', get_all, name="getAll"),
    path('delete/<int:id>', delete_data, name="deleteData"),
]