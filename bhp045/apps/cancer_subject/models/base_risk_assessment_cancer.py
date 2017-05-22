# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO_DONT_KNOW
from edc.base.model.fields.custom.custom_fields import OtherCharField

from .base_scheduled_visit_model import BaseScheduledVisitModel
from ..choices.base_risk_assessment import CANCER_TYPE_CHOICE, CANCER_BEFORE_CHOICE


class BaseRiskAssessmentCancer (BaseScheduledVisitModel):

    family_cancer = models.CharField(
        verbose_name=("Has your son, daughter, brother, sister, or "
                        "parent ever had cancer?"),
        max_length=25,
        choices=YES_NO_DONT_KNOW,
        help_text="",
        )

    family_cancer_type = models.CharField(
        verbose_name=("What kind of cancer did your brother, sister, "
                        "or parent have?"),
        max_length=45,
        choices=CANCER_TYPE_CHOICE,
        blank=True,
        help_text="",
        )

    family_cancer_other = OtherCharField()

    had_previous_cancer = models.CharField(
        verbose_name=("Have you had PREVIOUS cancer, before the current "
                        "cancer?"),
        max_length=25,
        choices=YES_NO_DONT_KNOW,
        help_text="",
        )

    previous_cancer = models.CharField(
        verbose_name="What kind of cancer did you have before?",
        max_length=45,
        choices=CANCER_BEFORE_CHOICE,
        blank=True,
        help_text="",
        )

    previous_cancer_other = OtherCharField()

    history = AuditTrail()

    def get_visit(self):
        return self.subject_visit

    def __unicode__(self):
        return unicode(self.subject_visit)

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_baseriskassessmentcancer_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Base Risk Assessment: Cancer"
        verbose_name_plural = "Base Risk Assessment: Cancer"
