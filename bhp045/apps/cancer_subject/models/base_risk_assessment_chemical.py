# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO_DONT_KNOW

from .base_scheduled_visit_model import BaseScheduledVisitModel
from ..choices.base_risk_assessment import (ASBESTOS_NO_PROTECTION_CHOICE, CHEMICALS_TIME_CHOICE,
                                            TOTAL_TIME_NO_PROTECTION_CHOICE)


class BaseRiskAssessmentChemical (BaseScheduledVisitModel):

    """ chemical exposure """
    asbestos = models.CharField(
        verbose_name=("Have you ever worked with asbestos without adequate protection?"),
        max_length=25,
        choices=YES_NO_DONT_KNOW,
        help_text="",
        )

    asbestos_no_protection = models.CharField(
        verbose_name=("What is the total amount of time you worked with "
                      "asbestos without protection?"),
        max_length=25,
        choices=ASBESTOS_NO_PROTECTION_CHOICE,
        blank=True,
        help_text="",
        )

    chemicals = models.CharField(
        verbose_name=("Have you ever worked with any of these chemical without adequate "
                      "protection?"),
        max_length=25,
        choices=YES_NO_DONT_KNOW,
        help_text=("Radon, Cadmium, Chromium, Beryllium, Aluminum, Silica, Sulfuric acid,"
                   " mist, chloromethyl ether, coke (fuel from coal), mustard gas"),
        )

    chemicals_time = models.CharField(
        verbose_name=("What is the total amount of time you worked with "
                        "the chemical(s) without protection?"),
        max_length=25,
        choices=CHEMICALS_TIME_CHOICE,
        blank=True,
        help_text="",
        )

    arsenic_smelting = models.CharField(
        verbose_name=("Have you ever been involved with arsenic "
                        "smelting (nickel and copper), coal gasification, "
                        "or iron/steel founding without adequate "
                        "protection? "),
        max_length=25,
        choices=YES_NO_DONT_KNOW,
        help_text="",
        )

    total_time_no_protection = models.CharField(
        verbose_name=("What is the total amount of time you worked with "
                        "the process(es) without protection?"),
        max_length=25,
        choices=TOTAL_TIME_NO_PROTECTION_CHOICE,
        blank=True,
        help_text="",
        )

    history = AuditTrail()

    def get_visit(self):
        return self.subject_visit

    def __unicode__(self):
        return unicode(self.subject_visit)

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_baseriskassessmentchemical_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Base Risk Assessment: Chemicals"
        verbose_name_plural = "Base Risk Assessment: Chemicals"
