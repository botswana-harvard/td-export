from edc_pdutils.csv_exporters import CsvNonCrfTablesExporter
from edc_pdutils.df_preppers import DfPrepper as DefaultPrepper

from .td_csv_exporter import TdCsvExporter


class CsvNonCrfTablesExporter(CsvNonCrfTablesExporter):
    """
    Example Usage:
        $ ssh -f django@td.bhp.org.bw -L5001:localhost:3306 -N

        >>>
        from edc_pdutils.csv_exporters.tshilo_dikgotla import CsvCrfTablesExporter
        tbl_exporter = TdCsvNonCrfTablesExporter(app_label='td', exclude_history=True)

    """
    df_prepper_cls = DefaultPrepper
    csv_exporter_cls = TdCsvExporter
