from data_collection.github_importer import BaseGitHubImporter


class Command(BaseGitHubImporter):

    srid = 4326
    districts_srid = 4326
    council_id = "W06000009"
    elections = ["parl.2017-06-08"]
    scraper_name = "wdiv-scrapers/DC-PollingStations-Pembrokeshire"
    geom_type = "geojson"

    def district_record_to_dict(self, record):
        poly = self.extract_geometry(record, self.geom_type, self.get_srid("districts"))
        return {
            "internal_council_id": record["DistrictID"],
            "name": record["DistrictName"],
            "area": poly,
            "polling_station_id": record["StationID"],
        }

    def station_record_to_dict(self, record):
        location = self.extract_geometry(
            record, self.geom_type, self.get_srid("stations")
        )
        return {
            "internal_council_id": record["StationID"],
            "postcode": "",
            "address": record["StationName"],
            "location": location,
        }
