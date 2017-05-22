from django import forms

from .base_subject_model_form import BaseSubjectModelForm
from ..models import (LabResult, LabResultHeightWeight, LabResultHiv,
                                   LabResultCd4, LabResultViralload,
                                   LabResultHaematology, LabResultChemistry,
                                   LabResultTb)


# LabResult
class LabResultForm (BaseSubjectModelForm):

    class Meta:
        model = LabResult


# LabResultHeightWeight
class LabResultHeightWeightForm (BaseSubjectModelForm):

    class Meta:
        model = LabResultHeightWeight


# LabResultHiv
class LabResultHivForm (BaseSubjectModelForm):

    class Meta:
        model = LabResultHiv


# LabResultCd4
class LabResultCd4Form (BaseSubjectModelForm):

    class Meta:
        model = LabResultCd4


# LabResultViralload
class LabResultViralloadForm (BaseSubjectModelForm):

    class Meta:
        model = LabResultViralload


# LabResultHaematology
class LabResultHaematologyForm (BaseSubjectModelForm):

    class Meta:
        model = LabResultHaematology


# LabResultChemistry
class LabResultChemistryForm (BaseSubjectModelForm):

    class Meta:
        model = LabResultChemistry


# LabResultTb
class LabResultTbForm (BaseSubjectModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['tb_treatment'] == 'Yes, isoniazid preventative therapy (IPT)' and not cleaned_data['tb_treatment_start']:
            raise forms.ValidationError('If participant is receiving any kind of treatment, when did this treatment begin')
        if cleaned_data['tb_treatment'] == 'Yes, combination anti-tuberculosis treatment (ATT)' and not cleaned_data['tb_treatment_start']:
            raise forms.ValidationError('If participant is receiving any kind of treatment, when did this treatment begin')
        cleaned_data = super(LabResultTbForm, self).clean()
        return cleaned_data

    class Meta:
        model = LabResultTb
