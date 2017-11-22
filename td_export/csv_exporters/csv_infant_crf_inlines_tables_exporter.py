from edc_pdutils import CsvCrfInlineTablesExporter, NonCrfDfHandler

from ..column_handlers import ColumnHandler
from ..constants import SYSTEM_COLUMNS
from ..df_handlers import InfantCrfDfHandler
from ..dialects import InfantCrfDialect
from .td_csv_exporter import TdCsvExporter


class InfantInlineDfHandler(NonCrfDfHandler):

    crf_dialect_cls = InfantCrfDialect
    column_handler_cls = ColumnHandler
    na_value = '.'
    system_columns = SYSTEM_COLUMNS
    visit_column = 'infant_visit_id'
    visit_tbl = 'td_infant_infantvisit'


class CsvInfantCrfInlineTablesExporter(CsvCrfInlineTablesExporter):

    app_label = 'td_infant'
    df_handler_cls = InfantCrfDfHandler
    df_inline_handler_cls = InfantInlineDfHandler
    visit_column = 'infant_visit_id'
    csv_exporter_cls = TdCsvExporter
    exclude_history_tables = True
