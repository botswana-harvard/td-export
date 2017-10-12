from ..dialects import MaternalCrfDialect
from .td_df_handlers import TdCrfDfHandler


class MaternalCrfDfHandler(TdCrfDfHandler):

    crf_dialect_cls = MaternalCrfDialect
    visit_column = 'maternal_visit_id'

    visit_tbl = 'td_maternal_maternalvisit'
    enrollment_tbl = 'td_maternal_antenatalenrollment'
    hiv_status_tbl = 'td_maternal_rapidtestresult'
    rando_tbl = 'td_maternal_maternalrando'

    sort_by = ['subject_identifier', 'visit_datetime']
