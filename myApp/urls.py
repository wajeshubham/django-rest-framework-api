from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'employee', views.EmployeeView, basename='employee')
router.register(r'activity_period', views.ActivityPeriodView, basename='activity_period')

urlpatterns = []
urlpatterns += router.urls
