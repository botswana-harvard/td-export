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
