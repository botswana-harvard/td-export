from .maternal_crf_dialect import MaternalCrfDialect
from .td_crf_df_prepper import TdCrfDfPrepper


class MaternalCrfDfPrepper(TdCrfDfPrepper):

    crf_dialect_cls = MaternalCrfDialect
    visit_column = 'maternal_visit_id'

    visit_tbl = 'td_maternal_maternalvisit'
    enrollment_tbl = 'td_maternal_antenatalenrollment'
    hiv_status_tbl = 'td_maternal_rapidtestresult'
    rando_tbl = 'td_maternal_maternalrando'

    sort_by = ['subject_identifier', 'visit_datetime']

    def __init__(self, rx_mapping=None, **kwargs):
        self.rx_mapping = rx_mapping
        super().__init__(**kwargs)

    def prepare_dataframe(self, **kwargs):
        super().prepare_dataframe(**kwargs)
        # remap RX field
        self.dataframe['rx'] = self.dataframe['rx'].map(self.rx_mapping.get)
