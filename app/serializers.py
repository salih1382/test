from rest_framework import serializers
from .models import ChallengeItem, ChallengeTransaction
import jdatetime

class ChallengeItemSerializer(serializers.ModelSerializer):
    is_done = serializers.SerializerMethodField()
    jalali_date_to_display = serializers.SerializerMethodField()

    class Meta:
        model = ChallengeItem
        fields = ['id', 'title', 'description', 'is_done', 'jalali_date_to_display']

    def get_is_done(self, obj):
        user = self.context['request'].user
        return ChallengeTransaction.objects.filter(challenge_item=obj, user=user).exists()

    def get_jalali_date_to_display(self, obj):
        jalali_date = jdatetime.datetime.fromgregorian(datetime=obj.date_to_display)
        return jalali_date.strftime('%Y/%m/%d')


class ChallengePostSerializer(serializers.Serializer):
    challenge_item_ids = serializers.ListField(
        child=serializers.IntegerField(), required=True
    )
