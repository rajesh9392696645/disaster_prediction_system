import React, { useEffect, useState } from "react";
import axios from "axios";

import {
    MapContainer,
    TileLayer,
    Marker,
    Popup,
    Circle
}
from "react-leaflet";

import "leaflet/dist/leaflet.css";

const GISPage = () => {

    const [locations, setLocations] = useState([]);

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        fetchGISData();

    }, []);

    const fetchGISData = async () => {

        try {

            const response = await axios.get(
                "http://localhost:5000/api/gis"
            );

            setLocations(
                response.data
            );

        }

        catch(error){

            console.log(
                "GIS API Error:",
                error.message
            );

        }

        finally{

            setLoading(false);

        }

    };

    return (

        <div style={styles.container}>

            <h1 style={styles.heading}>

                GIS Disaster Mapping

            </h1>

            <p style={styles.subtitle}>

                Satellite Data + Risk Zone Visualization

            </p>

            {

                loading ?

                (

                    <h2>

                        Loading GIS Map...

                    </h2>

                )

                :

                (

                    <MapContainer
                        center={[20.5937,78.9629]}
                        zoom={5}
                        style={styles.map}
                    >

                        <TileLayer
                            attribution='OpenStreetMap'
                            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                        />

                        {

                            locations.map((item,index)=>(

                                <React.Fragment key={index}>

                                    <Marker
                                        position={[
                                            item.latitude,
                                            item.longitude
                                        ]}
                                    >

                                        <Popup>

                                            <h3>

                                                {item.disasterType}

                                            </h3>

                                            <p>

                                                Risk Level:
                                                {" "}
                                                {item.riskLevel}

                                            </p>

                                            <p>

                                                Location:
                                                {" "}
                                                {item.location}

                                            </p>

                                        </Popup>

                                    </Marker>

                                    <Circle
                                        center={[
                                            item.latitude,
                                            item.longitude
                                        ]}
                                        radius={50000}
                                        pathOptions={{
                                            color:"red"
                                        }}
                                    />

                                </React.Fragment>

                            ))

                        }

                    </MapContainer>

                )

            }

            <div style={styles.infoCard}>

                <h2>

                    GIS Monitoring Modules

                </h2>

                <ul>

                    <li>

                        Flood Risk Mapping

                    </li>

                    <li>

                        Wildfire Heat Zones

                    </li>

                    <li>

                        Cyclone Path Tracking

                    </li>

                    <li>

                        Rescue Route Planning

                    </li>

                    <li>

                        Satellite Area Monitoring

                    </li>

                </ul>

            </div>

        </div>

    );

};

const styles = {

    container: {

        padding:"30px",

        minHeight:"100vh",

        background:"#f8fafc"

    },

    heading: {

        textAlign:"center",

        color:"#1e3a8a"

    },

    subtitle: {

        textAlign:"center",

        marginBottom:"25px",

        color:"#64748b"

    },

    map: {

        height:"550px",

        width:"100%",

        borderRadius:"12px"

    },

    infoCard: {

        background:"#ffffff",

        marginTop:"30px",

        padding:"25px",

        borderRadius:"12px",

        boxShadow:
            "0px 4px 12px rgba(0,0,0,0.12)"
    }

};

export default GISPage;