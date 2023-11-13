from django.urls import path

from budget_management.categories.views import CategoryListView

urlpatterns = [
    path("", CategoryListView.as_view(), name="category_list"),
]
