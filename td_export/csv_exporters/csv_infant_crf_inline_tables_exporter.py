from edc_pdutils.csv_exporters import CsvCrfInlineTablesExporter

from ..df_preppers import InfantCrfDfPrepper
from .td_csv_exporter import TdCsvExporter


class CsvInfantCrfInlineTablesExporter(CsvCrfInlineTablesExporter):

    df_prepper_cls = InfantCrfDfPrepper
    visit_column = 'infant_visit_id'
    csv_exporter_cls = TdCsvExporter
