from edc_pdutils import CsvExporter


class TdCsvExporter(CsvExporter):
    delimiter = ','
    date_format = '%Y-%m-%d'
