from django.urls import path

from api.views import ItemBuyView, ItemDetailView

urlpatterns = [
    path('buy/<int:item_id>/', ItemBuyView.as_view(), name="item_buy"),
    path('item/<int:item_id>/', ItemDetailView.as_view(), name="item_detail"),
]
