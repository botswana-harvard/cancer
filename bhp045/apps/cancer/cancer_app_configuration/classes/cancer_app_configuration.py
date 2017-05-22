from datetime import datetime, date

from edc.apps.app_configuration.classes import BaseAppConfiguration
from edc.core.bhp_variables.models import StudySpecific, StudySite
from edc.device.device.classes import device

study_start_datetime = datetime(2010, 05, 02, 7, 30, 00)
study_end_datetime = datetime(2020, 05, 01, 7, 00, 00)


class CancerAppConfiguration(BaseAppConfiguration):

    def prepare(self):
        super(CancerAppConfiguration, self).prepare()

    global_configuration = {
            'dashboard':
                {'show_not_required_metadata': False,
                 'allow_additional_requisitions': False,
                 'show_drop_down_requisitions': True},
            'appointment':
                {'allowed_iso_weekdays': '12345',
                 'use_same_weekday': True,
                 'default_appt_type': 'default'},
                                 }

    study_variables_setup = {
                'protocol_number': 'BHP045',
                'protocol_code': '045',
                'protocol_title': 'BHP045',
                'research_title': 'BHP045',
                'study_start_datetime': study_start_datetime,
                'minimum_age_of_consent': 16,
                'maximum_age_of_consent': 120,
                'gender_of_consent': 'MF',
                'subject_identifier_seed': '10000',
                'subject_identifier_prefix': '045',
                'subject_identifier_modulus': '7',
                'subject_type': 'subject',
                'machine_type': 'SERVER',
                'hostname_prefix': 's007',
                'device_id': device.device_id}

    holidays_setup = {
        'New Year': date(2015, 1, 01),
        'New Year Holiday': date(2015, 1, 02),
#         'Good Fiday': date(2014, 4, 18),
#         'Easter Monday': date(2014, 4, 21),
#         'Labour Day': date(2014, 5, 01),
#         'Ascension Day': date(2014, 5, 29),
#         'Sir Seretse Khama Day': date(2014, 7, 01),
#         'President\'s Day': date(2014, 7, 17),
#         'President\'s Day Holiday': date(2014, 7, 21),
        'Independence Day': date(2015, 9, 30),
        'Botswana Day Holiday': date(2015, 10, 01),
        'Christmas Day': date(2015, 12, 25),
        'Boxing Day': date(2015, 12, 26),
        }

    consent_catalogue_setup = {
                'name': 'cancer',
                'content_type_map': 'subjectconsent',
                'consent_type': 'study',
                'version': 1,
                'start_datetime': study_start_datetime,
                'end_datetime': study_end_datetime,
                'add_for_app': 'cancer_subject'}

    study_site_setup = [{'site_name': 'Gaborone', 'site_code': '040'},
                        {'site_name': 'Francistown', 'site_code': '060'},
                        ]

    consent_catalogue_list = [consent_catalogue_setup]

    lab_clinic_api_setup = {
        'panel': [],
        'aliquot_type': []}

    lab_setup = {'cancer': {
                    'panel': [],
                    'aliquot_type': [],
                     'profile': [],
                     'profile_item': []}}

    def update_or_create_study_variables(self):
        if StudySpecific.objects.all().count() == 0:
            StudySpecific.objects.create(**self.study_variables_setup)
        else:
            StudySpecific.objects.all().update(**self.study_variables_setup)
        self._setup_study_sites()

    def _setup_study_sites(self):
        for site in self.study_site_setup:
            try:
                StudySite.objects.get(**site)
            except StudySite.DoesNotExist:
                StudySite.objects.create(**site)

cancer_app_configuration = CancerAppConfiguration()
