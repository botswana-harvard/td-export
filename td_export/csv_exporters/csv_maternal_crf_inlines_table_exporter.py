from edc_pdutils.csv_exporters import CsvCrfInlineTablesExporter

from ..df_handlers import MaternalCrfDfHandler, TdCrfDfHandler
from .td_csv_exporter import TdCsvExporter


class CsvMaternalCrfInlineTablesExporter(CsvCrfInlineTablesExporter):

    df_handler_cls = MaternalCrfDfHandler
    df_inline_handler_cls = TdCrfDfHandler
    visit_column = 'maternal_visit_id'
    csv_exporter_cls = TdCsvExporter
