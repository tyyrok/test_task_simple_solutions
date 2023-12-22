from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"Item {self.name}"


class ItemStripe(models.Model):
    price_id = models.CharField(max_length=35)
    item = models.OneToOneField(
        Item,
        on_delete=models.CASCADE,
        primary_key=True
    )

    def __str__(self) -> str:
        return f"Stripe Price Id for {self.item}"
