from edc_pdutils.csv_exporters import CsvCrfTablesExporter

from ..df_handlers import MaternalCrfDfHandler
from .td_csv_exporter import TdCsvExporter


class CsvMaternalCrfTablesExporter(CsvCrfTablesExporter):
    """
    Example Usage:
        $ ssh -f django@td.bhp.org.bw -L5001:localhost:3306 -N

        >>>
        from td_export.csv_exporters import CsvMaternalCrfTablesExporter
        exporter = CsvMaternalCrfTablesExporter()
        exporter.to_csv()

    """
    app_label = 'td_'
    df_handler_cls = MaternalCrfDfHandler
    visit_column = 'maternal_visit_id'
    csv_exporter_cls = TdCsvExporter
    exclude_history_tables = True
