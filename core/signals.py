from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from core.models import ContentImage


# user deletes image
@receiver(pre_delete, sender=ContentImage)
def delete_content_image(instance, **_kwargs):
    instance.image.delete(save=False)


# user updates image
@receiver(pre_save, sender=ContentImage)
def change_content_image(instance, **_kwargs):
    if instance.id:
        # perform for updates only
        old_image = get_object_or_404(
            ContentImage,
            **{'id': instance.id}
        )
        if old_image.image.url != instance.image.url:
            old_image.image.delete(save=False)
