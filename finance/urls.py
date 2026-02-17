from rest_framework.routers import DefaultRouter
from .views import IncomeViewSet, ExpenseViewSet, DebtViewSet

router = DefaultRouter()
router.register(r'income', IncomeViewSet, basename='income')
router.register(r'expense', ExpenseViewSet, basename='expense')
router.register(r'debt', DebtViewSet, basename='debt')

urlpatterns = router.urls
