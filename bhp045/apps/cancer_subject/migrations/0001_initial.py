# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SubjectConsentAudit'
        db.create_table('cancer_subject_subjectconsent_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_identifier', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=36, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True)),
            ('initials', self.gf('django.db.models.fields.CharField')(max_length=3, null=True)),
            ('dob', self.gf('django.db.models.fields.DateField')(null=True)),
            ('is_dob_estimated', self.gf('django.db.models.fields.CharField')(max_length=25, null=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1, null=True)),
            ('subject_type', self.gf('django.db.models.fields.CharField')(default='undetermined', max_length=25, null=True)),
            ('study_site', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_subjectconsent', to=orm['bhp_variables.StudySite'])),
            ('consent_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('guardian_name', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True, blank=True)),
            ('may_store_samples', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('is_verified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_verified_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('identity', self.gf('django.db.models.fields.CharField')(max_length=78L)),
            ('identity_type', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('confirm_identity', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True)),
            ('original_identifier', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('is_incarcerated', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['SubjectConsentAudit'])

        # Adding model 'SubjectConsent'
        db.create_table('cancer_subject_subjectconsent', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_identifier', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=36, null=True, blank=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True)),
            ('initials', self.gf('django.db.models.fields.CharField')(max_length=3, null=True)),
            ('dob', self.gf('django.db.models.fields.DateField')(null=True)),
            ('is_dob_estimated', self.gf('django.db.models.fields.CharField')(max_length=25, null=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1, null=True)),
            ('subject_type', self.gf('django.db.models.fields.CharField')(default='undetermined', max_length=25, null=True)),
            ('study_site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_variables.StudySite'])),
            ('consent_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('guardian_name', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True, blank=True)),
            ('may_store_samples', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('is_verified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_verified_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('identity', self.gf('django.db.models.fields.CharField')(unique=True, max_length=78L)),
            ('identity_type', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('confirm_identity', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True)),
            ('original_identifier', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('is_incarcerated', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('cancer_subject', ['SubjectConsent'])

        # Adding model 'SubjectDeathAudit'
        db.create_table('cancer_subject_subjectdeath_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('death_date', self.gf('django.db.models.fields.DateField')()),
            ('death_cause_info', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_subjectdeath', to=orm['bhp_adverse.DeathCauseInfo'])),
            ('death_cause_info_other', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('death_cause', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('death_cause_category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_subjectdeath', to=orm['bhp_adverse.DeathCauseCategory'])),
            ('death_cause_other', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('death_medical_responsibility', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_subjectdeath', to=orm['bhp_adverse.DeathMedicalResponsibility'])),
            ('participant_hospitalized', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('death_reason_hospitalized', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='_audit_subjectdeath', null=True, to=orm['bhp_adverse.DeathReasonHospitalized'])),
            ('days_hospitalized', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('illness_duration', self.gf('django.db.models.fields.IntegerField')()),
            ('perform_autopsy', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('dx_code', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_subjectdeath', max_length=25, to=orm['bhp_code_lists.DxCode'])),
            ('comment', self.gf('django.db.models.fields.TextField')(max_length=500, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('registered_subject', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_subjectdeath', to=orm['bhp_registration.RegisteredSubject'])),
        ))
        db.send_create_signal('cancer_subject', ['SubjectDeathAudit'])

        # Adding model 'SubjectDeath'
        db.create_table('cancer_subject_subjectdeath', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('registered_subject', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True)),
            ('death_date', self.gf('django.db.models.fields.DateField')()),
            ('death_cause_info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_adverse.DeathCauseInfo'])),
            ('death_cause_info_other', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('death_cause', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('death_cause_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_adverse.DeathCauseCategory'])),
            ('death_cause_other', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('death_medical_responsibility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_adverse.DeathMedicalResponsibility'])),
            ('participant_hospitalized', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('death_reason_hospitalized', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_adverse.DeathReasonHospitalized'], null=True, blank=True)),
            ('days_hospitalized', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('illness_duration', self.gf('django.db.models.fields.IntegerField')()),
            ('perform_autopsy', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('dx_code', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_code_lists.DxCode'], max_length=25)),
            ('comment', self.gf('django.db.models.fields.TextField')(max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal('cancer_subject', ['SubjectDeath'])

        # Adding model 'SubjectOffStudyAudit'
        db.create_table('cancer_subject_subjectoffstudy_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('offstudy_date', self.gf('django.db.models.fields.DateField')()),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('reason_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(max_length=250, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('registered_subject', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_subjectoffstudy', to=orm['bhp_registration.RegisteredSubject'])),
        ))
        db.send_create_signal('cancer_subject', ['SubjectOffStudyAudit'])

        # Adding model 'SubjectOffStudy'
        db.create_table('cancer_subject_subjectoffstudy', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('registered_subject', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True)),
            ('offstudy_date', self.gf('django.db.models.fields.DateField')()),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('reason_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal('cancer_subject', ['SubjectOffStudy'])

        # Adding model 'SubjectVisitAudit'
        db.create_table('cancer_subject_subjectvisit_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('reason_missed', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('info_source', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('info_source_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(max_length=250, null=True, blank=True)),
            ('reason_unscheduled', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('appointment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_subjectvisit', to=orm['bhp_appointment.Appointment'])),
        ))
        db.send_create_signal('cancer_subject', ['SubjectVisitAudit'])

        # Adding model 'SubjectVisit'
        db.create_table('cancer_subject_subjectvisit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('appointment', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_appointment.Appointment'], unique=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('reason_missed', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('info_source', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('info_source_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(max_length=250, null=True, blank=True)),
            ('reason_unscheduled', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
        ))
        db.send_create_signal('cancer_subject', ['SubjectVisit'])

        # Adding model 'EnrollmentChecklistAudit'
        db.create_table('cancer_subject_enrollmentchecklist_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('registration_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('has_diagnosis', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('registered_subject', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_enrollmentchecklist', to=orm['bhp_registration.RegisteredSubject'])),
        ))
        db.send_create_signal('cancer_subject', ['EnrollmentChecklistAudit'])

        # Adding model 'EnrollmentChecklist'
        db.create_table('cancer_subject_enrollmentchecklist', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('registered_subject', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True)),
            ('registration_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('has_diagnosis', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('cancer_subject', ['EnrollmentChecklist'])

        # Adding model 'BaseRiskAssessmentAudit'
        db.create_table('cancer_subject_baseriskassessment_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_baseriskassessment', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('participant_interviewed', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('hepatitis', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('tuberculosis', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('year_tb', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('has_worked_mine', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('has_smoked', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('age_firstsex', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('has_alcohol', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('tradmedicine', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('is_albino', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['BaseRiskAssessmentAudit'])

        # Adding model 'BaseRiskAssessment'
        db.create_table('cancer_subject_baseriskassessment', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('participant_interviewed', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('hepatitis', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('tuberculosis', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('year_tb', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('has_worked_mine', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('has_smoked', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('age_firstsex', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('has_alcohol', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('tradmedicine', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('is_albino', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('cancer_subject', ['BaseRiskAssessment'])

        # Adding model 'BaseRiskAssessmentSmokingAudit'
        db.create_table('cancer_subject_baseriskassessmentsmoking_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_baseriskassessmentsmoking', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('smoke_now', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('cigarette_smoking', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('years_smoked', self.gf('django.db.models.fields.IntegerField')()),
            ('cigarette_smoked', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('when_quit', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('years_smoked_before', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['BaseRiskAssessmentSmokingAudit'])

        # Adding model 'BaseRiskAssessmentSmoking'
        db.create_table('cancer_subject_baseriskassessmentsmoking', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('smoke_now', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('cigarette_smoking', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('years_smoked', self.gf('django.db.models.fields.IntegerField')()),
            ('cigarette_smoked', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('when_quit', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('years_smoked_before', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('cancer_subject', ['BaseRiskAssessmentSmoking'])

        # Adding model 'BaseRiskAssessmentSunAudit'
        db.create_table('cancer_subject_baseriskassessmentsun_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_baseriskassessmentsun', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('hours_outdoor', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('sleeved_shirt', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('hat', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('shade_umbrella', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('sunglasses', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['BaseRiskAssessmentSunAudit'])

        # Adding model 'BaseRiskAssessmentSun'
        db.create_table('cancer_subject_baseriskassessmentsun', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('hours_outdoor', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('sleeved_shirt', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('hat', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('shade_umbrella', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('sunglasses', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('cancer_subject', ['BaseRiskAssessmentSun'])

        # Adding model 'BaseRiskAssessmentMiningAudit'
        db.create_table('cancer_subject_baseriskassessmentmining_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_baseriskassessmentmining', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('mine_time', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('mine_type', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('mine_prompt_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('mine_underground', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('mine_underground_time', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('last_mine', self.gf('django.db.models.fields.DateField')(max_length=25)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['BaseRiskAssessmentMiningAudit'])

        # Adding model 'BaseRiskAssessmentMining'
        db.create_table('cancer_subject_baseriskassessmentmining', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('mine_time', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('mine_type', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('mine_prompt_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('mine_underground', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('mine_underground_time', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('last_mine', self.gf('django.db.models.fields.DateField')(max_length=25)),
        ))
        db.send_create_signal('cancer_subject', ['BaseRiskAssessmentMining'])

        # Adding model 'BaseRiskAssessmentAlcoholAudit'
        db.create_table('cancer_subject_baseriskassessmentalcohol_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_baseriskassessmentalcohol', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('alcohol_weekly', self.gf('django.db.models.fields.IntegerField')()),
            ('amount_drinking', self.gf('django.db.models.fields.IntegerField')()),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['BaseRiskAssessmentAlcoholAudit'])

        # Adding model 'BaseRiskAssessmentAlcohol'
        db.create_table('cancer_subject_baseriskassessmentalcohol', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('alcohol_weekly', self.gf('django.db.models.fields.IntegerField')()),
            ('amount_drinking', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('cancer_subject', ['BaseRiskAssessmentAlcohol'])

        # Adding model 'BaseRiskAssessmentFemaleAudit'
        db.create_table('cancer_subject_baseriskassessmentfemale_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_baseriskassessmentfemale', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('age_period', self.gf('django.db.models.fields.IntegerField')()),
            ('children', self.gf('django.db.models.fields.IntegerField')()),
            ('years_breastfed', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['BaseRiskAssessmentFemaleAudit'])

        # Adding model 'BaseRiskAssessmentFemale'
        db.create_table('cancer_subject_baseriskassessmentfemale', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('age_period', self.gf('django.db.models.fields.IntegerField')()),
            ('children', self.gf('django.db.models.fields.IntegerField')()),
            ('years_breastfed', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('cancer_subject', ['BaseRiskAssessmentFemale'])

        # Adding model 'BaseRiskAssessmentChemicalAudit'
        db.create_table('cancer_subject_baseriskassessmentchemical_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_baseriskassessmentchemical', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('asbestos', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('asbestos_no_protection', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('chemicals', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('chemicals_time', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('arsenic_smelting', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('total_time_no_protection', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['BaseRiskAssessmentChemicalAudit'])

        # Adding model 'BaseRiskAssessmentChemical'
        db.create_table('cancer_subject_baseriskassessmentchemical', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('asbestos', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('asbestos_no_protection', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('chemicals', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('chemicals_time', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('arsenic_smelting', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('total_time_no_protection', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
        ))
        db.send_create_signal('cancer_subject', ['BaseRiskAssessmentChemical'])

        # Adding model 'BaseRiskAssessmentFuelAudit'
        db.create_table('cancer_subject_baseriskassessmentfuel_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_baseriskassessmentfuel', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('fuel_20y', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('fuel_20y_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('cooking', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('fuel_mm', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('fuel_mm_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('cooking_mm', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['BaseRiskAssessmentFuelAudit'])

        # Adding model 'BaseRiskAssessmentFuel'
        db.create_table('cancer_subject_baseriskassessmentfuel', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('fuel_20y', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('fuel_20y_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('cooking', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('fuel_mm', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('fuel_mm_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('cooking_mm', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal('cancer_subject', ['BaseRiskAssessmentFuel'])

        # Adding model 'BaseRiskAssessmentCancerAudit'
        db.create_table('cancer_subject_baseriskassessmentcancer_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_baseriskassessmentcancer', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('family_cancer', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('family_cancer_type', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('family_cancer_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('had_previous_cancer', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('previous_cancer', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('previous_cancer_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['BaseRiskAssessmentCancerAudit'])

        # Adding model 'BaseRiskAssessmentCancer'
        db.create_table('cancer_subject_baseriskassessmentcancer', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('family_cancer', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('family_cancer_type', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('family_cancer_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('had_previous_cancer', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('previous_cancer', self.gf('django.db.models.fields.CharField')(max_length=45, blank=True)),
            ('previous_cancer_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
        ))
        db.send_create_signal('cancer_subject', ['BaseRiskAssessmentCancer'])

        # Adding model 'BaseRiskAssessmentDemoAudit'
        db.create_table('cancer_subject_baseriskassessmentdemo_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_baseriskassessmentdemo', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('marital_status', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('marital_status_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('race', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('race_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('ethnic_grp', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('ethnic_grp_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('district20', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('setting20', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=65)),
            ('setting', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('education', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('occupation_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('money_provide', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('money_provide_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('money_earned', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('electricity', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('toilet', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('toilet_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('household_people', self.gf('django.db.models.fields.IntegerField')()),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['BaseRiskAssessmentDemoAudit'])

        # Adding model 'BaseRiskAssessmentDemo'
        db.create_table('cancer_subject_baseriskassessmentdemo', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('marital_status', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('marital_status_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('race', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('race_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('ethnic_grp', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('ethnic_grp_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('district20', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('setting20', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=65)),
            ('setting', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('education', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('occupation_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('money_provide', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('money_provide_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('money_earned', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('electricity', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('toilet', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('toilet_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('household_people', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('cancer_subject', ['BaseRiskAssessmentDemo'])

        # Adding model 'BaseRiskAssessmentEatingAudit'
        db.create_table('cancer_subject_baseriskassessmenteating_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_baseriskassessmenteating', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('five_fruit', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('meals_weekly', self.gf('django.db.models.fields.IntegerField')()),
            ('meal_sorghum', self.gf('django.db.models.fields.IntegerField')()),
            ('meal_millet', self.gf('django.db.models.fields.IntegerField')()),
            ('meal_rice', self.gf('django.db.models.fields.IntegerField')()),
            ('meal_peanuts', self.gf('django.db.models.fields.IntegerField')()),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['BaseRiskAssessmentEatingAudit'])

        # Adding model 'BaseRiskAssessmentEating'
        db.create_table('cancer_subject_baseriskassessmenteating', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('five_fruit', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('meals_weekly', self.gf('django.db.models.fields.IntegerField')()),
            ('meal_sorghum', self.gf('django.db.models.fields.IntegerField')()),
            ('meal_millet', self.gf('django.db.models.fields.IntegerField')()),
            ('meal_rice', self.gf('django.db.models.fields.IntegerField')()),
            ('meal_peanuts', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('cancer_subject', ['BaseRiskAssessmentEating'])

        # Adding model 'CancerDiagnosisAudit'
        db.create_table('cancer_subject_cancerdiagnosis_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_cancerdiagnosis', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('diagnosis', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('cancer_category', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('symptom_prompt', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('symptom_prompt_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('symptom_first_noticed', self.gf('django.db.models.fields.DateField')(max_length=25)),
            ('first_evaluation', self.gf('django.db.models.fields.DateField')(max_length=25)),
            ('trad_evaluation', self.gf('django.db.models.fields.DateField')(max_length=25, null=True, blank=True)),
            ('date_diagnosed', self.gf('django.db.models.fields.DateField')(max_length=25, null=True, blank=True)),
            ('diagnosis_basis', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('diagnosis_basis_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('diagnosis_word', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cancer_site', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('clinical_diagnosis', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('tumour', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('tumour_basis', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('lymph_nodes', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('lymph_basis', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('metastasis', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('metastasis_basis', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('cancer_stage', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('cancer_stage_modifier', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['CancerDiagnosisAudit'])

        # Adding model 'CancerDiagnosis'
        db.create_table('cancer_subject_cancerdiagnosis', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('diagnosis', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('cancer_category', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('symptom_prompt', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('symptom_prompt_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('symptom_first_noticed', self.gf('django.db.models.fields.DateField')(max_length=25)),
            ('first_evaluation', self.gf('django.db.models.fields.DateField')(max_length=25)),
            ('trad_evaluation', self.gf('django.db.models.fields.DateField')(max_length=25, null=True, blank=True)),
            ('date_diagnosed', self.gf('django.db.models.fields.DateField')(max_length=25, null=True, blank=True)),
            ('diagnosis_basis', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('diagnosis_basis_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('diagnosis_word', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cancer_site', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('clinical_diagnosis', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('tumour', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('tumour_basis', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('lymph_nodes', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('lymph_basis', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('metastasis', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('metastasis_basis', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('cancer_stage', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('cancer_stage_modifier', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('cancer_subject', ['CancerDiagnosis'])

        # Adding model 'ActivityAndFunctioningAudit'
        db.create_table('cancer_subject_activityandfunctioning_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_activityandfunctioning', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('health_rate', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('health_problems', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('difficulty_work', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('bodily_pain', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('energy', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('health_probs_limit', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('emotional_probs', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('probs_from_work', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('perform_status', self.gf('django.db.models.fields.CharField')(max_length=205)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['ActivityAndFunctioningAudit'])

        # Adding model 'ActivityAndFunctioning'
        db.create_table('cancer_subject_activityandfunctioning', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('health_rate', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('health_problems', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('difficulty_work', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('bodily_pain', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('energy', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('health_probs_limit', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('emotional_probs', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('probs_from_work', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('perform_status', self.gf('django.db.models.fields.CharField')(max_length=205)),
        ))
        db.send_create_signal('cancer_subject', ['ActivityAndFunctioning'])

        # Adding model 'OncologyTreatmentPlanAudit'
        db.create_table('cancer_subject_oncologytreatmentplan_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_oncologytreatmentplan', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('treatment_plan', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('chemotherapy', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('chemo_intent', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('radiation_plan', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('radiation_treatments', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('surgical_plan', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('planned_operation', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['OncologyTreatmentPlanAudit'])

        # Adding model 'OncologyTreatmentPlan'
        db.create_table('cancer_subject_oncologytreatmentplan', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('treatment_plan', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('chemotherapy', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('chemo_intent', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('radiation_plan', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('radiation_treatments', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('surgical_plan', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('planned_operation', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal('cancer_subject', ['OncologyTreatmentPlan'])

        # Adding model 'OTRChemoAudit'
        db.create_table('cancer_subject_otrchemo_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_otrchemo', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('chemo_intent', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('chemo_delays', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('why_delayed', self.gf('django.db.models.fields.CharField')(max_length=65, blank=True)),
            ('why_delayed_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('chemo_reduced', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('why_reduced', self.gf('django.db.models.fields.CharField')(max_length=75, blank=True)),
            ('why_reduced_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['OTRChemoAudit'])

        # Adding model 'OTRChemo'
        db.create_table('cancer_subject_otrchemo', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('chemo_intent', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('chemo_delays', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('why_delayed', self.gf('django.db.models.fields.CharField')(max_length=65, blank=True)),
            ('why_delayed_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('chemo_reduced', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('why_reduced', self.gf('django.db.models.fields.CharField')(max_length=75, blank=True)),
            ('why_reduced_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
        ))
        db.send_create_signal('cancer_subject', ['OTRChemo'])

        # Adding model 'ChemoMedPlanAudit'
        db.create_table('cancer_subject_chemomedplan_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('drug_code', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('dose_category', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('start_date', self.gf('django.db.models.fields.DateField')(max_length=35)),
            ('cycle_num', self.gf('django.db.models.fields.IntegerField')()),
            ('interval', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('specify_other_med', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('oncology_treatment_plan', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_chemomedplan', to=orm['cancer_subject.OncologyTreatmentPlan'])),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['ChemoMedPlanAudit'])

        # Adding model 'ChemoMedPlan'
        db.create_table('cancer_subject_chemomedplan', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('drug_code', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('dose_category', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('start_date', self.gf('django.db.models.fields.DateField')(max_length=35)),
            ('cycle_num', self.gf('django.db.models.fields.IntegerField')()),
            ('interval', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('specify_other_med', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('oncology_treatment_plan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.OncologyTreatmentPlan'])),
        ))
        db.send_create_signal('cancer_subject', ['ChemoMedPlan'])

        # Adding model 'ChemoMedRecordAudit'
        db.create_table('cancer_subject_chemomedrecord_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('drug_code', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('dose_category', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('start_date', self.gf('django.db.models.fields.DateField')(max_length=35)),
            ('cycle_num', self.gf('django.db.models.fields.IntegerField')()),
            ('interval', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('specify_other_med', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('otr_chemo', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_chemomedrecord', to=orm['cancer_subject.OTRChemo'])),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['ChemoMedRecordAudit'])

        # Adding model 'ChemoMedRecord'
        db.create_table('cancer_subject_chemomedrecord', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('drug_code', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('dose_category', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('start_date', self.gf('django.db.models.fields.DateField')(max_length=35)),
            ('cycle_num', self.gf('django.db.models.fields.IntegerField')()),
            ('interval', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('specify_other_med', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('otr_chemo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.OTRChemo'])),
        ))
        db.send_create_signal('cancer_subject', ['ChemoMedRecord'])

        # Adding model 'WhoIllness'
        db.create_table('cancer_subject_whoillness', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=250, db_index=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=250, db_index=True)),
            ('display_index', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
            ('field_name', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('version', self.gf('django.db.models.fields.CharField')(default='1.0', max_length=35)),
        ))
        db.send_create_signal('cancer_subject', ['WhoIllness'])

        # Adding model 'InfoDeterminant'
        db.create_table('cancer_subject_infodeterminant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=250, db_index=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=250, db_index=True)),
            ('display_index', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
            ('field_name', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('version', self.gf('django.db.models.fields.CharField')(default='1.0', max_length=35)),
        ))
        db.send_create_signal('cancer_subject', ['InfoDeterminant'])

        # Adding model 'TreatmentResponseAudit'
        db.create_table('cancer_subject_treatmentresponse_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_treatmentresponse', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('tx_response_class', self.gf('django.db.models.fields.CharField')(max_length=95)),
            ('tx_response_date', self.gf('django.db.models.fields.DateField')(max_length=25)),
            ('tx_response', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['TreatmentResponseAudit'])

        # Adding model 'TreatmentResponse'
        db.create_table('cancer_subject_treatmentresponse', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('tx_response_class', self.gf('django.db.models.fields.CharField')(max_length=95)),
            ('tx_response_date', self.gf('django.db.models.fields.DateField')(max_length=25)),
            ('tx_response', self.gf('django.db.models.fields.CharField')(max_length=35)),
        ))
        db.send_create_signal('cancer_subject', ['TreatmentResponse'])

        # Adding M2M table for field tx_info_determinant on 'TreatmentResponse'
        db.create_table('cancer_subject_treatmentresponse_tx_info_determinant', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('treatmentresponse', models.ForeignKey(orm['cancer_subject.treatmentresponse'], null=False)),
            ('infodeterminant', models.ForeignKey(orm['cancer_subject.infodeterminant'], null=False))
        ))
        db.create_unique('cancer_subject_treatmentresponse_tx_info_determinant', ['treatmentresponse_id', 'infodeterminant_id'])

        # Adding model 'ReferralAudit'
        db.create_table('cancer_subject_referral_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('referrals', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('why_referred', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('referral_date', self.gf('django.db.models.fields.DateTimeField')(max_length=25)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('registered_subject', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_referral', to=orm['bhp_registration.RegisteredSubject'])),
        ))
        db.send_create_signal('cancer_subject', ['ReferralAudit'])

        # Adding model 'Referral'
        db.create_table('cancer_subject_referral', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('registered_subject', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True)),
            ('referrals', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('why_referred', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('referral_date', self.gf('django.db.models.fields.DateTimeField')(max_length=25)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=35)),
        ))
        db.send_create_signal('cancer_subject', ['Referral'])

        # Adding model 'HaartRecordAudit'
        db.create_table('cancer_subject_haartrecord_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_haartrecord', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('hiv', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('haart_status', self.gf('django.db.models.fields.CharField')(max_length=145)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['HaartRecordAudit'])

        # Adding model 'HaartRecord'
        db.create_table('cancer_subject_haartrecord', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('hiv', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('haart_status', self.gf('django.db.models.fields.CharField')(max_length=145)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
        ))
        db.send_create_signal('cancer_subject', ['HaartRecord'])

        # Adding model 'HaartMedRecordAudit'
        db.create_table('cancer_subject_haartmedrecord_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('drug_name', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('mod_reason', self.gf('django.db.models.fields.CharField')(max_length=65)),
            ('arv_reason', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('start_date', self.gf('django.db.models.fields.DateField')(max_length=25)),
            ('stop_date', self.gf('django.db.models.fields.DateField')(max_length=25, null=True, blank=True)),
            ('haart_record', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_haartmedrecord', to=orm['cancer_subject.HaartRecord'])),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['HaartMedRecordAudit'])

        # Adding model 'HaartMedRecord'
        db.create_table('cancer_subject_haartmedrecord', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('drug_name', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('mod_reason', self.gf('django.db.models.fields.CharField')(max_length=65)),
            ('arv_reason', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('start_date', self.gf('django.db.models.fields.DateField')(max_length=25)),
            ('stop_date', self.gf('django.db.models.fields.DateField')(max_length=25, null=True, blank=True)),
            ('haart_record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.HaartRecord'])),
        ))
        db.send_create_signal('cancer_subject', ['HaartMedRecord'])

        # Adding model 'LocatorAudit'
        db.create_table('cancer_subject_locator_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('date_signed', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('mail_address', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('home_visit_permission', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('physical_address', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('may_follow_up', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('subject_cell', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True, blank=True)),
            ('subject_cell_alt', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True, blank=True)),
            ('subject_phone', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True, blank=True)),
            ('subject_phone_alt', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True, blank=True)),
            ('may_call_work', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('subject_work_place', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('subject_work_phone', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True, blank=True)),
            ('may_contact_someone', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True, blank=True)),
            ('contact_rel', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True, blank=True)),
            ('contact_physical_address', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('contact_cell', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True, blank=True)),
            ('contact_phone', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True, blank=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_locator', to=orm['cancer_subject.SubjectVisit'])),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('registered_subject', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_locator', null=True, to=orm['bhp_registration.RegisteredSubject'])),
        ))
        db.send_create_signal('cancer_subject', ['LocatorAudit'])

        # Adding model 'Locator'
        db.create_table('cancer_subject_locator', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('registered_subject', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True, null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('date_signed', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('mail_address', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('home_visit_permission', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('physical_address', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('may_follow_up', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('subject_cell', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True, blank=True)),
            ('subject_cell_alt', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True, blank=True)),
            ('subject_phone', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True, blank=True)),
            ('subject_phone_alt', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True, blank=True)),
            ('may_call_work', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('subject_work_place', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('subject_work_phone', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True, blank=True)),
            ('may_contact_someone', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True, blank=True)),
            ('contact_rel', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True, blank=True)),
            ('contact_physical_address', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('contact_cell', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True, blank=True)),
            ('contact_phone', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True, blank=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'])),
        ))
        db.send_create_signal('cancer_subject', ['Locator'])

        # Adding model 'LabResultAudit'
        db.create_table('cancer_subject_labresult_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_labresult', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('has_hiv_result', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('has_cd4', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('has_vl', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('has_haem', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('has_chem', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('has_other_abnormal', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('other_abnormal', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('abnormal_lab_results', self.gf('django.db.models.fields.CharField')(max_length=65)),
            ('tb_tests', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('tb_prompt_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['LabResultAudit'])

        # Adding model 'LabResult'
        db.create_table('cancer_subject_labresult', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('has_hiv_result', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('has_cd4', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('has_vl', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('has_haem', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('has_chem', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('has_other_abnormal', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('other_abnormal', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('abnormal_lab_results', self.gf('django.db.models.fields.CharField')(max_length=65)),
            ('tb_tests', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('tb_prompt_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
        ))
        db.send_create_signal('cancer_subject', ['LabResult'])

        # Adding model 'LabResultHivAudit'
        db.create_table('cancer_subject_labresulthiv_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_labresulthiv', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('test_date', self.gf('django.db.models.fields.DateField')(max_length=25, null=True, blank=True)),
            ('test_result', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['LabResultHivAudit'])

        # Adding model 'LabResultHiv'
        db.create_table('cancer_subject_labresulthiv', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('test_date', self.gf('django.db.models.fields.DateField')(max_length=25, null=True, blank=True)),
            ('test_result', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('cancer_subject', ['LabResultHiv'])

        # Adding model 'LabResultCd4Audit'
        db.create_table('cancer_subject_labresultcd4_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_labresultcd4', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('cd4_drawn_date', self.gf('django.db.models.fields.DateField')(max_length=25)),
            ('cd4_result', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['LabResultCd4Audit'])

        # Adding model 'LabResultCd4'
        db.create_table('cancer_subject_labresultcd4', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('cd4_drawn_date', self.gf('django.db.models.fields.DateField')(max_length=25)),
            ('cd4_result', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal('cancer_subject', ['LabResultCd4'])

        # Adding model 'LabResultViralloadAudit'
        db.create_table('cancer_subject_labresultviralload_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_labresultviralload', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('vl_drawn_date', self.gf('django.db.models.fields.DateField')(max_length=25)),
            ('vl_result', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['LabResultViralloadAudit'])

        # Adding model 'LabResultViralload'
        db.create_table('cancer_subject_labresultviralload', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('vl_drawn_date', self.gf('django.db.models.fields.DateField')(max_length=25)),
            ('vl_result', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal('cancer_subject', ['LabResultViralload'])

        # Adding model 'LabResultHaematologyAudit'
        db.create_table('cancer_subject_labresulthaematology_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_labresulthaematology', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('haem_drawn_date', self.gf('django.db.models.fields.DateField')(max_length=25)),
            ('hgb', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=1)),
            ('mcv', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=1)),
            ('wbc_count', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('anc_count', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
            ('platelet', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['LabResultHaematologyAudit'])

        # Adding model 'LabResultHaematology'
        db.create_table('cancer_subject_labresulthaematology', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('haem_drawn_date', self.gf('django.db.models.fields.DateField')(max_length=25)),
            ('hgb', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=1)),
            ('mcv', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=1)),
            ('wbc_count', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('anc_count', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
            ('platelet', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=1)),
        ))
        db.send_create_signal('cancer_subject', ['LabResultHaematology'])

        # Adding model 'LabResultChemistryAudit'
        db.create_table('cancer_subject_labresultchemistry_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_labresultchemistry', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('chem_drawn_date', self.gf('django.db.models.fields.DateField')(max_length=25)),
            ('alanine', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=1)),
            ('aspartate', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=1)),
            ('bilirubin', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1, blank=True)),
            ('creatinine', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=1, blank=True)),
            ('lactate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=1, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['LabResultChemistryAudit'])

        # Adding model 'LabResultChemistry'
        db.create_table('cancer_subject_labresultchemistry', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('chem_drawn_date', self.gf('django.db.models.fields.DateField')(max_length=25)),
            ('alanine', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=1)),
            ('aspartate', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=1)),
            ('bilirubin', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=1, blank=True)),
            ('creatinine', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=1, blank=True)),
            ('lactate', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=1, blank=True)),
        ))
        db.send_create_signal('cancer_subject', ['LabResultChemistry'])

        # Adding model 'LabResultTbAudit'
        db.create_table('cancer_subject_labresulttb_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_labresulttb', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('tb_description', self.gf('django.db.models.fields.CharField')(max_length=65)),
            ('tb_treatment', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tb_treatment_start', self.gf('django.db.models.fields.DateField')(max_length=25, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['LabResultTbAudit'])

        # Adding model 'LabResultTb'
        db.create_table('cancer_subject_labresulttb', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('tb_description', self.gf('django.db.models.fields.CharField')(max_length=65)),
            ('tb_treatment', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tb_treatment_start', self.gf('django.db.models.fields.DateField')(max_length=25, null=True, blank=True)),
        ))
        db.send_create_signal('cancer_subject', ['LabResultTb'])

        # Adding model 'LabResultHeightWeightAudit'
        db.create_table('cancer_subject_labresultheightweight_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_labresultheightweight', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('weight', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=1)),
            ('height', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1, blank=True)),
            ('cough2weeks', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['LabResultHeightWeightAudit'])

        # Adding model 'LabResultHeightWeight'
        db.create_table('cancer_subject_labresultheightweight', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('weight', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=1)),
            ('height', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1, blank=True)),
            ('cough2weeks', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('cancer_subject', ['LabResultHeightWeight'])

        # Adding model 'OncologyTreatmentRecordAudit'
        db.create_table('cancer_subject_oncologytreatmentrecord_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_oncologytreatmentrecord', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('treatment_received', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('chemo_received', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('radiation_received', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('surgical_therapy', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['OncologyTreatmentRecordAudit'])

        # Adding model 'OncologyTreatmentRecord'
        db.create_table('cancer_subject_oncologytreatmentrecord', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('treatment_received', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('chemo_received', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('radiation_received', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('surgical_therapy', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
        ))
        db.send_create_signal('cancer_subject', ['OncologyTreatmentRecord'])

        # Adding model 'OTRRadiationAudit'
        db.create_table('cancer_subject_otrradiation_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_otrradiation', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('concomitant', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('amount_radiation', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['OTRRadiationAudit'])

        # Adding model 'OTRRadiation'
        db.create_table('cancer_subject_otrradiation', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('concomitant', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('amount_radiation', self.gf('django.db.models.fields.CharField')(max_length=15)),
        ))
        db.send_create_signal('cancer_subject', ['OTRRadiation'])

        # Adding model 'OTRSurgicalAudit'
        db.create_table('cancer_subject_otrsurgical_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_otrsurgical', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('operation_performed', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_operation', self.gf('django.db.models.fields.DateField')(max_length=15, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['OTRSurgicalAudit'])

        # Adding model 'OTRSurgical'
        db.create_table('cancer_subject_otrsurgical', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('operation_performed', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date_operation', self.gf('django.db.models.fields.DateField')(max_length=15, null=True, blank=True)),
        ))
        db.send_create_signal('cancer_subject', ['OTRSurgical'])

        # Adding model 'BaselineHIVHistoryAudit'
        db.create_table('cancer_subject_baselinehivhistory_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_baselinehivhistory', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('has_hiv_result', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('had_who_illnesses', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('has_cd4', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['BaselineHIVHistoryAudit'])

        # Adding model 'BaselineHIVHistory'
        db.create_table('cancer_subject_baselinehivhistory', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('has_hiv_result', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('had_who_illnesses', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('has_cd4', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('cancer_subject', ['BaselineHIVHistory'])

        # Adding model 'BHHHivTestAudit'
        db.create_table('cancer_subject_bhhhivtest_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_bhhhivtest', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('hiv_drawn_date', self.gf('django.db.models.fields.DateField')(max_length=25)),
            ('hiv_result', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['BHHHivTestAudit'])

        # Adding model 'BHHHivTest'
        db.create_table('cancer_subject_bhhhivtest', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('hiv_drawn_date', self.gf('django.db.models.fields.DateField')(max_length=25)),
            ('hiv_result', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('cancer_subject', ['BHHHivTest'])

        # Adding model 'BHHWhoIllnessAudit'
        db.create_table('cancer_subject_bhhwhoillness_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_bhhwhoillness', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('who_illness_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('who_illness_date', self.gf('django.db.models.fields.DateField')(max_length=25, null=True)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['BHHWhoIllnessAudit'])

        # Adding model 'BHHWhoIllness'
        db.create_table('cancer_subject_bhhwhoillness', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('who_illness_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('who_illness_date', self.gf('django.db.models.fields.DateField')(max_length=25, null=True)),
        ))
        db.send_create_signal('cancer_subject', ['BHHWhoIllness'])

        # Adding M2M table for field who_illness on 'BHHWhoIllness'
        db.create_table('cancer_subject_bhhwhoillness_who_illness', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bhhwhoillness', models.ForeignKey(orm['cancer_subject.bhhwhoillness'], null=False)),
            ('whoillness', models.ForeignKey(orm['cancer_subject.whoillness'], null=False))
        ))
        db.create_unique('cancer_subject_bhhwhoillness_who_illness', ['bhhwhoillness_id', 'whoillness_id'])

        # Adding model 'BHHCd4Audit'
        db.create_table('cancer_subject_bhhcd4_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_bhhcd4', null=True, to=orm['cancer_subject.SubjectVisit'])),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('nadir_cd4', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2)),
            ('nadir_cd4_drawn_date', self.gf('django.db.models.fields.DateField')(max_length=25, null=True)),
            ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('cancer_subject', ['BHHCd4Audit'])

        # Adding model 'BHHCd4'
        db.create_table('cancer_subject_bhhcd4', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('subject_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cancer_subject.SubjectVisit'], null=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 10, 9, 0, 0))),
            ('nadir_cd4', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=6, decimal_places=2)),
            ('nadir_cd4_drawn_date', self.gf('django.db.models.fields.DateField')(max_length=25, null=True)),
        ))
        db.send_create_signal('cancer_subject', ['BHHCd4'])


    def backwards(self, orm):
        # Deleting model 'SubjectConsentAudit'
        db.delete_table('cancer_subject_subjectconsent_audit')

        # Deleting model 'SubjectConsent'
        db.delete_table('cancer_subject_subjectconsent')

        # Deleting model 'SubjectDeathAudit'
        db.delete_table('cancer_subject_subjectdeath_audit')

        # Deleting model 'SubjectDeath'
        db.delete_table('cancer_subject_subjectdeath')

        # Deleting model 'SubjectOffStudyAudit'
        db.delete_table('cancer_subject_subjectoffstudy_audit')

        # Deleting model 'SubjectOffStudy'
        db.delete_table('cancer_subject_subjectoffstudy')

        # Deleting model 'SubjectVisitAudit'
        db.delete_table('cancer_subject_subjectvisit_audit')

        # Deleting model 'SubjectVisit'
        db.delete_table('cancer_subject_subjectvisit')

        # Deleting model 'EnrollmentChecklistAudit'
        db.delete_table('cancer_subject_enrollmentchecklist_audit')

        # Deleting model 'EnrollmentChecklist'
        db.delete_table('cancer_subject_enrollmentchecklist')

        # Deleting model 'BaseRiskAssessmentAudit'
        db.delete_table('cancer_subject_baseriskassessment_audit')

        # Deleting model 'BaseRiskAssessment'
        db.delete_table('cancer_subject_baseriskassessment')

        # Deleting model 'BaseRiskAssessmentSmokingAudit'
        db.delete_table('cancer_subject_baseriskassessmentsmoking_audit')

        # Deleting model 'BaseRiskAssessmentSmoking'
        db.delete_table('cancer_subject_baseriskassessmentsmoking')

        # Deleting model 'BaseRiskAssessmentSunAudit'
        db.delete_table('cancer_subject_baseriskassessmentsun_audit')

        # Deleting model 'BaseRiskAssessmentSun'
        db.delete_table('cancer_subject_baseriskassessmentsun')

        # Deleting model 'BaseRiskAssessmentMiningAudit'
        db.delete_table('cancer_subject_baseriskassessmentmining_audit')

        # Deleting model 'BaseRiskAssessmentMining'
        db.delete_table('cancer_subject_baseriskassessmentmining')

        # Deleting model 'BaseRiskAssessmentAlcoholAudit'
        db.delete_table('cancer_subject_baseriskassessmentalcohol_audit')

        # Deleting model 'BaseRiskAssessmentAlcohol'
        db.delete_table('cancer_subject_baseriskassessmentalcohol')

        # Deleting model 'BaseRiskAssessmentFemaleAudit'
        db.delete_table('cancer_subject_baseriskassessmentfemale_audit')

        # Deleting model 'BaseRiskAssessmentFemale'
        db.delete_table('cancer_subject_baseriskassessmentfemale')

        # Deleting model 'BaseRiskAssessmentChemicalAudit'
        db.delete_table('cancer_subject_baseriskassessmentchemical_audit')

        # Deleting model 'BaseRiskAssessmentChemical'
        db.delete_table('cancer_subject_baseriskassessmentchemical')

        # Deleting model 'BaseRiskAssessmentFuelAudit'
        db.delete_table('cancer_subject_baseriskassessmentfuel_audit')

        # Deleting model 'BaseRiskAssessmentFuel'
        db.delete_table('cancer_subject_baseriskassessmentfuel')

        # Deleting model 'BaseRiskAssessmentCancerAudit'
        db.delete_table('cancer_subject_baseriskassessmentcancer_audit')

        # Deleting model 'BaseRiskAssessmentCancer'
        db.delete_table('cancer_subject_baseriskassessmentcancer')

        # Deleting model 'BaseRiskAssessmentDemoAudit'
        db.delete_table('cancer_subject_baseriskassessmentdemo_audit')

        # Deleting model 'BaseRiskAssessmentDemo'
        db.delete_table('cancer_subject_baseriskassessmentdemo')

        # Deleting model 'BaseRiskAssessmentEatingAudit'
        db.delete_table('cancer_subject_baseriskassessmenteating_audit')

        # Deleting model 'BaseRiskAssessmentEating'
        db.delete_table('cancer_subject_baseriskassessmenteating')

        # Deleting model 'CancerDiagnosisAudit'
        db.delete_table('cancer_subject_cancerdiagnosis_audit')

        # Deleting model 'CancerDiagnosis'
        db.delete_table('cancer_subject_cancerdiagnosis')

        # Deleting model 'ActivityAndFunctioningAudit'
        db.delete_table('cancer_subject_activityandfunctioning_audit')

        # Deleting model 'ActivityAndFunctioning'
        db.delete_table('cancer_subject_activityandfunctioning')

        # Deleting model 'OncologyTreatmentPlanAudit'
        db.delete_table('cancer_subject_oncologytreatmentplan_audit')

        # Deleting model 'OncologyTreatmentPlan'
        db.delete_table('cancer_subject_oncologytreatmentplan')

        # Deleting model 'OTRChemoAudit'
        db.delete_table('cancer_subject_otrchemo_audit')

        # Deleting model 'OTRChemo'
        db.delete_table('cancer_subject_otrchemo')

        # Deleting model 'ChemoMedPlanAudit'
        db.delete_table('cancer_subject_chemomedplan_audit')

        # Deleting model 'ChemoMedPlan'
        db.delete_table('cancer_subject_chemomedplan')

        # Deleting model 'ChemoMedRecordAudit'
        db.delete_table('cancer_subject_chemomedrecord_audit')

        # Deleting model 'ChemoMedRecord'
        db.delete_table('cancer_subject_chemomedrecord')

        # Deleting model 'WhoIllness'
        db.delete_table('cancer_subject_whoillness')

        # Deleting model 'InfoDeterminant'
        db.delete_table('cancer_subject_infodeterminant')

        # Deleting model 'TreatmentResponseAudit'
        db.delete_table('cancer_subject_treatmentresponse_audit')

        # Deleting model 'TreatmentResponse'
        db.delete_table('cancer_subject_treatmentresponse')

        # Removing M2M table for field tx_info_determinant on 'TreatmentResponse'
        db.delete_table('cancer_subject_treatmentresponse_tx_info_determinant')

        # Deleting model 'ReferralAudit'
        db.delete_table('cancer_subject_referral_audit')

        # Deleting model 'Referral'
        db.delete_table('cancer_subject_referral')

        # Deleting model 'HaartRecordAudit'
        db.delete_table('cancer_subject_haartrecord_audit')

        # Deleting model 'HaartRecord'
        db.delete_table('cancer_subject_haartrecord')

        # Deleting model 'HaartMedRecordAudit'
        db.delete_table('cancer_subject_haartmedrecord_audit')

        # Deleting model 'HaartMedRecord'
        db.delete_table('cancer_subject_haartmedrecord')

        # Deleting model 'LocatorAudit'
        db.delete_table('cancer_subject_locator_audit')

        # Deleting model 'Locator'
        db.delete_table('cancer_subject_locator')

        # Deleting model 'LabResultAudit'
        db.delete_table('cancer_subject_labresult_audit')

        # Deleting model 'LabResult'
        db.delete_table('cancer_subject_labresult')

        # Deleting model 'LabResultHivAudit'
        db.delete_table('cancer_subject_labresulthiv_audit')

        # Deleting model 'LabResultHiv'
        db.delete_table('cancer_subject_labresulthiv')

        # Deleting model 'LabResultCd4Audit'
        db.delete_table('cancer_subject_labresultcd4_audit')

        # Deleting model 'LabResultCd4'
        db.delete_table('cancer_subject_labresultcd4')

        # Deleting model 'LabResultViralloadAudit'
        db.delete_table('cancer_subject_labresultviralload_audit')

        # Deleting model 'LabResultViralload'
        db.delete_table('cancer_subject_labresultviralload')

        # Deleting model 'LabResultHaematologyAudit'
        db.delete_table('cancer_subject_labresulthaematology_audit')

        # Deleting model 'LabResultHaematology'
        db.delete_table('cancer_subject_labresulthaematology')

        # Deleting model 'LabResultChemistryAudit'
        db.delete_table('cancer_subject_labresultchemistry_audit')

        # Deleting model 'LabResultChemistry'
        db.delete_table('cancer_subject_labresultchemistry')

        # Deleting model 'LabResultTbAudit'
        db.delete_table('cancer_subject_labresulttb_audit')

        # Deleting model 'LabResultTb'
        db.delete_table('cancer_subject_labresulttb')

        # Deleting model 'LabResultHeightWeightAudit'
        db.delete_table('cancer_subject_labresultheightweight_audit')

        # Deleting model 'LabResultHeightWeight'
        db.delete_table('cancer_subject_labresultheightweight')

        # Deleting model 'OncologyTreatmentRecordAudit'
        db.delete_table('cancer_subject_oncologytreatmentrecord_audit')

        # Deleting model 'OncologyTreatmentRecord'
        db.delete_table('cancer_subject_oncologytreatmentrecord')

        # Deleting model 'OTRRadiationAudit'
        db.delete_table('cancer_subject_otrradiation_audit')

        # Deleting model 'OTRRadiation'
        db.delete_table('cancer_subject_otrradiation')

        # Deleting model 'OTRSurgicalAudit'
        db.delete_table('cancer_subject_otrsurgical_audit')

        # Deleting model 'OTRSurgical'
        db.delete_table('cancer_subject_otrsurgical')

        # Deleting model 'BaselineHIVHistoryAudit'
        db.delete_table('cancer_subject_baselinehivhistory_audit')

        # Deleting model 'BaselineHIVHistory'
        db.delete_table('cancer_subject_baselinehivhistory')

        # Deleting model 'BHHHivTestAudit'
        db.delete_table('cancer_subject_bhhhivtest_audit')

        # Deleting model 'BHHHivTest'
        db.delete_table('cancer_subject_bhhhivtest')

        # Deleting model 'BHHWhoIllnessAudit'
        db.delete_table('cancer_subject_bhhwhoillness_audit')

        # Deleting model 'BHHWhoIllness'
        db.delete_table('cancer_subject_bhhwhoillness')

        # Removing M2M table for field who_illness on 'BHHWhoIllness'
        db.delete_table('cancer_subject_bhhwhoillness_who_illness')

        # Deleting model 'BHHCd4Audit'
        db.delete_table('cancer_subject_bhhcd4_audit')

        # Deleting model 'BHHCd4'
        db.delete_table('cancer_subject_bhhcd4')


    models = {
        'bhp_adverse.deathcausecategory': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathCauseCategory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'bhp_adverse.deathcauseinfo': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathCauseInfo'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'bhp_adverse.deathmedicalresponsibility': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathMedicalResponsibility'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'bhp_adverse.deathreasonhospitalized': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathReasonHospitalized'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'bhp_appointment.appointment': {
            'Meta': {'ordering': "['registered_subject', 'appt_datetime']", 'object_name': 'Appointment'},
            'appt_datetime': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'appt_reason': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'appt_status': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '25', 'db_index': 'True'}),
            'best_appt_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'contact_tel': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dashboard_type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'study_site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_variables.StudySite']", 'null': 'True'}),
            'timepoint_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'visit_definition': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['bhp_visit.VisitDefinition']"}),
            'visit_instance': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1', 'null': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        'bhp_code_lists.dxcode': {
            'Meta': {'object_name': 'DxCode'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_ref': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'long_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'bhp_content_type_map.contenttypemap': {
            'Meta': {'ordering': "['name']", 'unique_together': "(['app_label', 'model'],)", 'object_name': 'ContentTypeMap', 'db_table': "'bhp_common_contenttypemap'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'bhp_registration.registeredsubject': {
            'Meta': {'ordering': "['subject_identifier']", 'object_name': 'RegisteredSubject'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'hiv_status': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'identity': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'identity_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'is_dob_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'may_store_samples': ('django.db.models.fields.CharField', [], {'default': "'?'", 'max_length': '3'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'randomization_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'registration_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'registration_identifier': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'registration_status': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'relative_identifier': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'salt': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'screening_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sid': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'study_site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_variables.StudySite']", 'null': 'True', 'blank': 'True'}),
            'subject_consent_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'subject_type': ('django.db.models.fields.CharField', [], {'default': "'undetermined'", 'max_length': '25', 'null': 'True'}),
            'survival_status': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'bhp_variables.studysite': {
            'Meta': {'ordering': "['site_code']", 'unique_together': "[('site_code', 'site_name')]", 'object_name': 'StudySite'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'site_code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'site_name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'bhp_visit.membershipform': {
            'Meta': {'object_name': 'MembershipForm'},
            'category': ('django.db.models.fields.CharField', [], {'default': "'subject'", 'max_length': '25', 'null': 'True'}),
            'content_type_map': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['bhp_content_type_map.ContentTypeMap']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'bhp_visit.schedulegroup': {
            'Meta': {'ordering': "['group_name']", 'object_name': 'ScheduleGroup'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'group_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'grouping_key': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'membership_form': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_visit.MembershipForm']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'bhp_visit.visitdefinition': {
            'Meta': {'ordering': "['code', 'time_point']", 'object_name': 'VisitDefinition'},
            'base_interval': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'base_interval_unit': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '10'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '4', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'grouping': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'instruction': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'lower_window': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lower_window_unit': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '10'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'schedule_group': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bhp_visit.ScheduleGroup']", 'symmetrical': 'False'}),
            'time_point': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '35', 'db_index': 'True'}),
            'upper_window': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'upper_window_unit': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '10'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.activityandfunctioning': {
            'Meta': {'object_name': 'ActivityAndFunctioning'},
            'bodily_pain': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'difficulty_work': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'emotional_probs': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'energy': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'health_problems': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'health_probs_limit': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'health_rate': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'perform_status': ('django.db.models.fields.CharField', [], {'max_length': '205'}),
            'probs_from_work': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.activityandfunctioningaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'ActivityAndFunctioningAudit', 'db_table': "'cancer_subject_activityandfunctioning_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'bodily_pain': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'difficulty_work': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'emotional_probs': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'energy': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'health_problems': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'health_probs_limit': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'health_rate': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'perform_status': ('django.db.models.fields.CharField', [], {'max_length': '205'}),
            'probs_from_work': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_activityandfunctioning'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.baselinehivhistory': {
            'Meta': {'object_name': 'BaselineHIVHistory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'had_who_illnesses': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_cd4': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_hiv_result': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.baselinehivhistoryaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'BaselineHIVHistoryAudit', 'db_table': "'cancer_subject_baselinehivhistory_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'had_who_illnesses': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_cd4': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_hiv_result': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baselinehivhistory'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.baseriskassessment': {
            'Meta': {'object_name': 'BaseRiskAssessment'},
            'age_firstsex': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_alcohol': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_smoked': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_worked_mine': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hepatitis': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'is_albino': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'participant_interviewed': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'tradmedicine': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'tuberculosis': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'year_tb': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'cancer_subject.baseriskassessmentalcohol': {
            'Meta': {'object_name': 'BaseRiskAssessmentAlcohol'},
            'alcohol_weekly': ('django.db.models.fields.IntegerField', [], {}),
            'amount_drinking': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.baseriskassessmentalcoholaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'BaseRiskAssessmentAlcoholAudit', 'db_table': "'cancer_subject_baseriskassessmentalcohol_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'alcohol_weekly': ('django.db.models.fields.IntegerField', [], {}),
            'amount_drinking': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baseriskassessmentalcohol'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.baseriskassessmentaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'BaseRiskAssessmentAudit', 'db_table': "'cancer_subject_baseriskassessment_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'age_firstsex': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_alcohol': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_smoked': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_worked_mine': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hepatitis': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'is_albino': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'participant_interviewed': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baseriskassessment'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'tradmedicine': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'tuberculosis': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'year_tb': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'cancer_subject.baseriskassessmentcancer': {
            'Meta': {'object_name': 'BaseRiskAssessmentCancer'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'family_cancer': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'family_cancer_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'family_cancer_type': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'had_previous_cancer': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'previous_cancer': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'previous_cancer_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.baseriskassessmentcanceraudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'BaseRiskAssessmentCancerAudit', 'db_table': "'cancer_subject_baseriskassessmentcancer_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'family_cancer': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'family_cancer_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'family_cancer_type': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'had_previous_cancer': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'previous_cancer': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'previous_cancer_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baseriskassessmentcancer'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.baseriskassessmentchemical': {
            'Meta': {'object_name': 'BaseRiskAssessmentChemical'},
            'arsenic_smelting': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'asbestos': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'asbestos_no_protection': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'chemicals': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'chemicals_time': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'total_time_no_protection': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.baseriskassessmentchemicalaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'BaseRiskAssessmentChemicalAudit', 'db_table': "'cancer_subject_baseriskassessmentchemical_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'arsenic_smelting': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'asbestos': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'asbestos_no_protection': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'chemicals': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'chemicals_time': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baseriskassessmentchemical'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'total_time_no_protection': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.baseriskassessmentdemo': {
            'Meta': {'object_name': 'BaseRiskAssessmentDemo'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '65'}),
            'district20': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'electricity': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'ethnic_grp': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'ethnic_grp_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'household_people': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'marital_status': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'marital_status_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'money_earned': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'money_provide': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'money_provide_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'occupation_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'race': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'race_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'setting': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'setting20': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'toilet': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'toilet_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.baseriskassessmentdemoaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'BaseRiskAssessmentDemoAudit', 'db_table': "'cancer_subject_baseriskassessmentdemo_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '65'}),
            'district20': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'electricity': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'ethnic_grp': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'ethnic_grp_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'household_people': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'marital_status': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'marital_status_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'money_earned': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'money_provide': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'money_provide_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'occupation_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'race': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'race_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'setting': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'setting20': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baseriskassessmentdemo'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'toilet': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'toilet_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.baseriskassessmenteating': {
            'Meta': {'object_name': 'BaseRiskAssessmentEating'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'five_fruit': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'meal_millet': ('django.db.models.fields.IntegerField', [], {}),
            'meal_peanuts': ('django.db.models.fields.IntegerField', [], {}),
            'meal_rice': ('django.db.models.fields.IntegerField', [], {}),
            'meal_sorghum': ('django.db.models.fields.IntegerField', [], {}),
            'meals_weekly': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.baseriskassessmenteatingaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'BaseRiskAssessmentEatingAudit', 'db_table': "'cancer_subject_baseriskassessmenteating_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'five_fruit': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'meal_millet': ('django.db.models.fields.IntegerField', [], {}),
            'meal_peanuts': ('django.db.models.fields.IntegerField', [], {}),
            'meal_rice': ('django.db.models.fields.IntegerField', [], {}),
            'meal_sorghum': ('django.db.models.fields.IntegerField', [], {}),
            'meals_weekly': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baseriskassessmenteating'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.baseriskassessmentfemale': {
            'Meta': {'object_name': 'BaseRiskAssessmentFemale'},
            'age_period': ('django.db.models.fields.IntegerField', [], {}),
            'children': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'years_breastfed': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'cancer_subject.baseriskassessmentfemaleaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'BaseRiskAssessmentFemaleAudit', 'db_table': "'cancer_subject_baseriskassessmentfemale_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'age_period': ('django.db.models.fields.IntegerField', [], {}),
            'children': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baseriskassessmentfemale'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'years_breastfed': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'cancer_subject.baseriskassessmentfuel': {
            'Meta': {'object_name': 'BaseRiskAssessmentFuel'},
            'cooking': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'cooking_mm': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'fuel_20y': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'fuel_20y_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'fuel_mm': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'fuel_mm_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.baseriskassessmentfuelaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'BaseRiskAssessmentFuelAudit', 'db_table': "'cancer_subject_baseriskassessmentfuel_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'cooking': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'cooking_mm': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'fuel_20y': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'fuel_20y_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'fuel_mm': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'fuel_mm_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baseriskassessmentfuel'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.baseriskassessmentmining': {
            'Meta': {'object_name': 'BaseRiskAssessmentMining'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'last_mine': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'mine_prompt_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'mine_time': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'mine_type': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'mine_underground': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'mine_underground_time': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.baseriskassessmentminingaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'BaseRiskAssessmentMiningAudit', 'db_table': "'cancer_subject_baseriskassessmentmining_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'last_mine': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'mine_prompt_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'mine_time': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'mine_type': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'mine_underground': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'mine_underground_time': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baseriskassessmentmining'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.baseriskassessmentsmoking': {
            'Meta': {'object_name': 'BaseRiskAssessmentSmoking'},
            'cigarette_smoked': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'cigarette_smoking': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'smoke_now': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'when_quit': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'years_smoked': ('django.db.models.fields.IntegerField', [], {}),
            'years_smoked_before': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'cancer_subject.baseriskassessmentsmokingaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'BaseRiskAssessmentSmokingAudit', 'db_table': "'cancer_subject_baseriskassessmentsmoking_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'cigarette_smoked': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'cigarette_smoking': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'smoke_now': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baseriskassessmentsmoking'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'when_quit': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'years_smoked': ('django.db.models.fields.IntegerField', [], {}),
            'years_smoked_before': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'cancer_subject.baseriskassessmentsun': {
            'Meta': {'object_name': 'BaseRiskAssessmentSun'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hat': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hours_outdoor': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'shade_umbrella': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'sleeved_shirt': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'sunglasses': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.baseriskassessmentsunaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'BaseRiskAssessmentSunAudit', 'db_table': "'cancer_subject_baseriskassessmentsun_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hat': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hours_outdoor': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'shade_umbrella': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'sleeved_shirt': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baseriskassessmentsun'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'sunglasses': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.bhhcd4': {
            'Meta': {'object_name': 'BHHCd4'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nadir_cd4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2'}),
            'nadir_cd4_drawn_date': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.bhhcd4audit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'BHHCd4Audit', 'db_table': "'cancer_subject_bhhcd4_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nadir_cd4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2'}),
            'nadir_cd4_drawn_date': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_bhhcd4'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.bhhhivtest': {
            'Meta': {'object_name': 'BHHHivTest'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hiv_drawn_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'hiv_result': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.bhhhivtestaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'BHHHivTestAudit', 'db_table': "'cancer_subject_bhhhivtest_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hiv_drawn_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'hiv_result': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_bhhhivtest'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.bhhwhoillness': {
            'Meta': {'object_name': 'BHHWhoIllness'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'who_illness': ('django.db.models.fields.related.ManyToManyField', [], {'max_length': '35', 'to': "orm['cancer_subject.WhoIllness']", 'null': 'True', 'symmetrical': 'False'}),
            'who_illness_date': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True'}),
            'who_illness_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'})
        },
        'cancer_subject.bhhwhoillnessaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'BHHWhoIllnessAudit', 'db_table': "'cancer_subject_bhhwhoillness_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_bhhwhoillness'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'who_illness_date': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True'}),
            'who_illness_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'})
        },
        'cancer_subject.cancerdiagnosis': {
            'Meta': {'object_name': 'CancerDiagnosis'},
            'cancer_category': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'cancer_site': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'cancer_stage': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'cancer_stage_modifier': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'clinical_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_diagnosed': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'diagnosis_basis': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'diagnosis_basis_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'diagnosis_word': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'first_evaluation': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'lymph_basis': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'lymph_nodes': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'metastasis': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'metastasis_basis': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'symptom_first_noticed': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'symptom_prompt': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'symptom_prompt_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'trad_evaluation': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'tumour': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'tumour_basis': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.cancerdiagnosisaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'CancerDiagnosisAudit', 'db_table': "'cancer_subject_cancerdiagnosis_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'cancer_category': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'cancer_site': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'cancer_stage': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'cancer_stage_modifier': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'clinical_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_diagnosed': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'diagnosis_basis': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'diagnosis_basis_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'diagnosis_word': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'first_evaluation': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'lymph_basis': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'lymph_nodes': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'metastasis': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'metastasis_basis': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_cancerdiagnosis'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'symptom_first_noticed': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'symptom_prompt': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'symptom_prompt_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'trad_evaluation': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'tumour': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'tumour_basis': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.chemomedplan': {
            'Meta': {'object_name': 'ChemoMedPlan'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'cycle_num': ('django.db.models.fields.IntegerField', [], {}),
            'dose_category': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'drug_code': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'interval': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'oncology_treatment_plan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.OncologyTreatmentPlan']"}),
            'specify_other_med': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.chemomedplanaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'ChemoMedPlanAudit', 'db_table': "'cancer_subject_chemomedplan_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'cycle_num': ('django.db.models.fields.IntegerField', [], {}),
            'dose_category': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'drug_code': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'interval': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'oncology_treatment_plan': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_chemomedplan'", 'to': "orm['cancer_subject.OncologyTreatmentPlan']"}),
            'specify_other_med': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.chemomedrecord': {
            'Meta': {'object_name': 'ChemoMedRecord'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'cycle_num': ('django.db.models.fields.IntegerField', [], {}),
            'dose_category': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'drug_code': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'interval': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'otr_chemo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.OTRChemo']"}),
            'specify_other_med': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.chemomedrecordaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'ChemoMedRecordAudit', 'db_table': "'cancer_subject_chemomedrecord_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'cycle_num': ('django.db.models.fields.IntegerField', [], {}),
            'dose_category': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'drug_code': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'interval': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'otr_chemo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_chemomedrecord'", 'to': "orm['cancer_subject.OTRChemo']"}),
            'specify_other_med': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.enrollmentchecklist': {
            'Meta': {'object_name': 'EnrollmentChecklist'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'registration_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.enrollmentchecklistaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'EnrollmentChecklistAudit', 'db_table': "'cancer_subject_enrollmentchecklist_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_enrollmentchecklist'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'registration_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.haartmedrecord': {
            'Meta': {'object_name': 'HaartMedRecord'},
            'arv_reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'drug_name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'haart_record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.HaartRecord']"}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'mod_reason': ('django.db.models.fields.CharField', [], {'max_length': '65'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'stop_date': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.haartmedrecordaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'HaartMedRecordAudit', 'db_table': "'cancer_subject_haartmedrecord_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'arv_reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'drug_name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'haart_record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_haartmedrecord'", 'to': "orm['cancer_subject.HaartRecord']"}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'mod_reason': ('django.db.models.fields.CharField', [], {'max_length': '65'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'stop_date': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.haartrecord': {
            'Meta': {'object_name': 'HaartRecord'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'haart_status': ('django.db.models.fields.CharField', [], {'max_length': '145'}),
            'hiv': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.haartrecordaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'HaartRecordAudit', 'db_table': "'cancer_subject_haartrecord_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'haart_status': ('django.db.models.fields.CharField', [], {'max_length': '145'}),
            'hiv': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_haartrecord'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.infodeterminant': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'InfoDeterminant'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'cancer_subject.labresult': {
            'Meta': {'object_name': 'LabResult'},
            'abnormal_lab_results': ('django.db.models.fields.CharField', [], {'max_length': '65'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_cd4': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_chem': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_haem': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_hiv_result': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_other_abnormal': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_vl': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'other_abnormal': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'tb_prompt_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'tb_tests': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.labresultaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'LabResultAudit', 'db_table': "'cancer_subject_labresult_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'abnormal_lab_results': ('django.db.models.fields.CharField', [], {'max_length': '65'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_cd4': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_chem': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_haem': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_hiv_result': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_other_abnormal': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_vl': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'other_abnormal': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_labresult'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'tb_prompt_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'tb_tests': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.labresultcd4': {
            'Meta': {'object_name': 'LabResultCd4'},
            'cd4_drawn_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'cd4_result': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.labresultcd4audit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'LabResultCd4Audit', 'db_table': "'cancer_subject_labresultcd4_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'cd4_drawn_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'cd4_result': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_labresultcd4'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.labresultchemistry': {
            'Meta': {'object_name': 'LabResultChemistry'},
            'alanine': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '1'}),
            'aspartate': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '1'}),
            'bilirubin': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'chem_drawn_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'creatinine': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '1', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'lactate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '1', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.labresultchemistryaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'LabResultChemistryAudit', 'db_table': "'cancer_subject_labresultchemistry_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'alanine': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '1'}),
            'aspartate': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '1'}),
            'bilirubin': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'chem_drawn_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'creatinine': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '1', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'lactate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '1', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_labresultchemistry'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.labresulthaematology': {
            'Meta': {'object_name': 'LabResultHaematology'},
            'anc_count': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'haem_drawn_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'hgb': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'mcv': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '1'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'platelet': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'wbc_count': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        'cancer_subject.labresulthaematologyaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'LabResultHaematologyAudit', 'db_table': "'cancer_subject_labresulthaematology_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'anc_count': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'haem_drawn_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'hgb': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'mcv': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '1'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'platelet': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '1'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_labresulthaematology'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'wbc_count': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        'cancer_subject.labresultheightweight': {
            'Meta': {'object_name': 'LabResultHeightWeight'},
            'cough2weeks': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'height': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '1'})
        },
        'cancer_subject.labresultheightweightaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'LabResultHeightWeightAudit', 'db_table': "'cancer_subject_labresultheightweight_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'cough2weeks': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'height': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_labresultheightweight'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '1'})
        },
        'cancer_subject.labresulthiv': {
            'Meta': {'object_name': 'LabResultHiv'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'test_date': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'test_result': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.labresulthivaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'LabResultHivAudit', 'db_table': "'cancer_subject_labresulthiv_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_labresulthiv'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'test_date': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'test_result': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.labresulttb': {
            'Meta': {'object_name': 'LabResultTb'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'tb_description': ('django.db.models.fields.CharField', [], {'max_length': '65'}),
            'tb_treatment': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tb_treatment_start': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.labresulttbaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'LabResultTbAudit', 'db_table': "'cancer_subject_labresulttb_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_labresulttb'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'tb_description': ('django.db.models.fields.CharField', [], {'max_length': '65'}),
            'tb_treatment': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tb_treatment_start': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.labresultviralload': {
            'Meta': {'object_name': 'LabResultViralload'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'vl_drawn_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'vl_result': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'cancer_subject.labresultviralloadaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'LabResultViralloadAudit', 'db_table': "'cancer_subject_labresultviralload_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_labresultviralload'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'vl_drawn_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'vl_result': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'cancer_subject.locator': {
            'Meta': {'object_name': 'Locator'},
            'contact_cell': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'contact_physical_address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'contact_rel': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_signed': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'home_visit_permission': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'mail_address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'may_call_work': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'may_contact_someone': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'may_follow_up': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'physical_address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True', 'null': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_cell': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_cell_alt': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_phone': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_phone_alt': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']"}),
            'subject_work_phone': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_work_place': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.locatoraudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'LocatorAudit', 'db_table': "'cancer_subject_locator_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'contact_cell': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'contact_physical_address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'contact_rel': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_signed': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'home_visit_permission': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'mail_address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'may_call_work': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'may_contact_someone': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'may_follow_up': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'physical_address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_locator'", 'null': 'True', 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_cell': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_cell_alt': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_phone': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_phone_alt': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_locator'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'subject_work_phone': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_work_place': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.oncologytreatmentplan': {
            'Meta': {'object_name': 'OncologyTreatmentPlan'},
            'chemo_intent': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'chemotherapy': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'planned_operation': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'radiation_plan': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'radiation_treatments': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'surgical_plan': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'treatment_plan': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.oncologytreatmentplanaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'OncologyTreatmentPlanAudit', 'db_table': "'cancer_subject_oncologytreatmentplan_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'chemo_intent': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'chemotherapy': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'planned_operation': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'radiation_plan': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'radiation_treatments': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_oncologytreatmentplan'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'surgical_plan': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'treatment_plan': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.oncologytreatmentrecord': {
            'Meta': {'object_name': 'OncologyTreatmentRecord'},
            'chemo_received': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'radiation_received': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'surgical_therapy': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'treatment_received': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.oncologytreatmentrecordaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'OncologyTreatmentRecordAudit', 'db_table': "'cancer_subject_oncologytreatmentrecord_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'chemo_received': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'radiation_received': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_oncologytreatmentrecord'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'surgical_therapy': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'treatment_received': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.otrchemo': {
            'Meta': {'object_name': 'OTRChemo'},
            'chemo_delays': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'chemo_intent': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'chemo_reduced': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'why_delayed': ('django.db.models.fields.CharField', [], {'max_length': '65', 'blank': 'True'}),
            'why_delayed_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'why_reduced': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'why_reduced_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'})
        },
        'cancer_subject.otrchemoaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'OTRChemoAudit', 'db_table': "'cancer_subject_otrchemo_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'chemo_delays': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'chemo_intent': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'chemo_reduced': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_otrchemo'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'why_delayed': ('django.db.models.fields.CharField', [], {'max_length': '65', 'blank': 'True'}),
            'why_delayed_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'why_reduced': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'why_reduced_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'})
        },
        'cancer_subject.otrradiation': {
            'Meta': {'object_name': 'OTRRadiation'},
            'amount_radiation': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'concomitant': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.otrradiationaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'OTRRadiationAudit', 'db_table': "'cancer_subject_otrradiation_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'amount_radiation': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'concomitant': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_otrradiation'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.otrsurgical': {
            'Meta': {'object_name': 'OTRSurgical'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_operation': ('django.db.models.fields.DateField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'operation_performed': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.otrsurgicalaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'OTRSurgicalAudit', 'db_table': "'cancer_subject_otrsurgical_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_operation': ('django.db.models.fields.DateField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'operation_performed': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_otrsurgical'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.referral': {
            'Meta': {'object_name': 'Referral'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'referral_date': ('django.db.models.fields.DateTimeField', [], {'max_length': '25'}),
            'referrals': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'why_referred': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        'cancer_subject.referralaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'ReferralAudit', 'db_table': "'cancer_subject_referral_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'referral_date': ('django.db.models.fields.DateTimeField', [], {'max_length': '25'}),
            'referrals': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_referral'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'why_referred': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        'cancer_subject.subjectconsent': {
            'Meta': {'object_name': 'SubjectConsent'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'confirm_identity': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'consent_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'guardian_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'identity': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '78L'}),
            'identity_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'is_dob_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'is_incarcerated': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'is_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_verified_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'may_store_samples': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'original_identifier': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'study_site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_variables.StudySite']"}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'subject_type': ('django.db.models.fields.CharField', [], {'default': "'undetermined'", 'max_length': '25', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.subjectconsentaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'SubjectConsentAudit', 'db_table': "'cancer_subject_subjectconsent_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'confirm_identity': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'consent_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'guardian_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'identity': ('django.db.models.fields.CharField', [], {'max_length': '78L'}),
            'identity_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'is_dob_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'is_incarcerated': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'is_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_verified_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'may_store_samples': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'original_identifier': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'study_site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_subjectconsent'", 'to': "orm['bhp_variables.StudySite']"}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'subject_type': ('django.db.models.fields.CharField', [], {'default': "'undetermined'", 'max_length': '25', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.subjectdeath': {
            'Meta': {'object_name': 'SubjectDeath'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_hospitalized': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'death_cause': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'death_cause_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_adverse.DeathCauseCategory']"}),
            'death_cause_info': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_adverse.DeathCauseInfo']"}),
            'death_cause_info_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'death_cause_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'death_date': ('django.db.models.fields.DateField', [], {}),
            'death_medical_responsibility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_adverse.DeathMedicalResponsibility']"}),
            'death_reason_hospitalized': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_adverse.DeathReasonHospitalized']", 'null': 'True', 'blank': 'True'}),
            'dx_code': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_code_lists.DxCode']", 'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'illness_duration': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'participant_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'perform_autopsy': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.subjectdeathaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'SubjectDeathAudit', 'db_table': "'cancer_subject_subjectdeath_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_hospitalized': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'death_cause': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'death_cause_category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_subjectdeath'", 'to': "orm['bhp_adverse.DeathCauseCategory']"}),
            'death_cause_info': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_subjectdeath'", 'to': "orm['bhp_adverse.DeathCauseInfo']"}),
            'death_cause_info_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'death_cause_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'death_date': ('django.db.models.fields.DateField', [], {}),
            'death_medical_responsibility': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_subjectdeath'", 'to': "orm['bhp_adverse.DeathMedicalResponsibility']"}),
            'death_reason_hospitalized': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'_audit_subjectdeath'", 'null': 'True', 'to': "orm['bhp_adverse.DeathReasonHospitalized']"}),
            'dx_code': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_subjectdeath'", 'max_length': '25', 'to': "orm['bhp_code_lists.DxCode']"}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'illness_duration': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'participant_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'perform_autopsy': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_subjectdeath'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.subjectoffstudy': {
            'Meta': {'object_name': 'SubjectOffStudy'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'offstudy_date': ('django.db.models.fields.DateField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.subjectoffstudyaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'SubjectOffStudyAudit', 'db_table': "'cancer_subject_subjectoffstudy_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'offstudy_date': ('django.db.models.fields.DateField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_subjectoffstudy'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.subjectvisit': {
            'Meta': {'object_name': 'SubjectVisit'},
            'appointment': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_appointment.Appointment']", 'unique': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'info_source': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_source_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'reason_unscheduled': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.subjectvisitaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'SubjectVisitAudit', 'db_table': "'cancer_subject_subjectvisit_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'appointment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_subjectvisit'", 'to': "orm['bhp_appointment.Appointment']"}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'info_source': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_source_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'reason_unscheduled': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.treatmentresponse': {
            'Meta': {'object_name': 'TreatmentResponse'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']", 'null': 'True'}),
            'tx_info_determinant': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cancer_subject.InfoDeterminant']", 'max_length': '45', 'symmetrical': 'False'}),
            'tx_response': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'tx_response_class': ('django.db.models.fields.CharField', [], {'max_length': '95'}),
            'tx_response_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.treatmentresponseaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'TreatmentResponseAudit', 'db_table': "'cancer_subject_treatmentresponse_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 10, 9, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_treatmentresponse'", 'null': 'True', 'to': "orm['cancer_subject.SubjectVisit']"}),
            'tx_response': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'tx_response_class': ('django.db.models.fields.CharField', [], {'max_length': '95'}),
            'tx_response_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'cancer_subject.whoillness': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'WhoIllness'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cancer_subject']