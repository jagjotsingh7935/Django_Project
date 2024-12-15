from django.test import TestCase
from .models import TodoItem, Tag

class TodoItemTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Urgent")
        self.todo = TodoItem.objects.create(
            title="Sample Task",
            description="Task description",
            status="OPEN",
        )
        self.todo.tags.add(self.tag)

    def test_create_todo(self):
        self.assertEqual(TodoItem.objects.count(), 1)
        self.assertEqual(self.todo.title, "Sample Task")
