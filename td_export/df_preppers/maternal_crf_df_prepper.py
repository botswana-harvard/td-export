from edc_pdutils.df_preppers import CrfDfPrepper
from edc_pdutils.df_formatter import DfFormatter


class Dialect:

    def select_visit_and_related(self, visit_tbl=None, visit_column=None, enrollment_tbl=None, hiv_status_tbl=None):
        """Returns an SQL statement that joins visit, appt, and registered_subject.

        This is for older EDC versions that use this schema.
        """
        return (
            'SELECT R.subject_identifier, R.screening_identifier, R.dob, R.gender, R.subject_type, R.sid, '
            'ENROLL.enrollment_hiv_status, '
            'V.report_datetime as visit_datetime, A.appt_status, V.study_status, '
            'VDEF.code as visit_code, VDEF.title as visit_title, VDEF.time_point, V.reason, '
            'A.appt_datetime, A.timepoint_datetime, A.best_appt_datetime, '
            'R.screening_age_in_years, R.registration_status, R.registration_datetime, '
            'R.randomization_datetime, V.survival_status, V.last_alive_date, '
            'IF(HIV.rapid_test_done is NULL, "No", HIV.rapid_test_done) as rapid_test_done, '
            'HIV.result_date as rapid_test_date, HIV.result as rapid_test_result, '
            f'V.id as {visit_column} '
            'from edc_appointment_appointment as A '
            f'LEFT JOIN {visit_tbl} as V on A.id=V.appointment_id '
            f'LEFT JOIN {hiv_status_tbl} as HIV on V.id=HIV.{visit_column} '
            'LEFT JOIN edc_visit_schedule_visitdefinition as VDEF on A.visit_definition_id=VDEF.id '
            'LEFT JOIN edc_registration_registeredsubject as R on A.registered_subject_id=R.id '
            f'LEFT JOIN {enrollment_tbl} as ENROLL on ENROLL.registered_subject_id=R.id'
        )


class MaternalCrfDfPrepper(CrfDfPrepper):

    dialect_cls = Dialect
    df_formatter_cls = DfFormatter
    visit_column = 'maternal_visit_id'
    visit_tbl = 'td_maternal_maternalvisit'

    enrollment_tbl = 'td_maternal_antenatalenrollment'
    hiv_status_tbl = 'td_maternal_rapidtestresult'
    sort_by = ['subject_identifier', 'visit_datetime']

    @property
    def sql_select_visit_and_related(self):
        return self.dialect.select_visit_and_related(
            self.visit_tbl, self.visit_column,
            self.enrollment_tbl, self.hiv_status_tbl)
