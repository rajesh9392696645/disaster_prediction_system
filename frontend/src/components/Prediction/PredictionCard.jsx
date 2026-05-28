import React from "react";

const PredictionCard = ({

    disaster,
    accuracy,
    probability

}) => {

    return (

        <div style={styles.card}>

            <h2>

                {disaster}

            </h2>

            <p>

                Accuracy : {accuracy}%

            </p>

            <p>

                Probability : {probability}%

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

export default PredictionCard;