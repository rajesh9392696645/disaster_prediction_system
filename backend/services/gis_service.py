# services/gis_service.py

import folium


class GISService:

    @staticmethod
    def generate_disaster_map(
        latitude,
        longitude,
        disaster_name
    ):

        disaster_map = folium.Map(
            location=[latitude, longitude],
            zoom_start=8
        )

        folium.Marker(

            [latitude, longitude],

            popup=disaster_name,

            tooltip="Disaster Location",

            icon=folium.Icon(
                color="red",
                icon="warning-sign"
            )

        ).add_to(disaster_map)

        map_path = "static/maps/disaster_map.html"

        disaster_map.save(map_path)

        return map_path