from django.urls import path
from . import views

app_name = "trucks"
urlpatterns = [
        # path("", views.index, name="index"),
        path("<int:truck_id>/", views.display_truck_info, name="display_truck_info"),
        ]
