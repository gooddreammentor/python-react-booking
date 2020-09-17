from rest_framework import serializers

from availabilities.models import Availability


class AvailabilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'
