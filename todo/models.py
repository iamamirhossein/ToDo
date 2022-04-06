from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):
    ITEM_TASK = '1'
    ITEM_ISSUE = '2'
    ITEM_REMINDER = '3'
    TYPE_CHOICES = [
        (ITEM_TASK, 'task'),
        (ITEM_ISSUE, 'issue'),
        (ITEM_REMINDER, 'reminder'),
    ]

    STATUS_DONE = '1'
    STATUS_DOING = '2'
    STATUS_TODO = '3'
    STATUS_CHOICES = [
        (STATUS_DONE, 'done'),
        (STATUS_DOING, 'doing'),
        (STATUS_TODO, 'todo'),
    ]

    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='reported_items', null=True)
    assigned = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='assigned_items', null=True)
    item_type = models.CharField(max_length=1, choices=TYPE_CHOICES, default=ITEM_TASK)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=STATUS_TODO)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.title

