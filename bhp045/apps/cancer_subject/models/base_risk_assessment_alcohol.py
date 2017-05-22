# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

from edc.audit.audit_trail import AuditTrail

from .base_scheduled_visit_model import BaseScheduledVisitModel


class BaseRiskAssessmentAlcohol (BaseScheduledVisitModel):

    alcohol_weekly = models.IntegerField(
        verbose_name=("How many days per week do you drink alcohol?"),
        validators=[MinValueValidator(1), MaxValueValidator(7)],
        #blank = True,
        help_text="",
        )

    amount_drinking = models.IntegerField(
        verbose_name=("On days you drink, how many drinks do you have (one drink is 300ml of "
                      "beer/chibuku, 150ml of wine,or 50ml of whiskey/vodka/gin)?"),
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        #blank = True,
        help_text="",
        )

    history = AuditTrail()

    def get_visit(self):
        return self.subject_visit

    def __unicode__(self):
        return unicode(self.subject_visit)

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_baseriskassessmentalcohol_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Base Risk Assessment: Alcohol"
        verbose_name_plural = "Base Risk Assessment: Alcohol"
