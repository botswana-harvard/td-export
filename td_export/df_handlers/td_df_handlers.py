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

    @property
    def columns(self):
        """Returns a list of column names.
        """
        columns = list(self.dataframe.columns)
        # "export_" columns
        if self.exclude_export_columns:
            columns = [col for col in columns if not col.startswith('export_')]
        ex_columns = ['form_as_json', 'initials', 'first_name']
        columns = [col for col in columns if col not in ex_columns]

        # "system" columns, move to the end
        if not self.exclude_system_columns:
            columns = [
                col for col in columns if col not in self.system_columns]
            columns.extend(self.system_columns)
        return columns