from .infant_crf_dialect import InfantCrfDialect
from .td_crf_df_prepper import TdCrfDfPrepper


class InfantCrfDfPrepper(TdCrfDfPrepper):

    crf_dialect_cls = InfantCrfDialect
    visit_column = 'infant_visit_id'
    visit_tbl = 'td_infant_infantvisit'
    sort_by = ['subject_identifier', 'visit_datetime']
