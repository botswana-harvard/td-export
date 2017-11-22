from edc_pdutils import CsvTablesExporter

from ..df_handlers import TdNonCrfDfHandler
from .td_csv_exporter import TdCsvExporter


class CsvNonCrfTablesExporter(CsvTablesExporter):
    """
    Example Usage:
        $ ssh -f django@td.bhp.org.bw -L5001:localhost:3306 -N

        >>>
        from td_export.csv_exporters import CsvCrfTablesExporter
        exporter = TdCsvNonCrfTablesExporter()
        exporter.to_csv()

    """
    app_label = 'td'
    df_handler_cls = TdNonCrfDfHandler
    csv_exporter_cls = TdCsvExporter
