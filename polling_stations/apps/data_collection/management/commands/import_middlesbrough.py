from data_collection.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "E06000002"
    addresses_name = (
        "parl.2017-06-08/Version 1/Middlesbrough Democracy_Club__08June2017.tsv"
    )
    stations_name = (
        "parl.2017-06-08/Version 1/Middlesbrough Democracy_Club__08June2017.tsv"
    )
    elections = ["parl.2017-06-08"]
    csv_delimiter = "\t"
