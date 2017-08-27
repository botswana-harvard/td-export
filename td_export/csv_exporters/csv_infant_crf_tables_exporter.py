from edc_pdutils.csv_exporters import CsvCrfTablesExporter

from ..df_preppers import InfantCrfDfPrepper
from .td_csv_exporter import TdCsvExporter


class CsvInfantCrfTablesExporter(CsvCrfTablesExporter):
    """
    Example Usage:
        $ ssh -f django@td.bhp.org.bw -L5001:localhost:3306 -N

        >>>
        from tc_export.csv_exporters import CsvInfantCrfTablesExporter
        tbl_exporter = CsvInfantCrfTablesExporter(
            app_label='td', exclude_history=True)

    """
    df_prepper_cls = InfantCrfDfPrepper
    visit_column = 'infant_visit_id'
    csv_exporter_cls = TdCsvExporter
