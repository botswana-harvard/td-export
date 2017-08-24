from edc_pdutils.csv_exporters import CsvCrfTablesExporter

from ..df_preppers import InfantCrfDfPrepper


class CsvInfantCrfTablesExporter(CsvCrfTablesExporter):
    """
    Example Usage:
        $ ssh -f django@td.bhp.org.bw -L5001:localhost:3306 -N

        >>>
        from edc_pdutils.mysqldb import Credentials
        from tc_export.csv_exporters import CsvInfantCrfTablesExporter
        credentials = Credentials(
            user='<user>', passwd='<password>',
            host='127.0.0.1', port='5001', dbname='bhp085')
        tbl_exporter = CsvInfantCrfTablesExporter(
            app_label='td', credentials=credentials, exclude_history=True)

    """
    df_prepper_cls = InfantCrfDfPrepper
    delimiter = ','
    visit_column = 'infant_visit_id'
    csv_date_format = '%Y-%m-%d'
