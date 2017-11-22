from edc_pdutils import CrfDialect


class MaternalCrfDialect(CrfDialect):

    @property
    def select_visit_and_related(self):
        """Returns an SQL statement that joins visit, appt, and registered_subject.

        This is for older EDC versions that use this schema.
        """
        sql = (
            'SELECT R.subject_identifier, R.screening_identifier, R.dob, R.gender, R.subject_type, '
            'RANDO.rx, '
            'ENROLL.enrollment_hiv_status, '
            'V.report_datetime as visit_datetime, A.appt_status, V.study_status, '
            'VDEF.code as visit_code, VDEF.title as visit_title, VDEF.time_point, V.reason, '
            'A.appt_datetime, A.timepoint_datetime, A.best_appt_datetime, '
            'R.screening_age_in_years, R.registration_status, R.registration_datetime, '
            'R.randomization_datetime, V.survival_status, V.last_alive_date, '
            'IF(HIV.rapid_test_done is NULL, "No", HIV.rapid_test_done) as rapid_test_done, '
            'HIV.result_date as rapid_test_date, HIV.result as rapid_test_result, '
            f'V.id as {self.obj.visit_column} '
            'from edc_appointment_appointment as A '
            f'LEFT JOIN {self.obj.visit_tbl} as V on A.id=V.appointment_id '
            f'LEFT JOIN {self.obj.hiv_status_tbl} as HIV on V.id=HIV.{self.obj.visit_column} '
            'LEFT JOIN edc_visit_schedule_visitdefinition as VDEF on A.visit_definition_id=VDEF.id '
            'LEFT JOIN edc_registration_registeredsubject as R on A.registered_subject_id=R.id '
            f'LEFT JOIN {self.obj.enrollment_tbl} as ENROLL on ENROLL.registered_subject_id=R.id '
            f'LEFT JOIN {self.obj.rando_tbl} as RANDO on R.sid=RANDO.sid '
        )
        return sql, None
