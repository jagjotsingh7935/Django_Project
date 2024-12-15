from rest_framework import serializers
from .models import TodoItem, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class TodoItemSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)  # Make tags optional

    class Meta:
        model = TodoItem
        fields = '__all__'

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        todo_item = TodoItem.objects.create(**validated_data)
        
        # Handle tags only if they are provided
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            todo_item.tags.add(tag)  # Add the tag to the TodoItem

        return todo_item

    def update(self, instance, validated_data):
        # Handle the update scenario where you want to keep existing tags and add new ones
        tags_data = validated_data.pop('tags', [])
        
        # Update the TodoItem fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()

        # Remove all existing tags and add the new ones
        instance.tags.clear()
        for tag_data in tags_data:
            tag, created = Tag.objects.get_or_create(**tag_data)
            instance.tags.add(tag)  # Add the tag to the TodoItem

        return instance
