# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

from edc.audit.audit_trail import AuditTrail

from .base_scheduled_visit_model import BaseScheduledVisitModel
from ..choices.base_risk_assessment import SMOKE_NOW_CHOICE, CIGARETTE_SMOKING_CHOICE, CIGARETTE_SMOKED_CHOICE, WHEN_QUIT_CHOICE


class BaseRiskAssessmentSmoking (BaseScheduledVisitModel):

    smoke_now = models.CharField(
        verbose_name="Do you smoke cigarettes now?",
        max_length=35,
        choices=SMOKE_NOW_CHOICE,
        help_text="",
        )

    cigarette_smoking = models.CharField(
        verbose_name="How many cigarettes do you smoke per day?",
        max_length=35,
        choices=CIGARETTE_SMOKING_CHOICE,
        null=True,
        blank=True,
        help_text="",
        )

    years_smoked = models.IntegerField(
        verbose_name="For how many years have you smoked?",
        validators=[MinValueValidator(0), MaxValueValidator(90)],
        null=True,
        blank=True,
        help_text="If subject has quit smoking, leave blank.",
        )

    cigarette_smoked = models.CharField(
        verbose_name="How many cigarettes did you smoke per day?",
        max_length=35,
        choices=CIGARETTE_SMOKED_CHOICE,
        null=True,
        blank=True,
        help_text="",
        )

    when_quit = models.CharField(
        verbose_name="When did you quit smoking cigarettes?",
        max_length=35,
        choices=WHEN_QUIT_CHOICE,
        null=True,
        blank=True,
        help_text="",
        )

    years_smoked_before = models.IntegerField(
        verbose_name="For how many years did you smoke before quitting?",
        null=True,
        blank=True,
        help_text="",
        )

    history = AuditTrail()

    def get_visit(self):
        return self.subject_visit

    def __unicode__(self):
        return unicode(self.subject_visit)

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_baseriskassessmentsmoking_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Base Risk Assessment: Smoking"
        verbose_name_plural = "Base Risk Assessment: Smoking"
