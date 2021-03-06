from data_collection.management.commands import BaseXpressDemocracyClubCsvImporter


class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = "E08000008"
    addresses_name = "local.2018-05-03/Version 1/Democracy_Club__03May2018.tsv"
    stations_name = "local.2018-05-03/Version 1/Democracy_Club__03May2018.tsv"
    elections = ["local.2018-05-03"]
    csv_delimiter = "\t"

    def address_record_to_dict(self, record):
        uprn = record.property_urn.strip().lstrip("0")

        if record.addressline6 == "OL5 0EX":
            return None

        if uprn == "200002851978":
            rec = super().address_record_to_dict(record)
            rec["postcode"] = "M43 7RZ"
            return rec

        if record.addressline6 == "SK14 1EY":
            return None

        return super().address_record_to_dict(record)
