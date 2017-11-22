from edc_pdutils import CsvCrfInlineTablesExporter, NonCrfDfHandler

from ..column_handlers import ColumnHandler
from ..constants import SYSTEM_COLUMNS
from ..df_handlers import MaternalCrfDfHandler
from .td_csv_exporter import TdCsvExporter
from ..dialects import MaternalCrfDialect


class MaternalInlineDfHandler(NonCrfDfHandler):

    crf_dialect_cls = MaternalCrfDialect
    column_handler_cls = ColumnHandler
    na_value = '.'
    system_columns = SYSTEM_COLUMNS
    visit_column = 'maternal_visit_id'
    visit_tbl = 'td_maternal_maternalvisit'


class CsvMaternalCrfInlineTablesExporter(CsvCrfInlineTablesExporter):

    app_label = 'td_maternal'
    csv_exporter_cls = TdCsvExporter
    df_handler_cls = MaternalCrfDfHandler
    df_inline_handler_cls = MaternalInlineDfHandler
    visit_column = 'maternal_visit_id'
    exclude_history_tables = True
