from edc_pdutils.csv_exporters import CsvCrfTablesExporter

from ..df_preppers import MaternalCrfDfPrepper
from .td_csv_exporter import TdCsvExporter


class CsvMaternalCrfTablesExporter(CsvCrfTablesExporter):
    """
    Example Usage:
        $ ssh -f django@td.bhp.org.bw -L5001:localhost:3306 -N

        >>>
        from tc_export.csv_exporters import CsvMaternalCrfTablesExporter
        tbl_exporter = CsvMaternalCrfTablesExporter(
            app_label='td', exclude_history=True)

    """
    df_prepper_cls = MaternalCrfDfPrepper
    visit_column = 'maternal_visit_id'
    csv_exporter_cls = TdCsvExporter

    def __init__(self, **kwargs):
        rx_mapping = {
            'enc1:::c623fb3d561354d55cf9312c0cf840ebf199adc740115bbca80d7b8963500942': 'A',
            'enc1:::f474f2b3e162ea58b01c89076309deb20d4a6c2779e93651c1fb110bef6e3468': 'B'}
        super().__init__(rx_mapping=rx_mapping, **kwargs)
