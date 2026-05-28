import React from "react";

const HeatMap = () => {

    return (

        <div style={styles.card}>

            <h2>

                Disaster Heat Map

            </h2>

            <p>

                High Risk : RED Zones

            </p>

            <p>

                Medium Risk : ORANGE Zones

            </p>

            <p>

                Low Risk : GREEN Zones

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
        "0 4px 12px rgba(0,0,0,0.12)"

    }

};

export default HeatMap;