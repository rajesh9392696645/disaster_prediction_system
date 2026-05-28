import React from "react";

import {

    MapContainer,
    TileLayer,
    Marker,
    Popup

}

from "react-leaflet";

import "leaflet/dist/leaflet.css";

const LeafletMap = () => {

    return (

        <MapContainer

            center={[17.3850,78.4867]}

            zoom={6}

            style={{
                height:"500px",
                width:"100%"
            }}

        >

            <TileLayer

                attribution=
                "&copy; OpenStreetMap"

                url=
                "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"

            />

            <Marker

                position={[17.3850,78.4867]}

            >

                <Popup>

                    Disaster Location

                </Popup>

            </Marker>

        </MapContainer>

    );

};

export default LeafletMap;