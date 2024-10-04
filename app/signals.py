from django.db.models.signals import post_save
from django.dispatch import receiver

from app.models.challenge import ChallengeTransaction


@receiver(post_save, sender=ChallengeTransaction)
def create_award_transaction(sender, instance, created, **kwargs):
    pass