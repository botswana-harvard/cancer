from django import forms
from django.contrib.admin.widgets import AdminRadioSelect, AdminRadioFieldRenderer

from edc.subject.off_study.forms import BaseOffStudyForm

from ...cancer_subject.choices import OFF_STUDY_REASON
from ..models import SubjectOffStudy


class SubjectOffStudyForm (BaseOffStudyForm):

    reason = forms.ChoiceField(
        label='Please code the primary reason participant taken off-study',
        choices=[choice for choice in OFF_STUDY_REASON],
        help_text="",
        widget=AdminRadioSelect(renderer=AdminRadioFieldRenderer),
        )

    class Meta:
        model = SubjectOffStudy
