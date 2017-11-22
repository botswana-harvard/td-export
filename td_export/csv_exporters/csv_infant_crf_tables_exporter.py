from edc_pdutils import CsvCrfTablesExporter

from ..df_handlers import InfantCrfDfHandler
from .td_csv_exporter import TdCsvExporter


class CsvInfantCrfTablesExporter(CsvCrfTablesExporter):
    """
    Example Usage:
        $ ssh -f django@td.bhp.org.bw -L5001:localhost:3306 -N

        >>>
        from td_export.csv_exporters import CsvInfantCrfTablesExporter
        exporter = CsvInfantCrfTablesExporter()
        exporter.to_csv()
    """
    app_label = 'td_'
    df_handler_cls = InfantCrfDfHandler
    visit_column = 'infant_visit_id'
    csv_exporter_cls = TdCsvExporter
    exclude_history_tables = True
