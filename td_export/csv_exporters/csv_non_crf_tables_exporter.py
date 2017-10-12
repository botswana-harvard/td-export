from edc_pdutils.csv_exporters import CsvNonCrfTablesExporter

from ..df_handlers import TdNonCrfDfHandler
from .td_csv_exporter import TdCsvExporter


class CsvNonCrfTablesExporter(CsvNonCrfTablesExporter):
    """
    Example Usage:
        $ ssh -f django@td.bhp.org.bw -L5001:localhost:3306 -N

        >>>
        from edc_pdutils.csv_exporters.tshilo_dikgotla import CsvCrfTablesExporter
        exporter = TdCsvNonCrfTablesExporter()
        exporter.to_csv()

    """
    app_label = 'td'
    df_handler_cls = TdNonCrfDfHandler
    csv_exporter_cls = TdCsvExporter
