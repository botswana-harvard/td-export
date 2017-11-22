from edc_pdutils import CsvCrfTablesExporter

from ..df_handlers import TdCrfDfHandler
from .td_csv_exporter import TdCsvExporter


class CsvLabTablesExporter(CsvCrfTablesExporter):
    """
    Example Usage:
        $ ssh -f django@td.bhp.org.bw -L5001:localhost:3306 -N

        >>>
        from td_export.csv_exporters import CsvInfantCrfTablesExporter
        exporter = CsvInfantCrfTablesExporter()
        exporter.to_csv()
    """
    app_label = 'td_lab'
    df_handler_cls = TdCrfDfHandler
    csv_exporter_cls = TdCsvExporter
    exclude_history_tables = True
    exclude_table_names = [
        'td_maternal_maternalrequisition', 'td_infant_infantrequisition']
