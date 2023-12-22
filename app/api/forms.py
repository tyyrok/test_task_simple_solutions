from django.forms import ModelForm

from api.models import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["id", "name", "price", "description"]
