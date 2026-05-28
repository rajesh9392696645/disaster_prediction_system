import React from "react";

const PredictionSummary = () => {

    return (

        <div style={styles.card}>

            <h2>

                Prediction Summary

            </h2>

            <ul>

                <li>

                    Flood Accuracy : 94%

                </li>

                <li>

                    Wildfire Accuracy : 92%

                </li>

                <li>

                    Cyclone Accuracy : 90%

                </li>

            </ul>

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

export default PredictionSummary;