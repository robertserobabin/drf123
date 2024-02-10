from django.urls import path
from payments.apps import PaymentsConfig
from payments.views import PaymentCreateAPIView, PaymentListAPIView, PaymentRetrieveAPIView, PaymentDestroyAPIView, \
    GetPaymentView

app_name = PaymentsConfig.name

urlpatterns = [
    path('payments/create/', PaymentCreateAPIView.as_view(), name='payments-create'),
    path('payments/', PaymentListAPIView.as_view(), name='payments'),
    path('payments/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payments-get'),
    path('payments/delete/<int:pk>/', PaymentDestroyAPIView.as_view(), name='payments-delete'),
    path('payments/<str:payment_id>/', GetPaymentView.as_view(), name='payment_get'),
]