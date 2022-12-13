from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import TypeEducationViewSet, UsersViewSet, FacultiesViewSet, ProfileEducationViewSet, DataViewSet
app_name = 'api_v1'

v1_router = DefaultRouter()
v1_router.register(r'users', UsersViewSet, basename='api-v1-users')
v1_router.register('type', TypeEducationViewSet, basename='api-v1-type')
v1_router.register(r'faculties/(?P<type_pk>\d+)', FacultiesViewSet, basename='faculties')
v1_router.register(r'profiles/(?P<type_pk>\d+)/(?P<facultie_pk>\d+)', ProfileEducationViewSet, basename='profiles')
v1_router.register(r'descriptions/(?P<type_pk>\d+)/(?P<facultie_pk>\d+)/(?P<profile_pk>\d+)', DataViewSet, basename='descriptions')

urlpatterns = [
     path('v1/', include(v1_router.urls)),
]
