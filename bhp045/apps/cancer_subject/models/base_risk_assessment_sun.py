# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail

from .base_scheduled_visit_model import BaseScheduledVisitModel
from ..choices.base_risk_assessment import (HOURS_OUTDOOR_CHOICE, SLEEVED_SHIRT_CHOICE,
                                            HAT_CHOICE, SUNGLASSES_CHOICE, SHADE_UMBRELLA_CHOICE)


class BaseRiskAssessmentSun (BaseScheduledVisitModel):

    hours_outdoor = models.CharField(
        verbose_name=("On average, how many hours are you outdoors per "
                        "day between 10am and 4pm?"),
        max_length=15,
        choices=HOURS_OUTDOOR_CHOICE,
        help_text="",
        )

    sleeved_shirt = models.CharField(
        verbose_name=("When you are outside on a sunny day, how often "
                        "do you wear a SHIRT WITH SLEEVES?"),
        max_length=15,
        choices=SLEEVED_SHIRT_CHOICE,
        help_text="",
        )

    hat = models.CharField(
        verbose_name=("When you are outside on a sunny day, how often "
                        "do you wear a HAT?"),
        max_length=15,
        choices=HAT_CHOICE,
        help_text="",
        )

    shade_umbrella = models.CharField(
        verbose_name=("When you are outside on a sunny day, how often "
                        "do you stay in the SHADE or UNDER AN UMBRELLA?"),
        max_length=15,
        choices=SHADE_UMBRELLA_CHOICE,
        help_text="",
        )

    sunglasses = models.CharField(
        verbose_name=("When you are outside on a sunny day, how often "
                        "do you wear SUNGLASSES?"),
        max_length=15,
        choices=SUNGLASSES_CHOICE,
        help_text="",
        )

    history = AuditTrail()

    def get_visit(self):
        return self.subject_visit

    def __unicode__(self):
        return unicode(self.subject_visit)

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_baseriskassessmentsun_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Base Risk Assessment: Sun"
        verbose_name_plural = "Base Risk Assessment: Sun"
