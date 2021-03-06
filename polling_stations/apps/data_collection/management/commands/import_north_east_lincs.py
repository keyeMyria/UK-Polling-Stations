from data_collection.management.commands import BaseHalaroseCsvImporter


class Command(BaseHalaroseCsvImporter):
    council_id = "E06000012"
    addresses_name = "local.2018-05-03/Version 2/polling_station_export-2018-04-12.csv"
    stations_name = "local.2018-05-03/Version 2/polling_station_export-2018-04-12.csv"
    elections = ["local.2018-05-03"]
    csv_encoding = "windows-1252"
