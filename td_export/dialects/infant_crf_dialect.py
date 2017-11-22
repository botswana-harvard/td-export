from edc_pdutils import CrfDialect


class InfantCrfDialect(CrfDialect):

    @property
    def select_visit_and_related(self):
        """Returns an SQL statement that joins visit, appt, and registered_subject.

        This is for older EDC versions that use this schema.
        """
        sql = (
            'SELECT R.subject_identifier, R.relative_identifier as maternal_identifier, '
            'R.dob, R.gender, R.subject_type, '
            'V.report_datetime as visit_datetime, A.appt_status, V.study_status, '
            'VDEF.code as visit_code, VDEF.title as visit_title, VDEF.time_point, V.reason, '
            'A.appt_datetime, A.timepoint_datetime, A.best_appt_datetime, '
            'R.registration_status, R.registration_datetime, '
            f'V.survival_status, V.last_alive_date, V.id as {self.obj.visit_column} '
            'from edc_appointment_appointment as A '
            f'LEFT JOIN {self.obj.visit_tbl} as V on A.id=V.appointment_id '
            'LEFT JOIN edc_visit_schedule_visitdefinition as VDEF on A.visit_definition_id=VDEF.id '
            'LEFT JOIN edc_registration_registeredsubject as R on A.registered_subject_id=R.id '
        )
        return sql, None
