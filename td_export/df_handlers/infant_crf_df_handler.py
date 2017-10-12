from ..dialects import InfantCrfDialect
from .td_df_handlers import TdCrfDfHandler


class InfantCrfDfHandler(TdCrfDfHandler):

    crf_dialect_cls = InfantCrfDialect

    visit_column = 'infant_visit_id'
    visit_tbl = 'td_infant_infantvisit'

    sort_by = ['subject_identifier', 'visit_datetime']
