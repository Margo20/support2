from django.urls import path
# from .views import test
from .views import ContactView


urlpatterns = [
    path('', ContactView.as_view(), name='contact')
]

# urlpatterns = [
#     path('',test, name='contact')
# ]