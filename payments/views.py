import stripe
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from payments.models import Payments
from payments.serializers import PaymentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.user = self.request.user
        new_payment = serializer.save()
        stripe.api_key = "sk_test_51OehrJD5m4aUSLBWp6g4FVyBmn0CvEC2HND6NThikhiPng4TrfFOPbZdOLLupbjmL2PHmCmdxgITUYVoRyqd8UXx00tuZGGevy"
        payment_intent = stripe.PaymentIntent.create(
            amount=2000,
            currency="usd",
            automatic_payment_methods={"enabled": True},
        )
        new_payment.session_id = payment_intent.id
        new_payment.amount = payment_intent.amount
        new_payment.save()

        return super().perform_create(new_payment)


class GetPaymentView(APIView):
    serializer_class = PaymentSerializer

    def get(self, request, payment_id):
        payment = Payments.objects.get(pk=payment_id)
        payment_id = payment.session_id
        stripe.api_key = 'sk_test_51OdoXSHC8LUh8NqZQboynIwfP7znL7qfNqCOqOYkl7k3pzAKN8QU45ye5RpnABJ2MRjLBfk6tWWisTmY9QoiXJNR00NP3ImbNV'
        payment_intent = stripe.PaymentIntent.retrieve(payment_id)
        print(payment_intent)
        return Response({'status': payment_intent.status, 'body': payment_intent})


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course_payment', 'lesson_payment', 'payment_method')
    ordering_fields = ('date',)


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Payments.objects.all()


class PaymentDestroyAPIView(generics.DestroyAPIView):
    queryset = Payments.objects.all()