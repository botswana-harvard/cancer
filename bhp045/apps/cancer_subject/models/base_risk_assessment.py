# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO, YES_NO_DONT_KNOW
from .base_scheduled_visit_model import BaseScheduledVisitModel
from ..choices.base_risk_assessment import HEPATITIS_BEFORE_CHOICE, AGE_FIRSTSEX_CHOICE, \
                                            TRADMEDICINE_CHOICE, YES_NO_DECLINED


class BaseRiskAssessment (BaseScheduledVisitModel):

    """ CA001"""
    #not required anymore
#     participant_interviewed = models.CharField(
#         verbose_name=("Was participant interviewed for demographic "
#                         "and risk factor information?"),
#         max_length=3,
#         choices=YES_NO,
#         help_text=(""),
#         )

    """ cancer, tb, hep """

    hepatitis = models.CharField(
        verbose_name=("Have you been told you have hepatitis B or C "
                        "before?"),
        max_length=15,
        choices=HEPATITIS_BEFORE_CHOICE,
        help_text="",
        )

    tuberculosis = models.CharField(
        verbose_name=("Do you have now or have you ever had "
                        "tuberculosis?"),
        max_length=25,
        choices=YES_NO_DONT_KNOW,
        help_text="",
        )

    year_tb = models.IntegerField(
        verbose_name=("In what year did you last have tuberculosis "
                        "(year of diagnosis)?"),
        validators=[MinValueValidator(1900), MaxValueValidator(2020)],
        null=True,
        blank=True,
        help_text="",
        )

    """ sun exposure """

    """ cooking fuel """

    """ mine work """
    has_worked_mine = models.CharField(
        verbose_name="Have you ever worked at a mine? ",
        max_length=35,
        choices=YES_NO_DECLINED,
        help_text="",
        )

    """ smoking """
    has_smoked = models.CharField(
        verbose_name="Have you ever smoked cigarettes?",
        max_length=35,
        choices=YES_NO_DECLINED,
        help_text="",
        )

    """ sex """
    age_firstsex = models.CharField(
        verbose_name="How old were you when you first had sex?",
        max_length=35,
        choices=AGE_FIRSTSEX_CHOICE,
        help_text="",
        )

    """ alcohol """
    has_alcohol = models.CharField(
        verbose_name="Do you drink alcohol?",
        max_length=35,
        choices=YES_NO_DECLINED,
        help_text="",
        )

    tradmedicine = models.CharField(
        verbose_name="How often do you use traditional medicine?",
        max_length=35,
        choices=TRADMEDICINE_CHOICE,
        help_text="",
        )

    is_albino = models.CharField(
        verbose_name="Is patient an albino?",
        max_length=3,
        choices=YES_NO,
        help_text="",
        )

    history = AuditTrail()

    def get_visit(self):
        return self.subject_visit

    def __unicode__(self):
        return unicode(self.subject_visit)

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_baseriskassessment_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Base Risk Assessment"
