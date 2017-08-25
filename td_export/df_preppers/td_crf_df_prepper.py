import pandas as pd

from edc_pdutils.df_preppers import CrfDialect


class TdCrfDfPrepper(CrfDialect):

    def prepare_dataframe(self, **kwargs):
        super().prepare_dataframe(**kwargs)
        # preserver time for drawn datetime before to_csv formats
        if 'drawn_datetime' in list(self.dataframe.columns):
            self.dataframe['drawn_datetime'] = (
                self.dataframe['drawn_datetime'].apply(
                    lambda x: x if pd.isnull(x) else x.strftime('%Y-%m-%d %H:%M')))
