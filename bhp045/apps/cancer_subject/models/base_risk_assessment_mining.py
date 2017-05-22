# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO_DONT_KNOW
from edc.base.model.fields.custom.custom_fields import OtherCharField

from .base_scheduled_visit_model import BaseScheduledVisitModel
from ..choices.base_risk_assessment import MINE_TIME_CHOICE, MINE_TYPE_CHOICE, MINE_UNDERGROUND_TIME_CHOICE


class BaseRiskAssessmentMining (BaseScheduledVisitModel):

    mine_time = models.CharField(
        verbose_name=("43. What is the total amount of time you worked "
                        "in the mine?"),
        max_length=25,
        choices=MINE_TIME_CHOICE,
        help_text="",
        )

    mine_type = models.CharField(
        verbose_name="44. What kind of mine have you worked in?",
        max_length=25,
        choices=MINE_TYPE_CHOICE,
        help_text="",
        )

    mine_prompt_other = OtherCharField()

    mine_underground = models.CharField(
        verbose_name="45. Have you ever worked UNDERGROUND in a mine? ",
        max_length=25,
        choices=YES_NO_DONT_KNOW,
        help_text="",
        )

    mine_underground_time = models.CharField(
        verbose_name=("46. What is the total amount of time you worked "
                        "UNDERGROUND in the mine?"),
        max_length=25,
        choices=MINE_UNDERGROUND_TIME_CHOICE,
        blank=True,
        help_text="",
        )

    last_mine = models.DateField(
        verbose_name="47. When did you last work in a mine?",
        max_length=25,
        help_text="",
        )

    history = AuditTrail()

    def get_visit(self):
        return self.subject_visit

    def __unicode__(self):
        return unicode(self.subject_visit)

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_baseriskassessmentmining_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Base Risk Assessment: Mining"
        verbose_name_plural = "Base Risk Assessment: Mining"
