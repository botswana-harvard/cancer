from collections import OrderedDict

from edc.subject.visit_schedule.classes import VisitScheduleConfiguration, site_visit_schedules, EntryTuple, MembershipFormTuple, ScheduleGroupTuple
from edc.constants import REQUIRED, NOT_REQUIRED, ADDITIONAL, NOT_ADDITIONAL

from ..models import EnrollmentChecklist, SubjectVisit


class SubjectMonthlyVisitSchedule(VisitScheduleConfiguration):

    name = 'subject visit schedule'
    app_label = 'cancer_subject'
    # membership forms
    # (name, model, visible)
    membership_forms = OrderedDict({
        'subject_enrollment': MembershipFormTuple('subject_enrollment', EnrollmentChecklist, True),
        })

    # schedule groups
    # (name, membership_form_name, grouping_key, comment)
    schedule_groups = OrderedDict({
        'Subject Enrollment': ScheduleGroupTuple('Subject Enrollment', 'subject_enrollment', None, None),
        })
    # visit_schedule
    # see edc.subject.visit_schedule.models.visit_defintion
    visit_definitions = OrderedDict()

    visit_definitions['1000'] = {
            'title': 'Enrollment Visit',
            'time_point': 0,
            'base_interval': 0,
            'base_interval_unit': 'D',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 45,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': SubjectVisit,
            'schedule_group': 'Subject Enrollment',
            'instructions': None,
            'requisitions': (),
            'entries': (
                EntryTuple(10L, u'cancer_subject', u'locator', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'cancer_subject', u'symptomsandtesting', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'cancer_subject', u'labresultheightweight', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(40L, u'cancer_subject', u'activityandfunctioning', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(60L, u'cancer_subject', u'baseriskassessmentdemo', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(70L, u'cancer_subject', u'baseriskassessment', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(80L, u'cancer_subject', u'baseriskassessmentfemale', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(90L, u'cancer_subject', u'baseriskassessmentcancer', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(100L, u'cancer_subject', u'baseriskassessmentsun', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(110L, u'cancer_subject', u'baseriskassessmentfuel', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(120L, u'cancer_subject', u'baseriskassessmentchemical', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(130L, u'cancer_subject', u'baseriskassessmentmining', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(140L, u'cancer_subject', u'baseriskassessmenteating', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(150L, u'cancer_subject', u'baseriskassessmentsmoking', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(160L, u'cancer_subject', u'baseriskassessmentalcohol', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(170L, u'cancer_subject', u'cancerdiagnosis', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(180L, u'cancer_subject', u'oncologytreatmentplan', REQUIRED, NOT_ADDITIONAL),
                #now not required
                #EntryTuple(190L, u'cancer_subject', u'labresult', REQUIRED, NOT_ADDITIONAL),
                #EntryTuple(200L, u'cancer_subject', u'labresulthiv', REQUIRED, NOT_ADDITIONAL),
                #removed on upgrade
                #EntryTuple(210L, u'cancer_subject', u'labresultcd4', REQUIRED, NOT_ADDITIONAL),
                #EntryTuple(220L, u'cancer_subject', u'labresultviralload', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(230L, u'cancer_subject', u'labresulthaematology', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(240L, u'cancer_subject', u'labresultchemistry', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(250L, u'cancer_subject', u'labresulttb', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(260L, u'cancer_subject', u'baselinehivhistory', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(270L, u'cancer_subject', u'bhhhivtest', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(280L, u'cancer_subject', u'bhhwhoillness', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(290L, u'cancer_subject', u'haartrecord', REQUIRED, NOT_ADDITIONAL),
                #EntryTuple(290L, u'cancer_subject', u'bhhcd4', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(300L, u'cancer_subject', u'oncologytreatmentrecord', REQUIRED, NOT_ADDITIONAL),
                #to be removed completely
                #EntryTuple(320L, u'cancer_subject', u'otrradiation', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(310L, u'cancer_subject', u'otrsurgical', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(320L, u'cancer_subject', u'otrchemo', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(330L, u'cancer_subject', u'radiationtreatment', REQUIRED, NOT_ADDITIONAL),
                #added on upgrade
                #EntryTuple(350L, u'cancer_subject', u'radiationtreatment', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(1000L, u'cancer_subject', u'subjectdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(1010L, u'cancer_subject', u'subjectoffstudy', NOT_REQUIRED, ADDITIONAL),
            )}
    visit_definitions['1300'] = {
            'title': '1300: Follow-up Visit',
            'time_point': 30,
            'base_interval': 3,
            'base_interval_unit': 'M',
            'window_lower_bound': 44,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 45,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': SubjectVisit,
            'schedule_group': 'Subject Enrollment',
            'instructions': None,
            'requisitions': (),
            'entries': (
                EntryTuple(10L, u'cancer_subject', u'activityandfunctioning', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'cancer_subject', u'currentsymptoms', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'cancer_subject', u'oncologytreatmentcompleted', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(40L, u'cancer_subject', u'otrchemo', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(50L, u'cancer_subject', u'radiationtreatment', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(60L, u'cancer_subject', u'otrsurgical', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(1000L, u'cancer_subject', u'subjectdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(1010L, u'cancer_subject', u'subjectoffstudy', NOT_REQUIRED, ADDITIONAL),
                )}
    visit_definitions['1600'] = {
            'title': '1600: Follow-up Visit',
            'time_point': 60,
            'base_interval': 6,
            'base_interval_unit': 'M',
            'window_lower_bound': 44,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 45,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': SubjectVisit,
            'schedule_group': 'Subject Enrollment',
            'instructions': None,
            'requisitions': (),
            'entries': (
                EntryTuple(10L, u'cancer_subject', u'activityandfunctioning', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'cancer_subject', u'currentsymptoms', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'cancer_subject', u'oncologytreatmentcompleted', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(40L, u'cancer_subject', u'otrchemo', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(50L, u'cancer_subject', u'radiationtreatment', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(60L, u'cancer_subject', u'otrsurgical', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(1000L, u'cancer_subject', u'subjectdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(1010L, u'cancer_subject', u'subjectoffstudy', NOT_REQUIRED, ADDITIONAL),
                )}
    visit_definitions['1900'] = {
            'title': '1900: Follow-up Visit',
            'time_point': 90,
            'base_interval': 9,
            'base_interval_unit': 'M',
            'window_lower_bound': 44,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 45,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': SubjectVisit,
            'schedule_group': 'Subject Enrollment',
            'instructions': None,
            'requisitions': (),
            'entries': (
                EntryTuple(10L, u'cancer_subject', u'activityandfunctioning', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'cancer_subject', u'currentsymptoms', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'cancer_subject', u'oncologytreatmentcompleted', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(40L, u'cancer_subject', u'otrchemo', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(50L, u'cancer_subject', u'radiationtreatment', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(60L, u'cancer_subject', u'otrsurgical', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(1000L, u'cancer_subject', u'subjectdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(1010L, u'cancer_subject', u'subjectoffstudy', NOT_REQUIRED, ADDITIONAL),
                )}
    visit_definitions['2200'] = {
            'title': '2200: Follow-up Visit',
            'time_point': 220,
            'base_interval': 12,
            'base_interval_unit': 'M',
            'window_lower_bound': 44,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 45,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': SubjectVisit,
            'schedule_group': 'Subject Enrollment',
            'instructions': None,
            'requisitions': (),
            'entries': (
                EntryTuple(10L, u'cancer_subject', u'activityandfunctioning', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'cancer_subject', u'currentsymptoms', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'cancer_subject', u'oncologytreatmentcompleted', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(40L, u'cancer_subject', u'otrchemo', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(50L, u'cancer_subject', u'radiationtreatment', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(60L, u'cancer_subject', u'otrsurgical', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(1000L, u'cancer_subject', u'subjectdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(1010L, u'cancer_subject', u'subjectoffstudy', NOT_REQUIRED, ADDITIONAL),
                )}
    visit_definitions['2500'] = {
            'title': '2500: Follow-up Visit',
            'time_point': 250,
            'base_interval': 15,
            'base_interval_unit': 'M',
            'window_lower_bound': 44,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 45,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': SubjectVisit,
            'schedule_group': 'Subject Enrollment',
            'instructions': None,
            'requisitions': (),
            'entries': (
                EntryTuple(10L, u'cancer_subject', u'activityandfunctioning', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'cancer_subject', u'currentsymptoms', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(1000L, u'cancer_subject', u'subjectdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(1010L, u'cancer_subject', u'subjectoffstudy', NOT_REQUIRED, ADDITIONAL),
                )}
    visit_definitions['2800'] = {
            'title': '2800: Follow-up Visit',
            'time_point': 280,
            'base_interval': 18,
            'base_interval_unit': 'M',
            'window_lower_bound': 44,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 45,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': SubjectVisit,
            'schedule_group': 'Subject Enrollment',
            'instructions': None,
            'requisitions': (),
            'entries': (
                EntryTuple(10L, u'cancer_subject', u'activityandfunctioning', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'cancer_subject', u'currentsymptoms', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(1000L, u'cancer_subject', u'subjectdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(1010L, u'cancer_subject', u'subjectoffstudy', NOT_REQUIRED, ADDITIONAL),
                )}
    visit_definitions['3100'] = {
            'title': '3100: Follow-up Visit',
            'time_point': 310,
            'base_interval': 21,
            'base_interval_unit': 'M',
            'window_lower_bound': 44,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 45,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': SubjectVisit,
            'schedule_group': 'Subject Enrollment',
            'instructions': None,
            'requisitions': (),
            'entries': (
                EntryTuple(10L, u'cancer_subject', u'activityandfunctioning', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'cancer_subject', u'currentsymptoms', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(1000L, u'cancer_subject', u'subjectdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(1010L, u'cancer_subject', u'subjectoffstudy', NOT_REQUIRED, ADDITIONAL),
                )}
    visit_definitions['3400'] = {
            'title': '3400: Follow-up Visit',
            'time_point': 340,
            'base_interval': 24,
            'base_interval_unit': 'M',
            'window_lower_bound': 44,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 45,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': SubjectVisit,
            'schedule_group': 'Subject Enrollment',
            'instructions': None,
            'requisitions': (),
            'entries': (
                EntryTuple(10L, u'cancer_subject', u'activityandfunctioning', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'cancer_subject', u'currentsymptoms', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(1000L, u'cancer_subject', u'subjectdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(1010L, u'cancer_subject', u'subjectoffstudy', NOT_REQUIRED, ADDITIONAL),
                )}
    visit_definitions['3700'] = {
            'title': '3700: Follow-up Visit',
            'time_point': 370,
            'base_interval': 27,
            'base_interval_unit': 'M',
            'window_lower_bound': 44,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 45,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': SubjectVisit,
            'schedule_group': 'Subject Enrollment',
            'instructions': None,
            'requisitions': (),
            'entries': (
                EntryTuple(10L, u'cancer_subject', u'activityandfunctioning', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'cancer_subject', u'currentsymptoms', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(1000L, u'cancer_subject', u'subjectdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(1010L, u'cancer_subject', u'subjectoffstudy', NOT_REQUIRED, ADDITIONAL),
                )}
    visit_definitions['4000'] = {
            'title': '4000: Follow-up Visit',
            'time_point': 400,
            'base_interval': 30,
            'base_interval_unit': 'M',
            'window_lower_bound': 44,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 45,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': SubjectVisit,
            'schedule_group': 'Subject Enrollment',
            'instructions': None,
            'requisitions': (),
            'entries': (
                EntryTuple(10L, u'cancer_subject', u'activityandfunctioning', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'cancer_subject', u'currentsymptoms', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(1000L, u'cancer_subject', u'subjectdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(1010L, u'cancer_subject', u'subjectoffstudy', NOT_REQUIRED, ADDITIONAL),
                )}
    visit_definitions['4300'] = {
            'title': '4300: Follow-up Visit',
            'time_point': 430,
            'base_interval': 33,
            'base_interval_unit': 'M',
            'window_lower_bound': 44,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 45,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': SubjectVisit,
            'schedule_group': 'Subject Enrollment',
            'instructions': None,
            'requisitions': (),
            'entries': (
                EntryTuple(10L, u'cancer_subject', u'activityandfunctioning', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'cancer_subject', u'currentsymptoms', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(1000L, u'cancer_subject', u'subjectdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(1010L, u'cancer_subject', u'subjectoffstudy', NOT_REQUIRED, ADDITIONAL),
                )}
    visit_definitions['4600'] = {
            'title': '4600: Follow-up Visit',
            'time_point': 460,
            'base_interval': 36,
            'base_interval_unit': 'M',
            'window_lower_bound': 44,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 45,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': SubjectVisit,
            'schedule_group': 'Subject Enrollment',
            'instructions': None,
            'requisitions': (),
            'entries': (
                EntryTuple(10L, u'cancer_subject', u'activityandfunctioning', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'cancer_subject', u'currentsymptoms', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(1000L, u'cancer_subject', u'subjectdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(1010L, u'cancer_subject', u'subjectoffstudy', NOT_REQUIRED, ADDITIONAL),
                )}
    visit_definitions['4900'] = {
            'title': '4900: Follow-up Visit',
            'time_point': 490,
            'base_interval': 39,
            'base_interval_unit': 'M',
            'window_lower_bound': 44,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 45,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': SubjectVisit,
            'schedule_group': 'Subject Enrollment',
            'instructions': None,
            'requisitions': (),
            'entries': (
                EntryTuple(10L, u'cancer_subject', u'activityandfunctioning', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'cancer_subject', u'currentsymptoms', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(1000L, u'cancer_subject', u'subjectdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(1010L, u'cancer_subject', u'subjectoffstudy', NOT_REQUIRED, ADDITIONAL),
                )}
    visit_definitions['5200'] = {
            'title': '5200: Follow-up Visit',
            'time_point': 520,
            'base_interval': 42,
            'base_interval_unit': 'M',
            'window_lower_bound': 44,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 45,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': SubjectVisit,
            'schedule_group': 'Subject Enrollment',
            'instructions': None,
            'requisitions': (),
            'entries': (
                EntryTuple(10L, u'cancer_subject', u'activityandfunctioning', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'cancer_subject', u'currentsymptoms', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(1000L, u'cancer_subject', u'subjectdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(1010L, u'cancer_subject', u'subjectoffstudy', NOT_REQUIRED, ADDITIONAL),
                )}
    visit_definitions['5500'] = {
            'title': '5500: Follow-up Visit',
            'time_point': 550,
            'base_interval': 45,
            'base_interval_unit': 'M',
            'window_lower_bound': 44,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 45,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': SubjectVisit,
            'schedule_group': 'Subject Enrollment',
            'instructions': None,
            'requisitions': (),
            'entries': (
                EntryTuple(10L, u'cancer_subject', u'activityandfunctioning', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'cancer_subject', u'currentsymptoms', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(1000L, u'cancer_subject', u'subjectdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(1010L, u'cancer_subject', u'subjectoffstudy', NOT_REQUIRED, ADDITIONAL),
                )}
    visit_definitions['5800'] = {
            'title': '5800: Follow-up Visit',
            'time_point': 580,
            'base_interval': 48,
            'base_interval_unit': 'M',
            'window_lower_bound': 44,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 45,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': SubjectVisit,
            'schedule_group': 'Subject Enrollment',
            'instructions': None,
            'requisitions': (),
            'entries': (
                EntryTuple(10L, u'cancer_subject', u'activityandfunctioning', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'cancer_subject', u'currentsymptoms', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(1000L, u'cancer_subject', u'subjectdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(1010L, u'cancer_subject', u'subjectoffstudy', NOT_REQUIRED, ADDITIONAL),
                )}
    visit_definitions['6100'] = {
            'title': '6100: Follow-up Visit',
            'time_point': 610,
            'base_interval': 51,
            'base_interval_unit': 'M',
            'window_lower_bound': 44,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 45,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': SubjectVisit,
            'schedule_group': 'Subject Enrollment',
            'instructions': None,
            'requisitions': (),
            'entries': (
                EntryTuple(10L, u'cancer_subject', u'activityandfunctioning', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'cancer_subject', u'currentsymptoms', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(1000L, u'cancer_subject', u'subjectdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(1010L, u'cancer_subject', u'subjectoffstudy', NOT_REQUIRED, ADDITIONAL),
                )}
    visit_definitions['6400'] = {
            'title': '6400: Follow-up Visit',
            'time_point': 640,
            'base_interval': 54,
            'base_interval_unit': 'M',
            'window_lower_bound': 44,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 45,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': SubjectVisit,
            'schedule_group': 'Subject Enrollment',
            'instructions': None,
            'requisitions': (),
            'entries': (
                EntryTuple(10L, u'cancer_subject', u'activityandfunctioning', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'cancer_subject', u'currentsymptoms', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(1000L, u'cancer_subject', u'subjectdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(1010L, u'cancer_subject', u'subjectoffstudy', NOT_REQUIRED, ADDITIONAL),
                )}
    visit_definitions['6700'] = {
            'title': '6700: Follow-up Visit',
            'time_point': 670,
            'base_interval': 57,
            'base_interval_unit': 'M',
            'window_lower_bound': 44,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 45,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': SubjectVisit,
            'schedule_group': 'Subject Enrollment',
            'instructions': None,
            'requisitions': (),
            'entries': (
                EntryTuple(10L, u'cancer_subject', u'activityandfunctioning', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'cancer_subject', u'currentsymptoms', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(1000L, u'cancer_subject', u'subjectdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(1010L, u'cancer_subject', u'subjectoffstudy', NOT_REQUIRED, ADDITIONAL),
                )}
    visit_definitions['7000'] = {
            'title': '7000: Follow-up Visit',
            'time_point': 700,
            'base_interval': 60,
            'base_interval_unit': 'M',
            'window_lower_bound': 44,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 45,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': SubjectVisit,
            'schedule_group': 'Subject Enrollment',
            'instructions': None,
            'requisitions': (),
            'entries': (
                EntryTuple(10L, u'cancer_subject', u'activityandfunctioning', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'cancer_subject', u'currentsymptoms', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(1000L, u'cancer_subject', u'subjectdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(1010L, u'cancer_subject', u'subjectoffstudy', NOT_REQUIRED, ADDITIONAL),
                )}
site_visit_schedules.register(SubjectMonthlyVisitSchedule)
