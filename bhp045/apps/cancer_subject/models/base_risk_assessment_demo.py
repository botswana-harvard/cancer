# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO

from edc.base.model.fields.custom.custom_fields import OtherCharField

from ..choices.base_risk_assessment import (MARITAL_STATUS_CHOICE, RACE_CHOICE, ETHNIC_GRP_CHOICE,
                                            DISTRICT20_CHOICE, SETTING20_CHOICE, DISTRICT_CHOICE,
                                            SETTING_CHOICE, EDUCATION_CHOICE, OCCUPATION_CHOICE,
                                            MONEY_PROVIDED_CHOICE, MONEY_EARNED_CHOICE,
                                            TOILET_CHOICE, FOOD_SECURITY, COMMUNITY)

from .base_scheduled_visit_model import BaseScheduledVisitModel


class BaseRiskAssessmentDemo (BaseScheduledVisitModel):

    marital_status = models.CharField(
        verbose_name="Marital status:",
        max_length=15,
        choices=MARITAL_STATUS_CHOICE,
        help_text="",
        )
    marital_status_other = OtherCharField()

    race = models.CharField(
        verbose_name="Race:",
        max_length=15,
        choices=RACE_CHOICE,
        help_text="",
        )

    race_other = OtherCharField()

    ethnic_grp = models.CharField(
        verbose_name="Ethnic Group:",
        max_length=25,
        choices=ETHNIC_GRP_CHOICE,
        help_text="",
        )
    ethnic_grp_other = OtherCharField()

    #added in upgrade
    community = models.CharField(
        verbose_name="Since 2014, what community have you lived in?",
        max_length=35,
        choices=COMMUNITY,
        help_text=""
        )
    community_other = OtherCharField()

    district20 = models.CharField(
        verbose_name=("Over the past 20 years, which district have you "
                        "lived in the most?"),
        max_length=55,
        choices=DISTRICT20_CHOICE,
        help_text="",
        )

    setting20 = models.CharField(
        verbose_name=("Over the past 20 years, what best describes the "
                        "setting you have lived in for most of the time?"),
        max_length=15,
        choices=SETTING20_CHOICE,
        help_text="",
        )

    district = models.CharField(
        verbose_name="Which district do you live in now?",
        max_length=65,
        choices=DISTRICT_CHOICE,
        help_text="",
        )

    setting = models.CharField(
        verbose_name=("What best describes the setting you live in for "
                        "most of the time now?"),
        max_length=15,
        choices=SETTING_CHOICE,
        help_text="",
        )

    education = models.CharField(
        verbose_name="Educational level completed:",
        max_length=25,
        choices=EDUCATION_CHOICE,
        help_text="",
        )

    occupation = models.CharField(
        verbose_name="Occupation:",
        max_length=25,
        choices=OCCUPATION_CHOICE,
        help_text="",
        )
    occupation_other = OtherCharField()

    money_provide = models.CharField(
        verbose_name="Who provides most of your money:",
        max_length=25,
        choices=MONEY_PROVIDED_CHOICE,
        help_text="",
        )
    money_provide_other = OtherCharField()

    money_earned = models.CharField(
        verbose_name="How much money do you personally earn?",
        max_length=45,
        choices=MONEY_EARNED_CHOICE,
        help_text="",
        )

    electricity = models.CharField(
        verbose_name="Do you have electricity in your house?",
        max_length=3,
        choices=YES_NO,
        help_text="",
        )

    toilet = models.CharField(
        verbose_name=("Which of the following types of toilet "
                        "facilities do you most often use at home?"),
        max_length=45,
        choices=TOILET_CHOICE,
        help_text="",
        )

    toilet_other = OtherCharField()

    household_people = models.IntegerField(
        verbose_name=("How many people, including yourself, stay in "
                        "your household/compound most of the time?"),
        help_text="",
        )

    food_security = models.CharField(
        verbose_name=("In the past 4 weeks, did you or any household member have to eat a "
                      "smaller meal than you felt you needed, or even to skip a meal, because"
                      "there was not enough food?"),
        max_length=15,
        choices=FOOD_SECURITY,
        help_text="",
        )

    history = AuditTrail()

    def get_visit(self):
        return self.subject_visit

    def __unicode__(self):
        return unicode(self.subject_visit)

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_baseriskassessmentdemo_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Base Risk Assessment: Demographics"
        verbose_name_plural = "Base Risk Assessment: Demographics"
