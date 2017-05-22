# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Deleting model 'InfoDeterminant'
        db.rename_table('cancer_subject_infodeterminant', 'cancer_list_infodeterminant')

        # Deleting model 'WhoIllness'
        db.rename_table('cancer_subject_whoillness', 'cancer_list_whoillness')

        # Adding index on 'BaseRiskAssessmentCancer', fields ['user_modified']
        db.create_index('cancer_subject_baseriskassessmentcancer', ['user_modified'])

        # Adding index on 'BaseRiskAssessmentCancer', fields ['user_created']
        db.create_index('cancer_subject_baseriskassessmentcancer', ['user_created'])


        # Changing field 'BaseRiskAssessmentCancer.subject_visit'
        db.alter_column('cancer_subject_baseriskassessmentcancer', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'BaseRiskAssessmentCancer', fields ['subject_visit']
        db.create_unique('cancer_subject_baseriskassessmentcancer', ['subject_visit_id'])

        # Adding index on 'LabResultChemistryAudit', fields ['user_modified']
        db.create_index('cancer_subject_labresultchemistry_audit', ['user_modified'])

        # Adding index on 'LabResultChemistryAudit', fields ['user_created']
        db.create_index('cancer_subject_labresultchemistry_audit', ['user_created'])


        # Changing field 'LabResultChemistryAudit.subject_visit'
        db.alter_column('cancer_subject_labresultchemistry_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding field 'SubjectConsent.consent_version_on_entry'
        db.add_column('cancer_subject_subjectconsent', 'consent_version_on_entry',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'SubjectConsent.consent_version_recent'
        db.add_column('cancer_subject_subjectconsent', 'consent_version_recent',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding index on 'SubjectConsent', fields ['user_created']
        db.create_index('cancer_subject_subjectconsent', ['user_created'])

        # Adding index on 'SubjectConsent', fields ['user_modified']
        db.create_index('cancer_subject_subjectconsent', ['user_modified'])

        # Adding index on 'SubjectOffStudy', fields ['user_modified']
        db.create_index('cancer_subject_subjectoffstudy', ['user_modified'])

        # Adding index on 'SubjectOffStudy', fields ['user_created']
        db.create_index('cancer_subject_subjectoffstudy', ['user_created'])

        # Adding field 'OTRRadiationAudit.radiation_details'
        db.add_column('cancer_subject_otrradiation_audit', 'radiation_details',
                      self.gf('django.db.models.fields.CharField')(default='-', max_length=3),
                      keep_default=False)


        # Changing field 'OTRRadiationAudit.concomitant'
        db.alter_column('cancer_subject_otrradiation_audit', 'concomitant', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))
        # Adding index on 'OTRRadiationAudit', fields ['user_modified']
        db.create_index('cancer_subject_otrradiation_audit', ['user_modified'])


        # Changing field 'OTRRadiationAudit.amount_radiation'
        db.alter_column('cancer_subject_otrradiation_audit', 'amount_radiation', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'OTRRadiationAudit.subject_visit'
        db.alter_column('cancer_subject_otrradiation_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'OTRRadiationAudit', fields ['user_created']
        db.create_index('cancer_subject_otrradiation_audit', ['user_created'])

        # Adding index on 'BaseRiskAssessment', fields ['user_modified']
        db.create_index('cancer_subject_baseriskassessment', ['user_modified'])

        # Adding index on 'BaseRiskAssessment', fields ['user_created']
        db.create_index('cancer_subject_baseriskassessment', ['user_created'])


        # Changing field 'BaseRiskAssessment.subject_visit'
        db.alter_column('cancer_subject_baseriskassessment', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'BaseRiskAssessment', fields ['subject_visit']
        db.create_unique('cancer_subject_baseriskassessment', ['subject_visit_id'])

        # Adding index on 'TreatmentResponseAudit', fields ['user_modified']
        db.create_index('cancer_subject_treatmentresponse_audit', ['user_modified'])

        # Adding index on 'TreatmentResponseAudit', fields ['user_created']
        db.create_index('cancer_subject_treatmentresponse_audit', ['user_created'])


        # Changing field 'TreatmentResponseAudit.subject_visit'
        db.alter_column('cancer_subject_treatmentresponse_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'BHHHivTest', fields ['user_modified']
        db.create_index('cancer_subject_bhhhivtest', ['user_modified'])


        # Changing field 'BHHHivTest.subject_visit'
        db.alter_column('cancer_subject_bhhhivtest', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'BHHHivTest', fields ['subject_visit']
        db.create_unique('cancer_subject_bhhhivtest', ['subject_visit_id'])

        # Adding index on 'BHHHivTest', fields ['user_created']
        db.create_index('cancer_subject_bhhhivtest', ['user_created'])

        # Adding index on 'LabResult', fields ['user_modified']
        db.create_index('cancer_subject_labresult', ['user_modified'])


        # Changing field 'LabResult.subject_visit'
        db.alter_column('cancer_subject_labresult', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'LabResult', fields ['subject_visit']
        db.create_unique('cancer_subject_labresult', ['subject_visit_id'])

        # Adding index on 'LabResult', fields ['user_created']
        db.create_index('cancer_subject_labresult', ['user_created'])

        # Adding index on 'BHHWhoIllness', fields ['user_modified']
        db.create_index('cancer_subject_bhhwhoillness', ['user_modified'])


        # Changing field 'BHHWhoIllness.subject_visit'
        db.alter_column('cancer_subject_bhhwhoillness', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'BHHWhoIllness', fields ['subject_visit']
        db.create_unique('cancer_subject_bhhwhoillness', ['subject_visit_id'])

        # Adding index on 'BHHWhoIllness', fields ['user_created']
        db.create_index('cancer_subject_bhhwhoillness', ['user_created'])

        # Adding index on 'ReferralAudit', fields ['user_modified']
        db.create_index('cancer_subject_referral_audit', ['user_modified'])

        # Adding index on 'ReferralAudit', fields ['user_created']
        db.create_index('cancer_subject_referral_audit', ['user_created'])

        # Adding index on 'OTRSurgicalAudit', fields ['user_modified']
        db.create_index('cancer_subject_otrsurgical_audit', ['user_modified'])

        # Adding index on 'OTRSurgicalAudit', fields ['user_created']
        db.create_index('cancer_subject_otrsurgical_audit', ['user_created'])


        # Changing field 'OTRSurgicalAudit.subject_visit'
        db.alter_column('cancer_subject_otrsurgical_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'ChemoMedPlan', fields ['user_modified']
        db.create_index('cancer_subject_chemomedplan', ['user_modified'])

        # Adding index on 'ChemoMedPlan', fields ['user_created']
        db.create_index('cancer_subject_chemomedplan', ['user_created'])

        # Adding index on 'BaseRiskAssessmentSmokingAudit', fields ['user_modified']
        db.create_index('cancer_subject_baseriskassessmentsmoking_audit', ['user_modified'])

        # Adding index on 'BaseRiskAssessmentSmokingAudit', fields ['user_created']
        db.create_index('cancer_subject_baseriskassessmentsmoking_audit', ['user_created'])


        # Changing field 'BaseRiskAssessmentSmokingAudit.subject_visit'
        db.alter_column('cancer_subject_baseriskassessmentsmoking_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'ChemoMedRecord', fields ['user_modified']
        db.create_index('cancer_subject_chemomedrecord', ['user_modified'])

        # Adding index on 'ChemoMedRecord', fields ['user_created']
        db.create_index('cancer_subject_chemomedrecord', ['user_created'])

        # Adding index on 'BaseRiskAssessmentChemicalAudit', fields ['user_modified']
        db.create_index('cancer_subject_baseriskassessmentchemical_audit', ['user_modified'])

        # Adding index on 'BaseRiskAssessmentChemicalAudit', fields ['user_created']
        db.create_index('cancer_subject_baseriskassessmentchemical_audit', ['user_created'])


        # Changing field 'BaseRiskAssessmentChemicalAudit.subject_visit'
        db.alter_column('cancer_subject_baseriskassessmentchemical_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding field 'SubjectConsentAudit.consent_version_on_entry'
        db.add_column('cancer_subject_subjectconsent_audit', 'consent_version_on_entry',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'SubjectConsentAudit.consent_version_recent'
        db.add_column('cancer_subject_subjectconsent_audit', 'consent_version_recent',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding index on 'SubjectConsentAudit', fields ['user_created']
        db.create_index('cancer_subject_subjectconsent_audit', ['user_created'])

        # Adding index on 'SubjectConsentAudit', fields ['user_modified']
        db.create_index('cancer_subject_subjectconsent_audit', ['user_modified'])

        # Adding index on 'Locator', fields ['user_created']
        db.create_index('cancer_subject_locator', ['user_created'])

        # Adding index on 'Locator', fields ['user_modified']
        db.create_index('cancer_subject_locator', ['user_modified'])

        # Adding index on 'ActivityAndFunctioningAudit', fields ['user_created']
        db.create_index('cancer_subject_activityandfunctioning_audit', ['user_created'])

        # Adding index on 'ActivityAndFunctioningAudit', fields ['user_modified']
        db.create_index('cancer_subject_activityandfunctioning_audit', ['user_modified'])


        # Changing field 'ActivityAndFunctioningAudit.subject_visit'
        db.alter_column('cancer_subject_activityandfunctioning_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'OTRSurgical', fields ['user_modified']
        db.create_index('cancer_subject_otrsurgical', ['user_modified'])


        # Changing field 'OTRSurgical.subject_visit'
        db.alter_column('cancer_subject_otrsurgical', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'OTRSurgical', fields ['subject_visit']
        db.create_unique('cancer_subject_otrsurgical', ['subject_visit_id'])

        # Adding index on 'OTRSurgical', fields ['user_created']
        db.create_index('cancer_subject_otrsurgical', ['user_created'])

        # Adding index on 'BaseRiskAssessmentFuelAudit', fields ['user_modified']
        db.create_index('cancer_subject_baseriskassessmentfuel_audit', ['user_modified'])

        # Adding index on 'BaseRiskAssessmentFuelAudit', fields ['user_created']
        db.create_index('cancer_subject_baseriskassessmentfuel_audit', ['user_created'])


        # Changing field 'BaseRiskAssessmentFuelAudit.subject_visit'
        db.alter_column('cancer_subject_baseriskassessmentfuel_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'SubjectVisitAudit', fields ['user_modified']
        db.create_index('cancer_subject_subjectvisit_audit', ['user_modified'])

        # Adding index on 'SubjectVisitAudit', fields ['user_created']
        db.create_index('cancer_subject_subjectvisit_audit', ['user_created'])

        # Adding index on 'BaseRiskAssessmentCancerAudit', fields ['user_modified']
        db.create_index('cancer_subject_baseriskassessmentcancer_audit', ['user_modified'])

        # Adding index on 'BaseRiskAssessmentCancerAudit', fields ['user_created']
        db.create_index('cancer_subject_baseriskassessmentcancer_audit', ['user_created'])


        # Changing field 'BaseRiskAssessmentCancerAudit.subject_visit'
        db.alter_column('cancer_subject_baseriskassessmentcancer_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'BHHWhoIllnessAudit', fields ['user_modified']
        db.create_index('cancer_subject_bhhwhoillness_audit', ['user_modified'])

        # Adding index on 'BHHWhoIllnessAudit', fields ['user_created']
        db.create_index('cancer_subject_bhhwhoillness_audit', ['user_created'])


        # Changing field 'BHHWhoIllnessAudit.subject_visit'
        db.alter_column('cancer_subject_bhhwhoillness_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'ChemoMedPlanAudit', fields ['user_modified']
        db.create_index('cancer_subject_chemomedplan_audit', ['user_modified'])

        # Adding index on 'ChemoMedPlanAudit', fields ['user_created']
        db.create_index('cancer_subject_chemomedplan_audit', ['user_created'])

        # Adding index on 'BaseRiskAssessmentAudit', fields ['user_created']
        db.create_index('cancer_subject_baseriskassessment_audit', ['user_created'])

        # Adding index on 'BaseRiskAssessmentAudit', fields ['user_modified']
        db.create_index('cancer_subject_baseriskassessment_audit', ['user_modified'])


        # Changing field 'BaseRiskAssessmentAudit.subject_visit'
        db.alter_column('cancer_subject_baseriskassessment_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'Referral', fields ['user_modified']
        db.create_index('cancer_subject_referral', ['user_modified'])

        # Adding index on 'Referral', fields ['user_created']
        db.create_index('cancer_subject_referral', ['user_created'])

        # Adding index on 'BaselineHIVHistoryAudit', fields ['user_modified']
        db.create_index('cancer_subject_baselinehivhistory_audit', ['user_modified'])

        # Adding index on 'BaselineHIVHistoryAudit', fields ['user_created']
        db.create_index('cancer_subject_baselinehivhistory_audit', ['user_created'])


        # Changing field 'BaselineHIVHistoryAudit.subject_visit'
        db.alter_column('cancer_subject_baselinehivhistory_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'ActivityAndFunctioning', fields ['user_modified']
        db.create_index('cancer_subject_activityandfunctioning', ['user_modified'])


        # Changing field 'ActivityAndFunctioning.subject_visit'
        db.alter_column('cancer_subject_activityandfunctioning', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'ActivityAndFunctioning', fields ['subject_visit']
        db.create_unique('cancer_subject_activityandfunctioning', ['subject_visit_id'])

        # Adding index on 'ActivityAndFunctioning', fields ['user_created']
        db.create_index('cancer_subject_activityandfunctioning', ['user_created'])

        # Adding index on 'OncologyTreatmentRecordAudit', fields ['user_modified']
        db.create_index('cancer_subject_oncologytreatmentrecord_audit', ['user_modified'])

        # Adding index on 'OncologyTreatmentRecordAudit', fields ['user_created']
        db.create_index('cancer_subject_oncologytreatmentrecord_audit', ['user_created'])


        # Changing field 'OncologyTreatmentRecordAudit.subject_visit'
        db.alter_column('cancer_subject_oncologytreatmentrecord_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'EnrollmentChecklist', fields ['user_modified']
        db.create_index('cancer_subject_enrollmentchecklist', ['user_modified'])

        # Adding index on 'EnrollmentChecklist', fields ['user_created']
        db.create_index('cancer_subject_enrollmentchecklist', ['user_created'])

        # Adding index on 'LabResultAudit', fields ['user_created']
        db.create_index('cancer_subject_labresult_audit', ['user_created'])

        # Adding index on 'LabResultAudit', fields ['user_modified']
        db.create_index('cancer_subject_labresult_audit', ['user_modified'])


        # Changing field 'LabResultAudit.subject_visit'
        db.alter_column('cancer_subject_labresult_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'TreatmentResponse', fields ['user_modified']
        db.create_index('cancer_subject_treatmentresponse', ['user_modified'])


        # Changing field 'TreatmentResponse.subject_visit'
        db.alter_column('cancer_subject_treatmentresponse', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'TreatmentResponse', fields ['subject_visit']
        db.create_unique('cancer_subject_treatmentresponse', ['subject_visit_id'])

        # Adding index on 'TreatmentResponse', fields ['user_created']
        db.create_index('cancer_subject_treatmentresponse', ['user_created'])

        # Deleting field 'HaartRecordAudit.hiv'
        db.delete_column('cancer_subject_haartrecord_audit', 'hiv')

        # Adding index on 'HaartRecordAudit', fields ['user_modified']
        db.create_index('cancer_subject_haartrecord_audit', ['user_modified'])

        # Adding index on 'HaartRecordAudit', fields ['user_created']
        db.create_index('cancer_subject_haartrecord_audit', ['user_created'])


        # Changing field 'HaartRecordAudit.subject_visit'
        db.alter_column('cancer_subject_haartrecord_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'BHHCd4Audit', fields ['user_modified']
        db.create_index('cancer_subject_bhhcd4_audit', ['user_modified'])

        # Adding index on 'BHHCd4Audit', fields ['user_created']
        db.create_index('cancer_subject_bhhcd4_audit', ['user_created'])


        # Changing field 'BHHCd4Audit.subject_visit'
        db.alter_column('cancer_subject_bhhcd4_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'ChemoMedRecordAudit', fields ['user_modified']
        db.create_index('cancer_subject_chemomedrecord_audit', ['user_modified'])

        # Adding index on 'ChemoMedRecordAudit', fields ['user_created']
        db.create_index('cancer_subject_chemomedrecord_audit', ['user_created'])


        # Changing field 'LabResultHeightWeight.weight'
        db.alter_column('cancer_subject_labresultheightweight', 'weight', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1))
        # Adding index on 'LabResultHeightWeight', fields ['user_modified']
        db.create_index('cancer_subject_labresultheightweight', ['user_modified'])


        # Changing field 'LabResultHeightWeight.subject_visit'
        db.alter_column('cancer_subject_labresultheightweight', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'LabResultHeightWeight', fields ['subject_visit']
        db.create_unique('cancer_subject_labresultheightweight', ['subject_visit_id'])

        # Adding index on 'LabResultHeightWeight', fields ['user_created']
        db.create_index('cancer_subject_labresultheightweight', ['user_created'])

        # Adding index on 'BHHHivTestAudit', fields ['user_modified']
        db.create_index('cancer_subject_bhhhivtest_audit', ['user_modified'])

        # Adding index on 'BHHHivTestAudit', fields ['user_created']
        db.create_index('cancer_subject_bhhhivtest_audit', ['user_created'])


        # Changing field 'BHHHivTestAudit.subject_visit'
        db.alter_column('cancer_subject_bhhhivtest_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'BaseRiskAssessmentEating', fields ['user_modified']
        db.create_index('cancer_subject_baseriskassessmenteating', ['user_modified'])


        # Changing field 'BaseRiskAssessmentEating.subject_visit'
        db.alter_column('cancer_subject_baseriskassessmenteating', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'BaseRiskAssessmentEating', fields ['subject_visit']
        db.create_unique('cancer_subject_baseriskassessmenteating', ['subject_visit_id'])

        # Adding index on 'BaseRiskAssessmentEating', fields ['user_created']
        db.create_index('cancer_subject_baseriskassessmenteating', ['user_created'])

        # Adding index on 'BaseRiskAssessmentEatingAudit', fields ['user_modified']
        db.create_index('cancer_subject_baseriskassessmenteating_audit', ['user_modified'])


        # Changing field 'BaseRiskAssessmentEatingAudit.subject_visit'
        db.alter_column('cancer_subject_baseriskassessmenteating_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'BaseRiskAssessmentEatingAudit', fields ['user_created']
        db.create_index('cancer_subject_baseriskassessmenteating_audit', ['user_created'])

        # Adding index on 'BaseRiskAssessmentFemaleAudit', fields ['user_modified']
        db.create_index('cancer_subject_baseriskassessmentfemale_audit', ['user_modified'])

        # Adding index on 'BaseRiskAssessmentFemaleAudit', fields ['user_created']
        db.create_index('cancer_subject_baseriskassessmentfemale_audit', ['user_created'])


        # Changing field 'BaseRiskAssessmentFemaleAudit.subject_visit'
        db.alter_column('cancer_subject_baseriskassessmentfemale_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'BHHCd4', fields ['user_modified']
        db.create_index('cancer_subject_bhhcd4', ['user_modified'])


        # Changing field 'BHHCd4.subject_visit'
        db.alter_column('cancer_subject_bhhcd4', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'BHHCd4', fields ['subject_visit']
        db.create_unique('cancer_subject_bhhcd4', ['subject_visit_id'])

        # Adding index on 'BHHCd4', fields ['user_created']
        db.create_index('cancer_subject_bhhcd4', ['user_created'])

        # Adding index on 'LabResultHaematologyAudit', fields ['user_modified']
        db.create_index('cancer_subject_labresulthaematology_audit', ['user_modified'])


        # Changing field 'LabResultHaematologyAudit.subject_visit'
        db.alter_column('cancer_subject_labresulthaematology_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'LabResultHaematologyAudit', fields ['user_created']
        db.create_index('cancer_subject_labresulthaematology_audit', ['user_created'])

        # Adding index on 'BaselineHIVHistory', fields ['user_modified']
        db.create_index('cancer_subject_baselinehivhistory', ['user_modified'])


        # Changing field 'BaselineHIVHistory.subject_visit'
        db.alter_column('cancer_subject_baselinehivhistory', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'BaselineHIVHistory', fields ['subject_visit']
        db.create_unique('cancer_subject_baselinehivhistory', ['subject_visit_id'])

        # Adding index on 'BaselineHIVHistory', fields ['user_created']
        db.create_index('cancer_subject_baselinehivhistory', ['user_created'])

        # Adding index on 'LabResultViralload', fields ['user_modified']
        db.create_index('cancer_subject_labresultviralload', ['user_modified'])


        # Changing field 'LabResultViralload.subject_visit'
        db.alter_column('cancer_subject_labresultviralload', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'LabResultViralload', fields ['subject_visit']
        db.create_unique('cancer_subject_labresultviralload', ['subject_visit_id'])

        # Adding index on 'LabResultViralload', fields ['user_created']
        db.create_index('cancer_subject_labresultviralload', ['user_created'])

        # Adding index on 'LabResultCd4Audit', fields ['user_modified']
        db.create_index('cancer_subject_labresultcd4_audit', ['user_modified'])

        # Adding index on 'LabResultCd4Audit', fields ['user_created']
        db.create_index('cancer_subject_labresultcd4_audit', ['user_created'])


        # Changing field 'LabResultCd4Audit.subject_visit'
        db.alter_column('cancer_subject_labresultcd4_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'SubjectDeath', fields ['user_modified']
        db.create_index('cancer_subject_subjectdeath', ['user_modified'])

        # Adding index on 'SubjectDeath', fields ['user_created']
        db.create_index('cancer_subject_subjectdeath', ['user_created'])


        # Changing field 'OncologyTreatmentPlanAudit.chemotherapy'
        db.alter_column('cancer_subject_oncologytreatmentplan_audit', 'chemotherapy', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))

        # Changing field 'OncologyTreatmentPlanAudit.surgical_plan'
        db.alter_column('cancer_subject_oncologytreatmentplan_audit', 'surgical_plan', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))

        # Changing field 'OncologyTreatmentPlanAudit.radiation_plan'
        db.alter_column('cancer_subject_oncologytreatmentplan_audit', 'radiation_plan', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))
        # Adding index on 'OncologyTreatmentPlanAudit', fields ['user_modified']
        db.create_index('cancer_subject_oncologytreatmentplan_audit', ['user_modified'])


        # Changing field 'OncologyTreatmentPlanAudit.chemo_intent'
        db.alter_column('cancer_subject_oncologytreatmentplan_audit', 'chemo_intent', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))
        # Adding index on 'OncologyTreatmentPlanAudit', fields ['user_created']
        db.create_index('cancer_subject_oncologytreatmentplan_audit', ['user_created'])


        # Changing field 'OncologyTreatmentPlanAudit.subject_visit'
        db.alter_column('cancer_subject_oncologytreatmentplan_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'BaseRiskAssessmentChemical', fields ['user_modified']
        db.create_index('cancer_subject_baseriskassessmentchemical', ['user_modified'])

        # Adding index on 'BaseRiskAssessmentChemical', fields ['user_created']
        db.create_index('cancer_subject_baseriskassessmentchemical', ['user_created'])


        # Changing field 'BaseRiskAssessmentChemical.subject_visit'
        db.alter_column('cancer_subject_baseriskassessmentchemical', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'BaseRiskAssessmentChemical', fields ['subject_visit']
        db.create_unique('cancer_subject_baseriskassessmentchemical', ['subject_visit_id'])

        # Adding index on 'BaseRiskAssessmentDemo', fields ['user_created']
        db.create_index('cancer_subject_baseriskassessmentdemo', ['user_created'])

        # Adding index on 'BaseRiskAssessmentDemo', fields ['user_modified']
        db.create_index('cancer_subject_baseriskassessmentdemo', ['user_modified'])


        # Changing field 'BaseRiskAssessmentDemo.subject_visit'
        db.alter_column('cancer_subject_baseriskassessmentdemo', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'BaseRiskAssessmentDemo', fields ['subject_visit']
        db.create_unique('cancer_subject_baseriskassessmentdemo', ['subject_visit_id'])

        # Adding index on 'SubjectVisit', fields ['user_modified']
        db.create_index('cancer_subject_subjectvisit', ['user_modified'])

        # Adding index on 'SubjectVisit', fields ['user_created']
        db.create_index('cancer_subject_subjectvisit', ['user_created'])

        # Adding index on 'LabResultCd4', fields ['user_modified']
        db.create_index('cancer_subject_labresultcd4', ['user_modified'])


        # Changing field 'LabResultCd4.subject_visit'
        db.alter_column('cancer_subject_labresultcd4', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'LabResultCd4', fields ['subject_visit']
        db.create_unique('cancer_subject_labresultcd4', ['subject_visit_id'])

        # Adding index on 'LabResultCd4', fields ['user_created']
        db.create_index('cancer_subject_labresultcd4', ['user_created'])

        # Adding index on 'OTRChemoAudit', fields ['user_modified']
        db.create_index('cancer_subject_otrchemo_audit', ['user_modified'])

        # Adding index on 'OTRChemoAudit', fields ['user_created']
        db.create_index('cancer_subject_otrchemo_audit', ['user_created'])


        # Changing field 'OTRChemoAudit.subject_visit'
        db.alter_column('cancer_subject_otrchemo_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'OncologyTreatmentRecord', fields ['user_modified']
        db.create_index('cancer_subject_oncologytreatmentrecord', ['user_modified'])


        # Changing field 'OncologyTreatmentRecord.subject_visit'
        db.alter_column('cancer_subject_oncologytreatmentrecord', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'OncologyTreatmentRecord', fields ['subject_visit']
        db.create_unique('cancer_subject_oncologytreatmentrecord', ['subject_visit_id'])

        # Adding index on 'OncologyTreatmentRecord', fields ['user_created']
        db.create_index('cancer_subject_oncologytreatmentrecord', ['user_created'])

        # Adding index on 'BaseRiskAssessmentSun', fields ['user_modified']
        db.create_index('cancer_subject_baseriskassessmentsun', ['user_modified'])


        # Changing field 'BaseRiskAssessmentSun.subject_visit'
        db.alter_column('cancer_subject_baseriskassessmentsun', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'BaseRiskAssessmentSun', fields ['subject_visit']
        db.create_unique('cancer_subject_baseriskassessmentsun', ['subject_visit_id'])

        # Adding index on 'BaseRiskAssessmentSun', fields ['user_created']
        db.create_index('cancer_subject_baseriskassessmentsun', ['user_created'])


        # Changing field 'CancerDiagnosis.cancer_stage_modifier'
        db.alter_column('cancer_subject_cancerdiagnosis', 'cancer_stage_modifier', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'CancerDiagnosis.cancer_category'
        db.alter_column('cancer_subject_cancerdiagnosis', 'cancer_category', self.gf('django.db.models.fields.CharField')(max_length=75, null=True))
        # Adding index on 'CancerDiagnosis', fields ['user_created']
        db.create_index('cancer_subject_cancerdiagnosis', ['user_created'])


        # Changing field 'CancerDiagnosis.tumour'
        db.alter_column('cancer_subject_cancerdiagnosis', 'tumour', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))
        # Adding index on 'CancerDiagnosis', fields ['user_modified']
        db.create_index('cancer_subject_cancerdiagnosis', ['user_modified'])


        # Changing field 'CancerDiagnosis.lymph_nodes'
        db.alter_column('cancer_subject_cancerdiagnosis', 'lymph_nodes', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'CancerDiagnosis.subject_visit'
        db.alter_column('cancer_subject_cancerdiagnosis', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'CancerDiagnosis', fields ['subject_visit']
        db.create_unique('cancer_subject_cancerdiagnosis', ['subject_visit_id'])


        # Changing field 'CancerDiagnosis.first_evaluation'
        db.alter_column('cancer_subject_cancerdiagnosis', 'first_evaluation', self.gf('django.db.models.fields.DateField')(max_length=25, null=True))

        # Changing field 'CancerDiagnosis.symptom_prompt'
        db.alter_column('cancer_subject_cancerdiagnosis', 'symptom_prompt', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))

        # Changing field 'CancerDiagnosis.lymph_basis'
        db.alter_column('cancer_subject_cancerdiagnosis', 'lymph_basis', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'CancerDiagnosis.symptom_first_noticed'
        db.alter_column('cancer_subject_cancerdiagnosis', 'symptom_first_noticed', self.gf('django.db.models.fields.DateField')(max_length=25, null=True))

        # Changing field 'CancerDiagnosis.diagnosis_word'
        db.alter_column('cancer_subject_cancerdiagnosis', 'diagnosis_word', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'CancerDiagnosis.tumour_basis'
        db.alter_column('cancer_subject_cancerdiagnosis', 'tumour_basis', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'CancerDiagnosis.diagnosis_basis'
        db.alter_column('cancer_subject_cancerdiagnosis', 'diagnosis_basis', self.gf('django.db.models.fields.CharField')(max_length=45, null=True))

        # Changing field 'CancerDiagnosis.metastasis_basis'
        db.alter_column('cancer_subject_cancerdiagnosis', 'metastasis_basis', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'CancerDiagnosis.metastasis'
        db.alter_column('cancer_subject_cancerdiagnosis', 'metastasis', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))
        # Adding index on 'BaseRiskAssessmentDemoAudit', fields ['user_created']
        db.create_index('cancer_subject_baseriskassessmentdemo_audit', ['user_created'])

        # Adding index on 'BaseRiskAssessmentDemoAudit', fields ['user_modified']
        db.create_index('cancer_subject_baseriskassessmentdemo_audit', ['user_modified'])


        # Changing field 'BaseRiskAssessmentDemoAudit.subject_visit'
        db.alter_column('cancer_subject_baseriskassessmentdemo_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'LabResultHivAudit', fields ['user_modified']
        db.create_index('cancer_subject_labresulthiv_audit', ['user_modified'])

        # Adding index on 'LabResultHivAudit', fields ['user_created']
        db.create_index('cancer_subject_labresulthiv_audit', ['user_created'])


        # Changing field 'LabResultHivAudit.subject_visit'
        db.alter_column('cancer_subject_labresulthiv_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Deleting field 'HaartRecord.hiv'
        db.delete_column('cancer_subject_haartrecord', 'hiv')

        # Adding index on 'HaartRecord', fields ['user_modified']
        db.create_index('cancer_subject_haartrecord', ['user_modified'])


        # Changing field 'HaartRecord.subject_visit'
        db.alter_column('cancer_subject_haartrecord', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'HaartRecord', fields ['subject_visit']
        db.create_unique('cancer_subject_haartrecord', ['subject_visit_id'])

        # Adding index on 'HaartRecord', fields ['user_created']
        db.create_index('cancer_subject_haartrecord', ['user_created'])

        # Adding index on 'LocatorAudit', fields ['user_created']
        db.create_index('cancer_subject_locator_audit', ['user_created'])

        # Adding index on 'LocatorAudit', fields ['user_modified']
        db.create_index('cancer_subject_locator_audit', ['user_modified'])

        # Adding index on 'LabResultViralloadAudit', fields ['user_modified']
        db.create_index('cancer_subject_labresultviralload_audit', ['user_modified'])

        # Adding index on 'LabResultViralloadAudit', fields ['user_created']
        db.create_index('cancer_subject_labresultviralload_audit', ['user_created'])


        # Changing field 'LabResultViralloadAudit.subject_visit'
        db.alter_column('cancer_subject_labresultviralload_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'SubjectDeathAudit', fields ['user_created']
        db.create_index('cancer_subject_subjectdeath_audit', ['user_created'])

        # Adding index on 'SubjectDeathAudit', fields ['user_modified']
        db.create_index('cancer_subject_subjectdeath_audit', ['user_modified'])

        # Adding index on 'BaseRiskAssessmentAlcohol', fields ['user_modified']
        db.create_index('cancer_subject_baseriskassessmentalcohol', ['user_modified'])


        # Changing field 'BaseRiskAssessmentAlcohol.subject_visit'
        db.alter_column('cancer_subject_baseriskassessmentalcohol', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'BaseRiskAssessmentAlcohol', fields ['subject_visit']
        db.create_unique('cancer_subject_baseriskassessmentalcohol', ['subject_visit_id'])

        # Adding index on 'BaseRiskAssessmentAlcohol', fields ['user_created']
        db.create_index('cancer_subject_baseriskassessmentalcohol', ['user_created'])

        # Adding index on 'LabResultTb', fields ['user_modified']
        db.create_index('cancer_subject_labresulttb', ['user_modified'])


        # Changing field 'LabResultTb.subject_visit'
        db.alter_column('cancer_subject_labresulttb', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'LabResultTb', fields ['subject_visit']
        db.create_unique('cancer_subject_labresulttb', ['subject_visit_id'])

        # Adding index on 'LabResultTb', fields ['user_created']
        db.create_index('cancer_subject_labresulttb', ['user_created'])

        # Adding index on 'HaartMedRecordAudit', fields ['user_modified']
        db.create_index('cancer_subject_haartmedrecord_audit', ['user_modified'])

        # Adding index on 'HaartMedRecordAudit', fields ['user_created']
        db.create_index('cancer_subject_haartmedrecord_audit', ['user_created'])

        # Adding index on 'BaseRiskAssessmentSmoking', fields ['user_modified']
        db.create_index('cancer_subject_baseriskassessmentsmoking', ['user_modified'])


        # Changing field 'BaseRiskAssessmentSmoking.subject_visit'
        db.alter_column('cancer_subject_baseriskassessmentsmoking', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'BaseRiskAssessmentSmoking', fields ['subject_visit']
        db.create_unique('cancer_subject_baseriskassessmentsmoking', ['subject_visit_id'])

        # Adding index on 'BaseRiskAssessmentSmoking', fields ['user_created']
        db.create_index('cancer_subject_baseriskassessmentsmoking', ['user_created'])

        # Adding field 'OTRRadiation.radiation_details'
        db.add_column('cancer_subject_otrradiation', 'radiation_details',
                      self.gf('django.db.models.fields.CharField')(default='-', max_length=3),
                      keep_default=False)


        # Changing field 'OTRRadiation.concomitant'
        db.alter_column('cancer_subject_otrradiation', 'concomitant', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))

        # Changing field 'OTRRadiation.amount_radiation'
        db.alter_column('cancer_subject_otrradiation', 'amount_radiation', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))
        # Adding index on 'OTRRadiation', fields ['user_modified']
        db.create_index('cancer_subject_otrradiation', ['user_modified'])

        # Adding index on 'OTRRadiation', fields ['user_created']
        db.create_index('cancer_subject_otrradiation', ['user_created'])


        # Changing field 'OTRRadiation.subject_visit'
        db.alter_column('cancer_subject_otrradiation', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'OTRRadiation', fields ['subject_visit']
        db.create_unique('cancer_subject_otrradiation', ['subject_visit_id'])

        # Adding index on 'BaseRiskAssessmentMiningAudit', fields ['user_modified']
        db.create_index('cancer_subject_baseriskassessmentmining_audit', ['user_modified'])


        # Changing field 'BaseRiskAssessmentMiningAudit.subject_visit'
        db.alter_column('cancer_subject_baseriskassessmentmining_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'BaseRiskAssessmentMiningAudit', fields ['user_created']
        db.create_index('cancer_subject_baseriskassessmentmining_audit', ['user_created'])

        # Adding index on 'OTRChemo', fields ['user_modified']
        db.create_index('cancer_subject_otrchemo', ['user_modified'])

        # Adding index on 'OTRChemo', fields ['user_created']
        db.create_index('cancer_subject_otrchemo', ['user_created'])


        # Changing field 'OTRChemo.subject_visit'
        db.alter_column('cancer_subject_otrchemo', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'OTRChemo', fields ['subject_visit']
        db.create_unique('cancer_subject_otrchemo', ['subject_visit_id'])

        # Adding index on 'BaseRiskAssessmentFemale', fields ['user_modified']
        db.create_index('cancer_subject_baseriskassessmentfemale', ['user_modified'])


        # Changing field 'BaseRiskAssessmentFemale.subject_visit'
        db.alter_column('cancer_subject_baseriskassessmentfemale', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'BaseRiskAssessmentFemale', fields ['subject_visit']
        db.create_unique('cancer_subject_baseriskassessmentfemale', ['subject_visit_id'])

        # Adding index on 'BaseRiskAssessmentFemale', fields ['user_created']
        db.create_index('cancer_subject_baseriskassessmentfemale', ['user_created'])

        # Adding index on 'HaartMedRecord', fields ['user_modified']
        db.create_index('cancer_subject_haartmedrecord', ['user_modified'])

        # Adding index on 'HaartMedRecord', fields ['user_created']
        db.create_index('cancer_subject_haartmedrecord', ['user_created'])


        # Changing field 'OncologyTreatmentPlan.surgical_plan'
        db.alter_column('cancer_subject_oncologytreatmentplan', 'surgical_plan', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))
        # Adding index on 'OncologyTreatmentPlan', fields ['user_modified']
        db.create_index('cancer_subject_oncologytreatmentplan', ['user_modified'])


        # Changing field 'OncologyTreatmentPlan.chemo_intent'
        db.alter_column('cancer_subject_oncologytreatmentplan', 'chemo_intent', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))
        # Adding index on 'OncologyTreatmentPlan', fields ['user_created']
        db.create_index('cancer_subject_oncologytreatmentplan', ['user_created'])


        # Changing field 'OncologyTreatmentPlan.chemotherapy'
        db.alter_column('cancer_subject_oncologytreatmentplan', 'chemotherapy', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))

        # Changing field 'OncologyTreatmentPlan.radiation_plan'
        db.alter_column('cancer_subject_oncologytreatmentplan', 'radiation_plan', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))

        # Changing field 'OncologyTreatmentPlan.subject_visit'
        db.alter_column('cancer_subject_oncologytreatmentplan', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'OncologyTreatmentPlan', fields ['subject_visit']
        db.create_unique('cancer_subject_oncologytreatmentplan', ['subject_visit_id'])


        # Changing field 'CancerDiagnosisAudit.cancer_stage_modifier'
        db.alter_column('cancer_subject_cancerdiagnosis_audit', 'cancer_stage_modifier', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'CancerDiagnosisAudit.cancer_category'
        db.alter_column('cancer_subject_cancerdiagnosis_audit', 'cancer_category', self.gf('django.db.models.fields.CharField')(max_length=75, null=True))
        # Adding index on 'CancerDiagnosisAudit', fields ['user_created']
        db.create_index('cancer_subject_cancerdiagnosis_audit', ['user_created'])


        # Changing field 'CancerDiagnosisAudit.tumour'
        db.alter_column('cancer_subject_cancerdiagnosis_audit', 'tumour', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))
        # Adding index on 'CancerDiagnosisAudit', fields ['user_modified']
        db.create_index('cancer_subject_cancerdiagnosis_audit', ['user_modified'])


        # Changing field 'CancerDiagnosisAudit.lymph_nodes'
        db.alter_column('cancer_subject_cancerdiagnosis_audit', 'lymph_nodes', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'CancerDiagnosisAudit.subject_visit'
        db.alter_column('cancer_subject_cancerdiagnosis_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))

        # Changing field 'CancerDiagnosisAudit.first_evaluation'
        db.alter_column('cancer_subject_cancerdiagnosis_audit', 'first_evaluation', self.gf('django.db.models.fields.DateField')(max_length=25, null=True))

        # Changing field 'CancerDiagnosisAudit.symptom_prompt'
        db.alter_column('cancer_subject_cancerdiagnosis_audit', 'symptom_prompt', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))

        # Changing field 'CancerDiagnosisAudit.lymph_basis'
        db.alter_column('cancer_subject_cancerdiagnosis_audit', 'lymph_basis', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'CancerDiagnosisAudit.symptom_first_noticed'
        db.alter_column('cancer_subject_cancerdiagnosis_audit', 'symptom_first_noticed', self.gf('django.db.models.fields.DateField')(max_length=25, null=True))

        # Changing field 'CancerDiagnosisAudit.diagnosis_word'
        db.alter_column('cancer_subject_cancerdiagnosis_audit', 'diagnosis_word', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'CancerDiagnosisAudit.tumour_basis'
        db.alter_column('cancer_subject_cancerdiagnosis_audit', 'tumour_basis', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'CancerDiagnosisAudit.diagnosis_basis'
        db.alter_column('cancer_subject_cancerdiagnosis_audit', 'diagnosis_basis', self.gf('django.db.models.fields.CharField')(max_length=45, null=True))

        # Changing field 'CancerDiagnosisAudit.metastasis_basis'
        db.alter_column('cancer_subject_cancerdiagnosis_audit', 'metastasis_basis', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))

        # Changing field 'CancerDiagnosisAudit.metastasis'
        db.alter_column('cancer_subject_cancerdiagnosis_audit', 'metastasis', self.gf('django.db.models.fields.CharField')(max_length=15, null=True))
        # Adding index on 'LabResultHiv', fields ['user_modified']
        db.create_index('cancer_subject_labresulthiv', ['user_modified'])


        # Changing field 'LabResultHiv.subject_visit'
        db.alter_column('cancer_subject_labresulthiv', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'LabResultHiv', fields ['subject_visit']
        db.create_unique('cancer_subject_labresulthiv', ['subject_visit_id'])

        # Adding index on 'LabResultHiv', fields ['user_created']
        db.create_index('cancer_subject_labresulthiv', ['user_created'])

        # Adding index on 'SubjectOffStudyAudit', fields ['user_modified']
        db.create_index('cancer_subject_subjectoffstudy_audit', ['user_modified'])

        # Adding index on 'SubjectOffStudyAudit', fields ['user_created']
        db.create_index('cancer_subject_subjectoffstudy_audit', ['user_created'])

        # Adding index on 'BaseRiskAssessmentSunAudit', fields ['user_modified']
        db.create_index('cancer_subject_baseriskassessmentsun_audit', ['user_modified'])

        # Adding index on 'BaseRiskAssessmentSunAudit', fields ['user_created']
        db.create_index('cancer_subject_baseriskassessmentsun_audit', ['user_created'])


        # Changing field 'BaseRiskAssessmentSunAudit.subject_visit'
        db.alter_column('cancer_subject_baseriskassessmentsun_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'LabResultTbAudit', fields ['user_modified']
        db.create_index('cancer_subject_labresulttb_audit', ['user_modified'])

        # Adding index on 'LabResultTbAudit', fields ['user_created']
        db.create_index('cancer_subject_labresulttb_audit', ['user_created'])


        # Changing field 'LabResultTbAudit.subject_visit'
        db.alter_column('cancer_subject_labresulttb_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'EnrollmentChecklistAudit', fields ['user_modified']
        db.create_index('cancer_subject_enrollmentchecklist_audit', ['user_modified'])

        # Adding index on 'EnrollmentChecklistAudit', fields ['user_created']
        db.create_index('cancer_subject_enrollmentchecklist_audit', ['user_created'])

        # Adding index on 'BaseRiskAssessmentFuel', fields ['user_modified']
        db.create_index('cancer_subject_baseriskassessmentfuel', ['user_modified'])


        # Changing field 'BaseRiskAssessmentFuel.subject_visit'
        db.alter_column('cancer_subject_baseriskassessmentfuel', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'BaseRiskAssessmentFuel', fields ['subject_visit']
        db.create_unique('cancer_subject_baseriskassessmentfuel', ['subject_visit_id'])

        # Adding index on 'BaseRiskAssessmentFuel', fields ['user_created']
        db.create_index('cancer_subject_baseriskassessmentfuel', ['user_created'])

        # Adding index on 'BaseRiskAssessmentMining', fields ['user_modified']
        db.create_index('cancer_subject_baseriskassessmentmining', ['user_modified'])


        # Changing field 'BaseRiskAssessmentMining.subject_visit'
        db.alter_column('cancer_subject_baseriskassessmentmining', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'BaseRiskAssessmentMining', fields ['subject_visit']
        db.create_unique('cancer_subject_baseriskassessmentmining', ['subject_visit_id'])

        # Adding index on 'BaseRiskAssessmentMining', fields ['user_created']
        db.create_index('cancer_subject_baseriskassessmentmining', ['user_created'])


        # Changing field 'LabResultHeightWeightAudit.weight'
        db.alter_column('cancer_subject_labresultheightweight_audit', 'weight', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=1))
        # Adding index on 'LabResultHeightWeightAudit', fields ['user_modified']
        db.create_index('cancer_subject_labresultheightweight_audit', ['user_modified'])

        # Adding index on 'LabResultHeightWeightAudit', fields ['user_created']
        db.create_index('cancer_subject_labresultheightweight_audit', ['user_created'])


        # Changing field 'LabResultHeightWeightAudit.subject_visit'
        db.alter_column('cancer_subject_labresultheightweight_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))
        # Adding index on 'LabResultChemistry', fields ['user_modified']
        db.create_index('cancer_subject_labresultchemistry', ['user_modified'])

        # Adding index on 'LabResultChemistry', fields ['user_created']
        db.create_index('cancer_subject_labresultchemistry', ['user_created'])


        # Changing field 'LabResultChemistry.subject_visit'
        db.alter_column('cancer_subject_labresultchemistry', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'LabResultChemistry', fields ['subject_visit']
        db.create_unique('cancer_subject_labresultchemistry', ['subject_visit_id'])

        # Adding index on 'LabResultHaematology', fields ['user_modified']
        db.create_index('cancer_subject_labresulthaematology', ['user_modified'])

        # Adding index on 'LabResultHaematology', fields ['user_created']
        db.create_index('cancer_subject_labresulthaematology', ['user_created'])


        # Changing field 'LabResultHaematology.subject_visit'
        db.alter_column('cancer_subject_labresulthaematology', 'subject_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(default='-', to=orm['cancer_subject.SubjectVisit'], unique=True))
        # Adding unique constraint on 'LabResultHaematology', fields ['subject_visit']
        db.create_unique('cancer_subject_labresulthaematology', ['subject_visit_id'])

        # Adding index on 'BaseRiskAssessmentAlcoholAudit', fields ['user_modified']
        db.create_index('cancer_subject_baseriskassessmentalcohol_audit', ['user_modified'])

        # Adding index on 'BaseRiskAssessmentAlcoholAudit', fields ['user_created']
        db.create_index('cancer_subject_baseriskassessmentalcohol_audit', ['user_created'])


        # Changing field 'BaseRiskAssessmentAlcoholAudit.subject_visit'
        db.alter_column('cancer_subject_baseriskassessmentalcohol_audit', 'subject_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(default='-', to=orm['cancer_subject.SubjectVisit']))

    def backwards(self, orm):
        pass

    models = {
        'bhp_adverse.deathcausecategory': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathCauseCategory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'bhp_adverse.deathcauseinfo': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathCauseInfo'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'bhp_adverse.deathreasonhospitalized': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathReasonHospitalized'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'bhp_appointment.appointment': {
            'Meta': {'ordering': "['registered_subject', 'appt_datetime']", 'unique_together': "(('registered_subject', 'visit_definition', 'visit_instance'),)", 'object_name': 'Appointment'},
            'appt_datetime': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'appt_reason': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'appt_status': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '25', 'db_index': 'True'}),
            'appt_type': ('django.db.models.fields.CharField', [], {'default': "'clinic'", 'max_length': '20'}),
            'best_appt_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'contact_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'contact_tel': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dashboard_type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'is_confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'study_site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_variables.StudySite']", 'null': 'True'}),
            'timepoint_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'visit_definition': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['bhp_visit.VisitDefinition']"}),
            'visit_instance': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1', 'null': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        'bhp_content_type_map.contenttypemap': {
            'Meta': {'ordering': "['name']", 'unique_together': "(['app_label', 'model'],)", 'object_name': 'ContentTypeMap', 'db_table': "'bhp_common_contenttypemap'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'bhp_registration.registeredsubject': {
            'Meta': {'ordering': "['subject_identifier']", 'unique_together': "(('identity', 'first_name', 'dob', 'initials', 'registration_identifier'),)", 'object_name': 'RegisteredSubject'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'hiv_status': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'bhp_variables.studysite': {
            'Meta': {'ordering': "['site_code']", 'unique_together': "[('site_code', 'site_name')]", 'object_name': 'StudySite'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'site_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'}),
            'site_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'bhp_visit.membershipform': {
            'Meta': {'object_name': 'MembershipForm'},
            'category': ('django.db.models.fields.CharField', [], {'default': "'subject'", 'max_length': '25', 'null': 'True'}),
            'content_type_map': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'+'", 'unique': 'True', 'to': "orm['bhp_content_type_map.ContentTypeMap']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'bhp_visit.schedulegroup': {
            'Meta': {'ordering': "['group_name']", 'object_name': 'ScheduleGroup'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'group_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'grouping_key': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'membership_form': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_visit.MembershipForm']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'bhp_visit.visitdefinition': {
            'Meta': {'ordering': "['code', 'time_point']", 'object_name': 'VisitDefinition'},
            'base_interval': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'base_interval_unit': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '10'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '6', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'grouping': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_list.infodeterminant': {
            'Meta': {'object_name': 'InfoDeterminant'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'cancer_list.whoillness': {
            'Meta': {'object_name': 'WhoIllness'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'perform_status': ('django.db.models.fields.CharField', [], {'max_length': '205'}),
            'probs_from_work': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'perform_status': ('django.db.models.fields.CharField', [], {'max_length': '205'}),
            'probs_from_work': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_activityandfunctioning'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.baselinehivhistory': {
            'Meta': {'object_name': 'BaselineHIVHistory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'had_who_illnesses': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_cd4': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_hiv_result': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baselinehivhistory'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.baseriskassessment': {
            'Meta': {'object_name': 'BaseRiskAssessment'},
            'age_firstsex': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_alcohol': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_smoked': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_worked_mine': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hepatitis': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'is_albino': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'participant_interviewed': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'tradmedicine': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'tuberculosis': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'year_tb': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'cancer_subject.baseriskassessmentalcohol': {
            'Meta': {'object_name': 'BaseRiskAssessmentAlcohol'},
            'alcohol_weekly': ('django.db.models.fields.IntegerField', [], {}),
            'amount_drinking': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baseriskassessmentalcohol'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'is_albino': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'participant_interviewed': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baseriskassessment'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'tradmedicine': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'tuberculosis': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'year_tb': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'cancer_subject.baseriskassessmentcancer': {
            'Meta': {'object_name': 'BaseRiskAssessmentCancer'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'family_cancer': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'family_cancer_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'family_cancer_type': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'had_previous_cancer': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'previous_cancer': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'previous_cancer_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'previous_cancer': ('django.db.models.fields.CharField', [], {'max_length': '45', 'blank': 'True'}),
            'previous_cancer_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baseriskassessmentcancer'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.baseriskassessmentchemical': {
            'Meta': {'object_name': 'BaseRiskAssessmentChemical'},
            'arsenic_smelting': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'asbestos': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'asbestos_no_protection': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'chemicals': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'chemicals_time': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'total_time_no_protection': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baseriskassessmentchemical'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'total_time_no_protection': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'setting': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'setting20': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'toilet': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'toilet_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'setting': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'setting20': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baseriskassessmentdemo'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'toilet': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'toilet_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.baseriskassessmenteating': {
            'Meta': {'object_name': 'BaseRiskAssessmentEating'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'five_fruit': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'meal_millet': ('django.db.models.fields.IntegerField', [], {}),
            'meal_peanuts': ('django.db.models.fields.IntegerField', [], {}),
            'meal_rice': ('django.db.models.fields.IntegerField', [], {}),
            'meal_sorghum': ('django.db.models.fields.IntegerField', [], {}),
            'meals_weekly': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.baseriskassessmenteatingaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'BaseRiskAssessmentEatingAudit', 'db_table': "'cancer_subject_baseriskassessmenteating_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'five_fruit': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'meal_millet': ('django.db.models.fields.IntegerField', [], {}),
            'meal_peanuts': ('django.db.models.fields.IntegerField', [], {}),
            'meal_rice': ('django.db.models.fields.IntegerField', [], {}),
            'meal_sorghum': ('django.db.models.fields.IntegerField', [], {}),
            'meals_weekly': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baseriskassessmenteating'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.baseriskassessmentfemale': {
            'Meta': {'object_name': 'BaseRiskAssessmentFemale'},
            'age_period': ('django.db.models.fields.IntegerField', [], {}),
            'children': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baseriskassessmentfemale'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baseriskassessmentfuel'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.baseriskassessmentmining': {
            'Meta': {'object_name': 'BaseRiskAssessmentMining'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'last_mine': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'mine_prompt_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'mine_time': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'mine_type': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'mine_underground': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'mine_underground_time': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.baseriskassessmentminingaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'BaseRiskAssessmentMiningAudit', 'db_table': "'cancer_subject_baseriskassessmentmining_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'last_mine': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'mine_prompt_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'mine_time': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'mine_type': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'mine_underground': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'mine_underground_time': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baseriskassessmentmining'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.baseriskassessmentsmoking': {
            'Meta': {'object_name': 'BaseRiskAssessmentSmoking'},
            'cigarette_smoked': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'cigarette_smoking': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'smoke_now': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'when_quit': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'years_smoked': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'smoke_now': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baseriskassessmentsmoking'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'when_quit': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'years_smoked': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'years_smoked_before': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'cancer_subject.baseriskassessmentsun': {
            'Meta': {'object_name': 'BaseRiskAssessmentSun'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hat': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hours_outdoor': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'shade_umbrella': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'sleeved_shirt': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'sunglasses': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.baseriskassessmentsunaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'BaseRiskAssessmentSunAudit', 'db_table': "'cancer_subject_baseriskassessmentsun_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hat': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hours_outdoor': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'shade_umbrella': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'sleeved_shirt': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_baseriskassessmentsun'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'sunglasses': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.bhhcd4': {
            'Meta': {'object_name': 'BHHCd4'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nadir_cd4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2'}),
            'nadir_cd4_drawn_date': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.bhhcd4audit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'BHHCd4Audit', 'db_table': "'cancer_subject_bhhcd4_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nadir_cd4': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2'}),
            'nadir_cd4_drawn_date': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_bhhcd4'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.bhhhivtest': {
            'Meta': {'object_name': 'BHHHivTest'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hiv_drawn_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'hiv_result': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hiv_testdate_est': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'hiv_testdate_est': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_bhhhivtest'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.bhhwhoillness': {
            'Meta': {'object_name': 'BHHWhoIllness'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'who_illness': ('django.db.models.fields.related.ManyToManyField', [], {'max_length': '35', 'to': "orm['cancer_list.WhoIllness']", 'null': 'True', 'symmetrical': 'False'}),
            'who_illness_date': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'who_illness_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'})
        },
        'cancer_subject.bhhwhoillnessaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'BHHWhoIllnessAudit', 'db_table': "'cancer_subject_bhhwhoillness_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_bhhwhoillness'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'who_illness_date': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'who_illness_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'})
        },
        'cancer_subject.cancerdiagnosis': {
            'Meta': {'object_name': 'CancerDiagnosis'},
            'cancer_category': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'cancer_site': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'cancer_stage': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'cancer_stage_modifier': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'clinical_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_diagnosed': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'diagnosis_basis': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'diagnosis_basis_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'diagnosis_word': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'first_evaluation': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'lymph_basis': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'lymph_nodes': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'metastasis': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'metastasis_basis': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'symptom_first_noticed': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'symptom_prompt': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'symptom_prompt_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'trad_evaluation': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'tumour': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'tumour_basis': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.cancerdiagnosisaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'CancerDiagnosisAudit', 'db_table': "'cancer_subject_cancerdiagnosis_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'cancer_category': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'cancer_site': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'cancer_stage': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'cancer_stage_modifier': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'clinical_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_diagnosed': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'diagnosis_basis': ('django.db.models.fields.CharField', [], {'max_length': '45', 'null': 'True', 'blank': 'True'}),
            'diagnosis_basis_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'diagnosis_word': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'first_evaluation': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'lymph_basis': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'lymph_nodes': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'metastasis': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'metastasis_basis': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_cancerdiagnosis'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'symptom_first_noticed': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'symptom_prompt': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'symptom_prompt_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'trad_evaluation': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'tumour': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'tumour_basis': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.chemomedplan': {
            'Meta': {'object_name': 'ChemoMedPlan'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'cycle_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dose_category': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'drug_code': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'interval': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'oncology_treatment_plan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.OncologyTreatmentPlan']"}),
            'specify_other_med': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.chemomedplanaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'ChemoMedPlanAudit', 'db_table': "'cancer_subject_chemomedplan_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'cycle_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dose_category': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'drug_code': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'interval': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'oncology_treatment_plan': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_chemomedplan'", 'to': "orm['cancer_subject.OncologyTreatmentPlan']"}),
            'specify_other_med': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.chemomedrecord': {
            'Meta': {'object_name': 'ChemoMedRecord'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'cycle_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dose_category': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'drug_code': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'interval': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'otr_chemo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.OTRChemo']"}),
            'specify_other_med': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.chemomedrecordaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'ChemoMedRecordAudit', 'db_table': "'cancer_subject_chemomedrecord_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'cycle_num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dose_category': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'drug_code': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'interval': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'otr_chemo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_chemomedrecord'", 'to': "orm['cancer_subject.OTRChemo']"}),
            'specify_other_med': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.enrollmentchecklist': {
            'Meta': {'object_name': 'EnrollmentChecklist'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'registration_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.enrollmentchecklistaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'EnrollmentChecklistAudit', 'db_table': "'cancer_subject_enrollmentchecklist_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_enrollmentchecklist'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'registration_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.haartmedrecord': {
            'Meta': {'object_name': 'HaartMedRecord'},
            'arv_reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'drug_name': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'haart_record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.HaartRecord']"}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'mod_reason': ('django.db.models.fields.CharField', [], {'max_length': '65', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'stop_date': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'mod_reason': ('django.db.models.fields.CharField', [], {'max_length': '65', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'stop_date': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.haartrecord': {
            'Meta': {'object_name': 'HaartRecord'},
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'haart_status': ('django.db.models.fields.CharField', [], {'max_length': '145', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.haartrecordaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'HaartRecordAudit', 'db_table': "'cancer_subject_haartrecord_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'haart_status': ('django.db.models.fields.CharField', [], {'max_length': '145', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_haartrecord'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'other_abnormal': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'tb_prompt_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'tb_tests': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'other_abnormal': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_labresult'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'tb_prompt_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'tb_tests': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.labresultcd4': {
            'Meta': {'object_name': 'LabResultCd4'},
            'cd4_drawn_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'cd4_result': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_labresultcd4'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.labresultchemistry': {
            'Meta': {'object_name': 'LabResultChemistry'},
            'alanine': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '1', 'blank': 'True'}),
            'aspartate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '1', 'blank': 'True'}),
            'bilirubin': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'chem_drawn_date': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'creatinine': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '1', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'lactate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '1', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.labresultchemistryaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'LabResultChemistryAudit', 'db_table': "'cancer_subject_labresultchemistry_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'alanine': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '1', 'blank': 'True'}),
            'aspartate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '1', 'blank': 'True'}),
            'bilirubin': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'chem_drawn_date': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'creatinine': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '1', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'lactate': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '1', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_labresultchemistry'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.labresulthaematology': {
            'Meta': {'object_name': 'LabResultHaematology'},
            'anc_count': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '3', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'haem_drawn_date': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hgb': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'mcv': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'platelet': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'wbc_count': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'})
        },
        'cancer_subject.labresulthaematologyaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'LabResultHaematologyAudit', 'db_table': "'cancer_subject_labresulthaematology_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'anc_count': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '3', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'haem_drawn_date': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hgb': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'mcv': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'platelet': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '1', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_labresulthaematology'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'wbc_count': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'})
        },
        'cancer_subject.labresultheightweight': {
            'Meta': {'object_name': 'LabResultHeightWeight'},
            'cough2weeks': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'height': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_labresultheightweight'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'})
        },
        'cancer_subject.labresulthiv': {
            'Meta': {'object_name': 'LabResultHiv'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'test_date': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'test_result': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.labresulthivaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'LabResultHivAudit', 'db_table': "'cancer_subject_labresulthiv_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_labresulthiv'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'test_date': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'test_result': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.labresulttb': {
            'Meta': {'object_name': 'LabResultTb'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'tb_description': ('django.db.models.fields.CharField', [], {'max_length': '65'}),
            'tb_treatment': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tb_treatment_start': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.labresulttbaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'LabResultTbAudit', 'db_table': "'cancer_subject_labresulttb_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_labresulttb'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'tb_description': ('django.db.models.fields.CharField', [], {'max_length': '65'}),
            'tb_treatment': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tb_treatment_start': ('django.db.models.fields.DateField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.labresultviralload': {
            'Meta': {'object_name': 'LabResultViralload'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_labresultviralload'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'vl_drawn_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'vl_result': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'cancer_subject.locator': {
            'Meta': {'object_name': 'Locator'},
            'alt_contact_cell': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'alt_contact_cell_number': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'alt_contact_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'alt_contact_rel': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'alt_contact_tel': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'contact_cell': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'contact_physical_address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'contact_rel': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_signed': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'has_alt_contact': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'home_visit_permission': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'mail_address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'may_call_work': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'may_contact_someone': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'may_follow_up': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'other_alt_contact_cell': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'physical_address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True', 'null': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_cell': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_cell_alt': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_phone': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_phone_alt': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cancer_subject.SubjectVisit']"}),
            'subject_work_phone': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_work_place': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.locatoraudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'LocatorAudit', 'db_table': "'cancer_subject_locator_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'alt_contact_cell': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'alt_contact_cell_number': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'alt_contact_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'alt_contact_rel': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'alt_contact_tel': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'contact_cell': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'contact_physical_address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'contact_rel': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_signed': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'has_alt_contact': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'home_visit_permission': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'mail_address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'may_call_work': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'may_contact_someone': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'may_follow_up': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'other_alt_contact_cell': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'physical_address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_locator'", 'null': 'True', 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_cell': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_cell_alt': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_phone': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_phone_alt': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_locator'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'subject_work_phone': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_work_place': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.oncologytreatmentplan': {
            'Meta': {'object_name': 'OncologyTreatmentPlan'},
            'chemo_intent': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'chemotherapy': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'planned_operation': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'radiation_plan': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'radiation_treatments': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'surgical_plan': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'treatment_plan': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.oncologytreatmentplanaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'OncologyTreatmentPlanAudit', 'db_table': "'cancer_subject_oncologytreatmentplan_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'chemo_intent': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'chemotherapy': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'planned_operation': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'radiation_plan': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'radiation_treatments': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_oncologytreatmentplan'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'surgical_plan': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'treatment_plan': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.oncologytreatmentrecord': {
            'Meta': {'object_name': 'OncologyTreatmentRecord'},
            'chemo_received': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'radiation_received': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'surgical_therapy': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'radiation_received': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_oncologytreatmentrecord'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'surgical_therapy': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.otrchemo': {
            'Meta': {'object_name': 'OTRChemo'},
            'chemo_delays': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'chemo_intent': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'chemo_reduced': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_otrchemo'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'why_delayed': ('django.db.models.fields.CharField', [], {'max_length': '65', 'blank': 'True'}),
            'why_delayed_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'why_reduced': ('django.db.models.fields.CharField', [], {'max_length': '75', 'blank': 'True'}),
            'why_reduced_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'})
        },
        'cancer_subject.otrradiation': {
            'Meta': {'object_name': 'OTRRadiation'},
            'amount_radiation': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'concomitant': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'radiation_details': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.otrradiationaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'OTRRadiationAudit', 'db_table': "'cancer_subject_otrradiation_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'amount_radiation': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'concomitant': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'radiation_details': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_otrradiation'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.otrsurgical': {
            'Meta': {'object_name': 'OTRSurgical'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_operation': ('django.db.models.fields.DateField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'operation_performed': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.otrsurgicalaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'OTRSurgicalAudit', 'db_table': "'cancer_subject_otrsurgical_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_operation': ('django.db.models.fields.DateField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'operation_performed': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_otrsurgical'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.referral': {
            'Meta': {'object_name': 'Referral'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'referral_date': ('django.db.models.fields.DateTimeField', [], {'max_length': '25'}),
            'referrals': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'referral_date': ('django.db.models.fields.DateTimeField', [], {'max_length': '25'}),
            'referrals': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_referral'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'why_referred': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        'cancer_subject.subjectconsent': {
            'Meta': {'object_name': 'SubjectConsent'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'confirm_identity': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'consent_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'consent_version_on_entry': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'consent_version_recent': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'guardian_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'identity': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '78L'}),
            'identity_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'is_dob_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'is_incarcerated': ('django.db.models.fields.CharField', [], {'default': "'No'", 'max_length': '3'}),
            'is_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_verified_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'may_store_samples': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'original_identifier': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'study_site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_variables.StudySite']"}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'subject_type': ('django.db.models.fields.CharField', [], {'default': "'undetermined'", 'max_length': '25', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'consent_version_on_entry': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'consent_version_recent': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'guardian_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'identity': ('django.db.models.fields.CharField', [], {'max_length': '78L'}),
            'identity_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'is_dob_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'is_incarcerated': ('django.db.models.fields.CharField', [], {'default': "'No'", 'max_length': '3'}),
            'is_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_verified_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'may_store_samples': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'original_identifier': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'study_site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_subjectconsent'", 'to': "orm['bhp_variables.StudySite']"}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'subject_type': ('django.db.models.fields.CharField', [], {'default': "'undetermined'", 'max_length': '25', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'death_reason_hospitalized': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_adverse.DeathReasonHospitalized']", 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'participant_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'death_reason_hospitalized': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'_audit_subjectdeath'", 'null': 'True', 'to': "orm['bhp_adverse.DeathReasonHospitalized']"}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'participant_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_subjectdeath'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.subjectoffstudy': {
            'Meta': {'object_name': 'SubjectOffStudy'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'offstudy_date': ('django.db.models.fields.DateField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.subjectoffstudyaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'SubjectOffStudyAudit', 'db_table': "'cancer_subject_subjectoffstudy_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'offstudy_date': ('django.db.models.fields.DateField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_subjectoffstudy'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.subjectvisit': {
            'Meta': {'object_name': 'SubjectVisit'},
            'appointment': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_appointment.Appointment']", 'unique': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'info_source': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_source_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'reason_unscheduled': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'info_source': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_source_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'reason_unscheduled': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.treatmentresponse': {
            'Meta': {'object_name': 'TreatmentResponse'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cancer_subject.SubjectVisit']", 'unique': 'True'}),
            'tx_info_determinant': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cancer_list.InfoDeterminant']", 'max_length': '45', 'symmetrical': 'False'}),
            'tx_response': ('django.db.models.fields.TextField', [], {'max_length': '350'}),
            'tx_response_class': ('django.db.models.fields.CharField', [], {'max_length': '95'}),
            'tx_response_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'cancer_subject.treatmentresponseaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'TreatmentResponseAudit', 'db_table': "'cancer_subject_treatmentresponse_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 19, 0, 0)'}),
            'subject_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_treatmentresponse'", 'to': "orm['cancer_subject.SubjectVisit']"}),
            'tx_response': ('django.db.models.fields.TextField', [], {'max_length': '350'}),
            'tx_response_class': ('django.db.models.fields.CharField', [], {'max_length': '95'}),
            'tx_response_date': ('django.db.models.fields.DateField', [], {'max_length': '25'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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