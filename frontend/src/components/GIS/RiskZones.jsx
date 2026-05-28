import React from "react";

const RiskZones = () => {

    return (

        <div style={styles.card}>

            <h2>

                Disaster Risk Zones

            </h2>

            <p>

                Hyderabad — HIGH

            </p>

            <p>

                Chennai — MEDIUM

            </p>

            <p>

                Mumbai — LOW

            </p>

        </div>

    );

};

const styles={

    card:{

        background:"#ffffff",

        padding:"20px",

        borderRadius:"12px",

        boxShadow:
        "0px 4px 12px rgba(0,0,0,0.12)"
    }

};

export default RiskZones;