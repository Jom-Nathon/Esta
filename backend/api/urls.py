from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name =  'api'

router = DefaultRouter()
router.register(r'plot', views.PlotViewSet, basename='plot')
# router.register('notes/', views.NoteListCreate, basename='node-list')
# router.register('notes/delete/<int:pk>/', views.NoteDelete, basename='delete_note')
router.register(r'plotcase', views.PlotCaseViewSet, basename='plotcase')
router.register(r'plotprice', views.PlotPriceViewSet, basename='plotprice')
router.register(r'plotsale', views.PlotSaleViewSet, basename='plotsale')
router.register(r'user', views.GetUserView, basename='currentuser')

urlpatterns = router.urls

# urlpatterns = [
#     path('notes/', views.NoteListCreate.as_view(), name='node-list'),
#     path('notes/delete/<int:pk>/', views.NoteDelete.as_view(), name='delete_note'),
#     path('plot/', views.PlotViewSet.as_view(), name='plot'),
#     path('plotcase/', views.PlotCaseViewSet.as_view(), name='plot_case'),
#     path('plotprice/', views.PlotPriceViewSet.as_view(), name='plot_price'),
#     path('plotsale/', views.PlotSaleViewSet.as_view(), name='plot_sale'),
#     path('user/', views.GetUserView.as_view(), name='user'),
# ]
