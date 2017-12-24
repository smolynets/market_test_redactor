import logging
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Flower



####student
@receiver(post_save, sender=Flower)
def log_flower_updated_added_event(sender, **kwargs):
	logger = logging.getLogger(__name__)
	flower = kwargs['instance']
	if kwargs['created']:
		logger.info("Flower added: %s %s (ID: %d)", flower.title, 
		 flower.user, flower.id)
	else:
		logger.info("Flower updated: %s %s (ID: %d)", flower.title, 
	     flower.user, flower.id)


@receiver(post_delete, sender=Flower)
def log_flower_deleted_event(sender, **kwargs):
	logger = logging.getLogger(__name__)
	flower = kwargs['instance']
	logger.info("Flower deleted: %s (ID: %d)", flower.title,
         flower.id)


