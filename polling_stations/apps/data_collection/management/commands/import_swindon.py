from data_collection.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "E06000030"
    addresses_name = "local.2018-05-03/Version 1/Democracy_Club__03May2018 Swindon.tsv"
    stations_name = "local.2018-05-03/Version 1/Democracy_Club__03May2018 Swindon.tsv"
    elections = ["local.2018-05-03"]
    csv_delimiter = "\t"

    def address_record_to_dict(self, record):
        uprn = record.property_urn.strip().lstrip("0")
        if uprn == "10090045827":
            rec = super().address_record_to_dict(record)
            rec["postcode"] = "SN25 2LR"
            return rec

        return super().address_record_to_dict(record)
