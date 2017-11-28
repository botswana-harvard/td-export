import pandas as pd

from edc_pdutils import CsvTablesExporter, TableToDataframe

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

    def __init__(self, **kwargs):
        self._df_registered_subject = pd.DataFrame()
        super().__init__(**kwargs)

    @property
    def df_registered_subject(self):
        if self._df_registered_subject.empty:
            columns = ['subject_identifier', 'relative_identifier', 'study_site',
                       'dob', 'gender', 'screening_identifier', 'screening_datetime',
                       'screening_age_in_years', 'registration_datetime', 'id']
            obj = TableToDataframe(
                table_name='edc_registration_registeredsubject',
                columns=columns)
            self._df_registered_subject = obj.dataframe.rename(
                columns={'id': 'registered_subject_id'})
        return self._df_registered_subject

    def to_df(self, table_name=None, **kwargs):
        """Returns a dataframe after passing the raw df
        through the df_handler class.
        """
        df = self.get_raw_df(table_name)
        rs_columns = list(self.df_registered_subject.columns)
        df_columns = list(df)
        columns = [
            col for col in rs_columns if col not in df_columns] + df_columns
        columns = [col for col in columns if not col.startswith('exported')]
        df = pd.merge(df, self.df_registered_subject,
                      on='registered_subject_id', how='left', suffixes=['', '_merged'])
        df = df.loc[:, columns]
        if self.df_handler_cls:
            df_handler = self.df_handler_cls(
                dataframe=df, db=self.db,
                table_name=table_name, **kwargs)
            df = df_handler.dataframe
        return df
