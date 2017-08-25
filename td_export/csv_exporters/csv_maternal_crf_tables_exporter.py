from edc_pdutils.csv_exporters import CsvCrfTablesExporter

from ..df_preppers import MaternalCrfDfPrepper


class CsvMaternalCrfTablesExporter(CsvCrfTablesExporter):
    """
    Example Usage:
        $ ssh -f django@td.bhp.org.bw -L5001:localhost:3306 -N

        >>>
        from edc_pdutils.mysqldb import Credentials
        from tc_export.csv_exporters import CsvMaternalCrfTablesExporter
        credentials = Credentials(
            user='<user>', passwd='<password>',
            host='127.0.0.1', port='5001', dbname='bhp085')
        tbl_exporter = CsvMaternalCrfTablesExporter(
            app_label='td', credentials=credentials, exclude_history=True)

    """
    df_prepper_cls = MaternalCrfDfPrepper
    delimiter = ','
    visit_column = 'maternal_visit_id'
    csv_date_format = '%Y-%m-%d'

    def __init__(self, **kwargs):
        rx_mapping = {
            'enc1:::c623fb3d561354d55cf9312c0cf840ebf199adc740115bbca80d7b8963500942': 'A',
            'enc1:::f474f2b3e162ea58b01c89076309deb20d4a6c2779e93651c1fb110bef6e3468': 'B'}
        super().__init__(rx_mapping=rx_mapping, **kwargs)
