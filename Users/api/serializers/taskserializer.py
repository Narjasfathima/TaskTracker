from rest_framework import serializers
from django.utils import timezone

from Admin.models import Task


class CustomJSONField(serializers.JSONField):
    """
    Custom JSON field serializer to convert JSON data into list format
    """
    def to_representation(self, value):
        if isinstance(value, dict):
            return list(value.values())
        return value
    

class TaskListSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id','task_id', 'title','due_date','assigned_to',
                  'status']
        
    def get_assigned_to(self, obj):
        full_name = obj.assigned_to.first_name + ' ' +obj.assigned_to.last_name
        return full_name
    

class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['status', 'completion_report', 'worked_hours']

    def validate(self, data):
        status = data.get('status')
        completion_report = data.get('completion_report')
        worked_hours = data.get('worked_hours')

        if status == 'Completed':
            if completion_report is None:
                raise serializers.ValidationError({'completion_report': 'This field is required when status is Completed.'})
            if not worked_hours:
                raise serializers.ValidationError({'worked_hours': 'This field is required when status is Completed.'})
        return data
    

class TaskReportViewSerializer(serializers.ModelSerializer):
    assigned_to = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [ 'title','due_date','assigned_to',
                  'completion_report','worked_hours']
        
    def get_assigned_to(self, obj):
        full_name = obj.assigned_to.first_name + ' ' +obj.assigned_to.last_name
        return full_name