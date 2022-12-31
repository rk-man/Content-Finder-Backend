
from django.shortcuts import redirect
from base.models import Order
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from base.serializers import OrderSerializer, OrderItemsSerializer
from rest_framework.response import Response
from rest_framework import status
from base.models import Content
import math

# stripe initialization
from django.conf import settings
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
backend_url = settings.BACKEND_URL
frontend_url = settings.FRONTEND_URL


def checkIfUserAlreadyBought():
    pass


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_checkout_session(req):
    products = req.data["orderItems"]
    # print(products)

    def getEachProduct(product):
        coverImage = product["coverImage"]
        return {
            "price_data": {
                "currency": "usd",
                "product_data": {
                    "name": product["title"],
                    "images": [f"{backend_url}/{coverImage}"]
                },
                "unit_amount": math.floor(float(product["price"]) * 100)
            },
            "quantity": 1
        }

    products = list(map(getEachProduct, products))
    print(products)

    checkout_session = None
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=products,
            mode='payment',
            success_url=frontend_url +
            '/orders/success?session_d={CHECKOUT_SESSION_ID}',
            cancel_url=frontend_url + '/orders/failed',
        )

        return Response({
            "checkout_session_url": checkout_session.url,
        })
    except Exception as e:
        print(e)
        return Response({
            "error": "Something went wrong"
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createOrder(req):
    profile = req.user.profile
    data = req.data
    filteredOrder = Order.objects.filter(buyer=profile)

    # to ensure that the user doesn't buy the content that has already been bought
    for item in data['orderItems']:
        orders = filteredOrder.filter(orderItems=item)
        if (orders):
            return Response({"detail": "Can't order an item that you have already bought"}, status=status.HTTP_406_NOT_ACCEPTABLE)

    order = Order.objects.create(
        buyer=profile,
        totalPrice=data["totalPrice"]
    )

    order.orderItems.set(data["orderItems"])

    sr = OrderSerializer(order, many=False)

    return Response(sr.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getAllOrders(req):
    profile = req.user.profile
    orders = Order.objects.filter(buyer=profile)
    sr = OrderItemsSerializer(orders, many=True)
    return Response(sr.data)
