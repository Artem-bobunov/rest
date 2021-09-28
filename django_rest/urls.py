from django.urls import path
from django_rest import views
from . import views
from django.urls import path

"""from .api import restViewSet
from rest_fraemwork import routers

router = routers.DefaultRputer()
router.register('restApp/rest/django_rest/',restViewSet,'django_rest')"""

"""urlpatterns = [
    path("rest/django_rest$", views.restApi_list),
    path('rest/django_rest/(?P<pk>[0-9]+)$', views.restApi_detail),
]"""

"""urlpatterns = [
    path("",views.ListTodoAPIView.as_view(),name="todo_list"),
    path("create/", views.CreateTodoAPIView.as_view(),name="todo_create"),
    path("update/<int:pk>/",views.UpdateTodoAPIView.as_view(),name="update_todo"),
    path("delete/<int:pk>/",views.DeleteTodoAPIView.as_view(),name="delete_todo")
]"""
urlpatterns = [
    path('book-list', views.bookList, name='book-list'),
    path('book-create', views.bookCreate, name='book-create'),
    path('book-update/<int:id>', views.bookUpdate, name='book-update'),
    path('book-delete/<int:id>', views.bookDelete, name='book-delete'),

]
