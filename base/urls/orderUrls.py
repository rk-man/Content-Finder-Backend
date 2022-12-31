from django.urls import path, include

from base.views.orderViews import createOrder, getAllOrders, create_checkout_session
urlpatterns = [
    path("", getAllOrders, name="get-all-orders"),
    path("create/", createOrder, name="create-order"),
    path("checkout-order/", create_checkout_session,
         name="create-checkout-session")
]
