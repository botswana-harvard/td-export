from edc_pdutils.csv_exporters import CsvCrfTablesExporter as Base
from edc_pdutils.df_preppers import DfPrepper as DefaultPrepper


class CsvCrfTablesExporter(Base):
    """
    Example Usage:
        $ ssh -f django@td.bhp.org.bw -L5001:localhost:3306 -N

        >>>
        from edc_pdutils.mysqldb import Credentials
        from edc_pdutils.csv_exporters.tshilo_dikgotla import CsvCrfTablesExporter
        credentials = Credentials(
            user='<user>', passwd='<password>',
            host='127.0.0.1', port='5001', dbname='bhp085')
        tbl_exporter = CsvNonCrfTablesExporter(
            app_label='td', credentials=credentials, exclude_history=True)

    """
    df_prepper_cls = DefaultPrepper
    visit_column = 'maternal_visit_id'
    delimiter = ','
