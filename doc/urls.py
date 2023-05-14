from django.urls import path
from .views import MyModelListCreateView, MyModelRetrieveUpdateDeleteView, MyModelListView

urlpatterns = [
    path('document/', MyModelListCreateView.as_view(), name='mymodel-list-create'),
    path('document/list', MyModelListView.as_view(), name='mymodel-list'),
    path('document/<int:id>', MyModelRetrieveUpdateDeleteView.as_view(), name='mymodel-retrieve-update-delete'),
]