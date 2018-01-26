from datetime import datetime
import os

from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
from dateutil.tz import gettz
from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings
from django.core.management.color import color_style

from edc_base.apps import AppConfig as BaseEdcBaseAppConfig
from edc_base.utils import get_utcnow
from edc_constants.constants import FAILED_ELIGIBILITY
from edc_device.apps import AppConfig as BaseEdcDeviceAppConfig
from edc_device.constants import CENTRAL_SERVER
from edc_identifier.apps import AppConfig as BaseEdcIdentifierAppConfig
from edc_lab.apps import AppConfig as BaseEdcLabAppConfig
from edc_lab_dashboard.apps import AppConfig as BaseEdcLabDashboardAppConfig
from edc_label.apps import AppConfig as BaseEdcLabelAppConfig
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig
from edc_sync_files.apps import AppConfig as BaseEdcSyncFilesAppConfig

from cancer_subject.apps import AppConfig as BaseCancerSubjectAppConfig
from edc_appointment.appointment_config import AppointmentConfig
from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
from edc_sync.apps import AppConfig as BaseEdcSyncAppConfig
from edc_timepoint.apps import AppConfig as BaseEdcTimepointAppConfig
from edc_timepoint.timepoint import Timepoint
from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, LOST_VISIT

style = color_style()


class AppConfig(DjangoAppConfig):
    name = 'cancer'
    base_template_name = 'cancer/base.html'
    dashboard_url_name = 'home_url'
    listboard_url_name = 'home_url'


class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
    protocol = 'BHP045'
    protocol_number = '045'
    protocol_name = 'Cancer'
    protocol_title = ''
    site_code = '45'
    site_name = 'Gaborone'
    study_open_datetime = datetime(2013, 10, 31, 0, 0, 0, tzinfo=gettz('UTC'))
    study_close_datetime = datetime(2022, 12, 31, 0, 0, 0, tzinfo=gettz('UTC'))


class CancerSubjectAppConfig(BaseCancerSubjectAppConfig):
    base_template_name = 'cancer/base.html'


class EdcLabDashboardAppConfig(BaseEdcLabDashboardAppConfig):
    base_template_name = 'bcpp/base.html'
    namespace = 'edc_lab_dashboard'
    result_model = 'edc_lab_dashboard.result'


class EdcLabAppConfig(BaseEdcLabAppConfig):
    base_template_name = 'cancer/base.html'
    requisition_model = 'cancer_subject.subjectrequisition'
    result_model = 'edc_lab.result'

    @property
    def study_site_name(self):
        return 'Gaborone'

    @property
    def site_code(self):
        return '45'


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'Cancer'
    institution = 'Botswana-Harvard AIDS Institute'
    copyright = '2017-{}'.format(get_utcnow().year)
    license = None


class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
    visit_models = {
        'cancer_subject': ('subject_visit', 'cancer_subject.subjectvisit')}


class EdcIdentifierAppConfig(BaseEdcIdentifierAppConfig):
    identifier_prefix = '045'


class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):
    reason_field = {'cancer_subject.subjectvisit': 'reason'}
    create_on_reasons = [SCHEDULED, UNSCHEDULED]
    delete_on_reasons = [LOST_VISIT, FAILED_ELIGIBILITY]


class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
    configurations = [
        AppointmentConfig(
            model='edc_appointment.appointment',
            related_visit_model='ambition_subject.subjectvisit',
            appt_type='hospital')]


class EdcTimepointAppConfig(BaseEdcTimepointAppConfig):
    timepoints = [
        Timepoint(
            model='cancer_subject.appointment',
            datetime_field='appt_datetime',
            status_field='appt_status',
            closed_status='DONE'
        ),
        Timepoint(
            model='cancer_subject.historicalappointment',
            datetime_field='appt_datetime',
            status_field='appt_status',
            closed_status='DONE'
        ),
    ]


class EdcSyncAppConfig(BaseEdcSyncAppConfig):
    edc_sync_files_using = True
    role = CENTRAL_SERVER


class EdcLabelAppConfig(BaseEdcLabelAppConfig):
    template_folder = os.path.join(
        settings.STATIC_ROOT, 'cancer', 'label_templates')


class EdcSyncFilesAppConfig(BaseEdcSyncFilesAppConfig):
    edc_sync_files_using = True
    role = CENTRAL_SERVER


class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
    country = 'botswana'
    definitions = {
        '7-day clinic': dict(days=[MO, TU, WE, TH, FR, SA, SU],
                             slots=[100, 100, 100, 100, 100, 100, 100]),
        '5-day clinic': dict(days=[MO, TU, WE, TH, FR],
                             slots=[100, 100, 100, 100, 100])}
