from typing import Any

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Model


class SequentialNumberField(models.PositiveIntegerField):
    def __init__(self, *args, key=None, start_at=1, increment=1, **kwargs):
        """
        Initializes a SequentialNumberField.

        Args:
            key (list of str, optional): A list of field names to use as keys for sequential number grouping.
                If specified, the sequential number will be unique within the group specified by the key.
                Defaults to None.
            start_at (int, optional): The initial value for the sequence. Defaults to 1.
            increment (int, optional): The increment value for the sequence. Defaults to 1.
        """
        if isinstance(key, str):
            self.key = [key]
        else:
            self.key = key
        self.start_at = start_at
        self.increment = increment
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance: Model, add: bool) -> Any:
        """
        Pre-save method to generate and assign the sequential number.

        Args:
            model_instance (Model): The model instance being saved.
            add (bool): True if the model instance is being added, False if it's being updated.

        Returns:
            int: The generated sequential number.
        """
        if getattr(model_instance, self.attname) is None:
            try:
                qs = self._get_queryset_for(model_instance)
                highest_item = qs.latest(self.attname)
                highest_value = getattr(highest_item, self.attname)
                value = highest_value + self.increment
            except ObjectDoesNotExist:
                value = self.start_at
            setattr(model_instance, self.attname, value)
            return value
        return super().pre_save(model_instance, add)

    def _get_queryset_for(self, model_instance: Model) -> models.QuerySet:
        """
        Get the queryset for retrieving the highest item for sequential number generation.

        Args:
            model_instance (Model): The model instance being saved.

        Returns:
            models.QuerySet: The queryset for retrieving the highest item.
        """
        qs = self.model.objects.all()
        if self.key:
            query = {field: getattr(model_instance, field) for field in self.key}
            qs = qs.filter(**query)
        return qs
