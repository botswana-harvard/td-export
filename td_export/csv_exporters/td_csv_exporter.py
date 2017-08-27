from edc_pdutils.csv_exporters import CsvExporter


class TdCsvExporter(CsvExporter):
    delimiter = ','
    csv_date_format = '%Y-%m-%d'
