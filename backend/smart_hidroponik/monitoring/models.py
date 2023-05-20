from typing import Any
from django.db import models
# Create your models here.

# third party imports
from django_extensions.db.models import TimeStampedModel


class TDSMonitoring(TimeStampedModel):
    tds_value = models.DecimalField(
        decimal_places=2, null=True, blank=True, max_digits=65)
    temperature_value = models.DecimalField(
        decimal_places=2, null=True, blank=True, max_digits=65)
    sensor = models.CharField(
        null=True, max_length=65, blank=True)

    class Meta:
        app_label = 'monitoring'
        verbose_name = "TDS"
        verbose_name_plural = "TDS"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
