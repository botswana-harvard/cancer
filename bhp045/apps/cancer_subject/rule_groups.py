from edc.constants import NO, YES
from edc.subject.appointment.models import Appointment
from edc.subject.rule_groups.classes import RuleGroup, site_rule_groups, ScheduledDataRule, Logic
from edc.subject.registration.models import RegisteredSubject

from ..cancer_list.models import ResultsToRecord
from models import (SubjectVisit, BaseRiskAssessment, BaselineHIVHistory,
                    OncologyTreatmentRecord, BHHHivTest, SymptomsAndTesting,
                    CancerDiagnosis, OncologyTreatmentCompleted, OncologyTreatmentPlan)


class BaseRiskAssessmentRuleGroup(RuleGroup):

    has_smoked = ScheduledDataRule(
        logic=Logic(
            predicate=(('has_smoked', 'equals', NO), ('has_smoked', 'equals', 'Declined', 'or')),
            consequence='not_required',
            alternative='new'),
        target_model=['baseriskassessmentsmoking'])

    has_worked_mine = ScheduledDataRule(
        logic=Logic(
            predicate=(('has_worked_mine', 'equals', NO), ('has_worked_mine', 'equals', 'Declined', 'or')),
            consequence='not_required',
            alternative='new'),
        target_model=['baseriskassessmentmining'])

    has_alcohol = ScheduledDataRule(
        logic=Logic(
            predicate=(('has_alcohol', 'equals', NO), ('has_alcohol', 'equals', 'Declined', 'or')),
            consequence='not_required',
            alternative='new'),
        target_model=['baseriskassessmentalcohol'])

    class Meta:
        app_label = 'cancer_subject'
        source_fk = (SubjectVisit, 'subject_visit')
        source_model = BaseRiskAssessment
site_rule_groups.register(BaseRiskAssessmentRuleGroup)


class GenderRuleGroup(RuleGroup):

    gender = ScheduledDataRule(
        logic=Logic(
            predicate=('gender', 'equals', 'm'),
            consequence='not_required',
            alternative='new'),
        target_model=['baseriskassessmentfemale'])

    class Meta:
        app_label = 'cancer_subject'
        source_fk = None
        source_model = RegisteredSubject
site_rule_groups.register(GenderRuleGroup)


# class LabResultRuleGroup(RuleGroup):

#     has_hiv_result = ScheduledDataRule(
#         logic=Logic(
#             predicate=('has_hiv_result', 'equals', 'no'),
#             consequence='not_required',
#             alternative='new'),
#         target_model=['labresulthiv'])

#     has_cd4 = ScheduledDataRule(
#         logic=Logic(
#             predicate=('has_cd4', 'equals', 'no'),
#             consequence='not_required',
#             alternative='new'),
#         target_model=['labresultcd4'])

#     has_vl = ScheduledDataRule(
#         logic=Logic(
#             predicate=('has_vl', 'equals', 'no'),
#             consequence='not_required',
#             alternative='new'),
#         target_model=['labresultviralload'])

#     has_haem = ScheduledDataRule(
#         logic=Logic(
#             predicate=('has_haem', 'equals', 'no'),
#             consequence='not_required',
#             alternative='new'),
#         target_model=['labresulthaematology'])
# 
#     has_chem = ScheduledDataRule(
#         logic=Logic(
#             predicate=('has_chem', 'equals', 'no'),
#             consequence='not_required',
#             alternative='new'),
#         target_model=['labresultchemistry'])
# 
#     tb_tests = ScheduledDataRule(
#         logic=Logic(
#             predicate=('tb_tests', 'equals', 'no'),
#             consequence='not_required',
#             alternative='new'),
#         target_model=['labresulttb'])

#     class Meta:
#         app_label = 'cancer_subject'
#         source_fk = (SubjectVisit, 'subject_visit')
#         source_model = LabResult
# site_rule_groups.register(LabResultRuleGroup)


class BaselineHIVHistoryRuleGroup(RuleGroup):

    has_hiv_result = ScheduledDataRule(
        logic=Logic(
            predicate=(('has_hiv_result', 'equals', NO), ('has_hiv_result', 'equals', 'Dont_know', 'or')),
            consequence='not_required',
            alternative='new'),
        target_model=['bhhhivtest'])

    had_who_illnesses = ScheduledDataRule(
        logic=Logic(
            predicate=('had_who_illnesses', 'equals', NO),
            consequence='not_required',
            alternative='new'),
        target_model=['bhhwhoillness'])

#     has_cd4 = ScheduledDataRule(
#         logic=Logic(
#             predicate=('has_cd4', 'equals', 'no'),
#             consequence='not_required',
#             alternative='new'),
#         target_model=['bhhcd4'])

    class Meta:
        app_label = 'cancer_subject'
        source_fk = (SubjectVisit, 'subject_visit')
        source_model = BaselineHIVHistory
site_rule_groups.register(BaselineHIVHistoryRuleGroup)


class BHHHivTestRuleGroup(RuleGroup):

    hiv_result = ScheduledDataRule(
        logic=Logic(
            predicate=('hiv_result', 'equals', 'POS'),
            consequence='new',
            alternative='not_required'),
        target_model=['haartrecord'])

    also_hiv_result = ScheduledDataRule(
        logic=Logic(
            predicate=(('hiv_result', 'equals', 'NEG'), ('hiv_result', 'equals', 'UKN', 'or')),
            consequence='not_required',
            alternative='new'),
        target_model=['haartrecord'])

    class Meta:
        app_label = 'cancer_subject'
        source_fk = (SubjectVisit, 'subject_visit')
        source_model = BHHHivTest
site_rule_groups.register(BHHHivTestRuleGroup)


def func_oncology_plan(visit_instance):
    try:
        OncologyTreatmentPlan.objects.get(subject_visit=visit_instance, radiation_plan=YES)
    except OncologyTreatmentPlan.DoesNotExist:
        return False
    return True


def func_oncology_record(visit_instance):
    try:
        OncologyTreatmentRecord.objects.get(subject_visit=visit_instance, radiation_received=YES)
    except OncologyTreatmentRecord.DoesNotExist:
        return False
    return True


def func_oncology(visit_instance):
    show_radiation_treatment = False
    if func_oncology_plan(visit_instance) and func_oncology_record(visit_instance):
        show_radiation_treatment = True
    elif not func_oncology_plan(visit_instance) and func_oncology_record(visit_instance):
        show_radiation_treatment = True
    elif func_oncology_plan(visit_instance) and not func_oncology_record(visit_instance):
        show_radiation_treatment = True
    elif not func_oncology_plan(visit_instance) and not func_oncology_record(visit_instance):
        show_radiation_treatment = False
    return show_radiation_treatment


class OncologyTreatmentPlanRuleGroup(RuleGroup):

    radiation_plan = ScheduledDataRule(
        logic=Logic(
            predicate=func_oncology,
            #predicate=('radiation_plan', 'equals', YES),
            consequence='new',
            alternative='not_required'),
        target_model=['radiationtreatment'])

    class Meta:
        app_label = 'cancer_subject'
        source_fk = (SubjectVisit, 'subject_visit')
        source_model = OncologyTreatmentPlan
site_rule_groups.register(OncologyTreatmentPlanRuleGroup)


class OncologyTreatmentRecordRuleGroup(RuleGroup):

    chemo_received = ScheduledDataRule(
        logic=Logic(
            predicate=('chemo_received', 'equals', NO),
            consequence='not_required',
            alternative='new'),
        target_model=['otrchemo'])

    radiation_received = ScheduledDataRule(
        logic=Logic(
            predicate=func_oncology,
            #predicate=('radiation_received', 'equals', YES),
            consequence='new',
            alternative='not_required'),
        target_model=['radiationtreatment'])

    surgical_therapy = ScheduledDataRule(
        logic=Logic(
            predicate=('surgical_therapy', 'equals', NO),
            consequence='not_required',
            alternative='new'),
        target_model=['otrsurgical'])

    class Meta:
        app_label = 'cancer_subject'
        source_fk = (SubjectVisit, 'subject_visit')
        source_model = OncologyTreatmentRecord
site_rule_groups.register(OncologyTreatmentRecordRuleGroup)


class OncologyTreatmentCompletedRuleGroup(RuleGroup):

    patient_had_chemo = ScheduledDataRule(
        logic=Logic(
            predicate=('patient_had_chemo', 'equals', YES),
            consequence='new',
            alternative='not_required'),
        target_model=['otrchemo'])

    patient_had_radiation = ScheduledDataRule(
        logic=Logic(
            predicate=('patient_had_radiation', 'equals', YES),
            consequence='new',
            alternative='not_required'),
        target_model=['radiationtreatment'])

    patient_had_surgery = ScheduledDataRule(
        logic=Logic(
            predicate=('patient_had_surgery', 'equals', YES),
            consequence='new',
            alternative='not_required'),
        target_model=['otrsurgical'])

    class Meta:
        app_label = 'cancer_subject'
        source_fk = (SubjectVisit, 'subject_visit')
        source_model = OncologyTreatmentCompleted
site_rule_groups.register(OncologyTreatmentCompletedRuleGroup)


class SymptomsTestingRuleGroup(RuleGroup):

    hiv_test_result = ScheduledDataRule(
        logic=Logic(
            predicate=(('hiv_result', 'ne', 'Pos'), ('hiv_test_result', 'ne', 'POS', 'or')),
            consequence='not_required',
            alternative='new'),
        target_model=['baselinehivhistory', 'bhhhivtest', 'bhhwhoillness', 'haartrecord'])

    class Meta:
        app_label = 'cancer_subject'
        source_fk = (SubjectVisit, 'subject_visit')
        source_model = SymptomsAndTesting
site_rule_groups.register(SymptomsTestingRuleGroup)


def func_haematology(visit_instance):
    haematology = ResultsToRecord.objects.get(name='haematology')
    try:
        the_diagnosis_form = CancerDiagnosis.objects.get(subject_visit=visit_instance, results_to_record__in=[haematology])
        if the_diagnosis_form:
            return True
    except CancerDiagnosis.DoesNotExist:
        return False


def func_chemistry(visit_instance):
    chemistry = ResultsToRecord.objects.get(name='chemistry')
    try:
        the_diagnosis_form = CancerDiagnosis.objects.get(subject_visit=visit_instance, results_to_record__in=[chemistry])
        if the_diagnosis_form:
            return True
    except CancerDiagnosis.DoesNotExist:
        return False


def func_tubercolosis(visit_instance):
    tb = ResultsToRecord.objects.get(name='tubercolosis')
    try:
        the_diagnosis_form = CancerDiagnosis.objects.get(subject_visit=visit_instance, results_to_record__in=[tb])
        if the_diagnosis_form:
            return True
    except CancerDiagnosis.DoesNotExist:
        return False


def func_none_selection(visit_instance):
    if_none = ResultsToRecord.objects.get(name='none')
    try:
        the_diagnosis_form = CancerDiagnosis.objects.get(subject_visit=visit_instance, results_to_record__in=[if_none])
        if the_diagnosis_form:
            return True
    except CancerDiagnosis.DoesNotExist:
        return False


class CancerDiagnosisRuleGroup(RuleGroup):

    results_to_record = ScheduledDataRule(
        logic=Logic(
            predicate=func_haematology,
            consequence='new',
            alternative='not_required'),
        target_model=['labresulthaematology'])

    results_to_record_2 = ScheduledDataRule(
        logic=Logic(
            predicate=func_chemistry,
            consequence='new',
            alternative='not_required'),
        target_model=['labresultchemistry'])

    results_to_record_3 = ScheduledDataRule(
        logic=Logic(
            predicate=func_tubercolosis,
            consequence='new',
            alternative='not_required'),
        target_model=['labresulttb'])

    results_to_record_4 = ScheduledDataRule(
        logic=Logic(
            predicate=func_none_selection,
            consequence='not_required',
            alternative='new'),
        target_model=['labresulthaematology', 'labresultchemistry', 'labresulttb'])

    class Meta:
        app_label = 'cancer_subject'
        source_fk = (SubjectVisit, 'subject_visit')
        source_model = CancerDiagnosis
site_rule_groups.register(CancerDiagnosisRuleGroup)
