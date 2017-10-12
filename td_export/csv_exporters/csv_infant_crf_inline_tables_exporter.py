from edc_pdutils.csv_exporters import CsvCrfInlineTablesExporter

from ..df_handlers import InfantCrfDfHandler, TdNonCrfDfHandler
from .td_csv_exporter import TdCsvExporter


class CsvInfantCrfInlineTablesExporter(CsvCrfInlineTablesExporter):

    df_handler_cls = InfantCrfDfHandler
    df_inline_handler_cls = TdNonCrfDfHandler
    visit_column = 'infant_visit_id'
    csv_exporter_cls = TdCsvExporter
