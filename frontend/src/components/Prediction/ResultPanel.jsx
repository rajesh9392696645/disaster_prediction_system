import React from "react";

const ResultPanel = () => {

    return (

        <div style={styles.card}>

            <h2>

                Prediction Results

            </h2>

            <p>

                Disaster :
                Flood Risk

            </p>

            <p>

                Confidence :
                94%

            </p>

            <p>

                Response Time :
                2 Seconds

            </p>

            <p>

                Status :
                High Alert

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

export default ResultPanel;