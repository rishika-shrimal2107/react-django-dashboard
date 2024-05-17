from django.urls import path
from . import views
urlpatterns = [
     path('persons/',views.PersonList.as_view()),
    path('persons/birth_count_month/<int:month>/', views.BirthCountMonthList.as_view(), name='birth-count-month-list'),
    path('male-persons/', views.MalePersonList.as_view(), name='male-persons'),
    path('female-persons/', views.FemalePersonList.as_view(), name='female-persons'),
]
