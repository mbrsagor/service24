from rest_framework.serializers import ModelSerializerfrom core.models.location import Locationclass LocationSerializer(ModelSerializer):    class Meta:        model = Location        fields = (            'id', 'name', 'parent', 'is_active'        )