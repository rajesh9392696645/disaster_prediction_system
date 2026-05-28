import React from "react";

const DisasterStats = () => {

    return (

        <div style={styles.card}>

            <h2>

                Disaster Statistics

            </h2>

            <p>

                Active Alerts: 18

            </p>

            <p>

                High Risk Zones: 7

            </p>

            <p>

                Emergency Responses: 26

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
        "0 4px 12px rgba(0,0,0,0.15)"
    }

};

export default DisasterStats;