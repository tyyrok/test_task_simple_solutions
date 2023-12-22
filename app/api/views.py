from django.shortcuts import render
from django.views import View
from django.http import HttpResponseNotFound, JsonResponse

from api.models import Item, ItemStripe
from api.forms import ItemForm
from api.utils import get_session_id, create_stripe_product


class ItemBuyView(View):
    def get(self, request, item_id, *args, **kwargs):
        if item := Item.objects.filter(id=item_id).first():
            try:
                price_id = item.itemstripe.price_id
            except ItemStripe.DoesNotExist:
                price_id = create_stripe_product(
                    name=item.name,
                    amount=item.price
                )
                ItemStripe.objects.create(item=item, price_id=price_id)

            session_id = get_session_id(price_id)
            data = {"session_id": session_id}
            return JsonResponse(data=data)

        return HttpResponseNotFound({"Item not found"})


class ItemDetailView(View):
    tempate_name = "api/item_detail.html"
    form_class = ItemForm

    def get(self, request, item_id, *args, **kwargs):
        if item := Item.objects.filter(id=item_id).first():
            form = self.form_class(instance=item)
            return render(
                request, self.tempate_name, {"form": form, "item_id": item_id}
            )

        return HttpResponseNotFound()
