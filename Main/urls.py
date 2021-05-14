from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^DB_(?P<table_name>[\w]+)", views.db_form),
    url("^", views.home)
]
