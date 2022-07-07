from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from products.models.product_provider import ProductProvider


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_product_provider_for_new_user(sender, **kwargs):
    if kwargs['created']:
        ProductProvider.objects.create(user=kwargs['instance'])
