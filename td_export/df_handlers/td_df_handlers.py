from edc_pdutils import CrfDfHandler, NonCrfDfHandler

from ..column_handlers import ColumnHandler
from ..constants import SYSTEM_COLUMNS


class TdCrfDfHandler(CrfDfHandler):

    system_columns = SYSTEM_COLUMNS
    column_handler_cls = ColumnHandler
    na_value = '.'


class TdNonCrfDfHandler(NonCrfDfHandler):

    system_columns = SYSTEM_COLUMNS
    column_handler_cls = ColumnHandler
    na_value = '.'
