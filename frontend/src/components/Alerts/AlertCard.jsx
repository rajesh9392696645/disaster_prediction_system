import React from "react";

const AlertCard = ({

    disaster,

    severity,

    location

}) => {

    return (

        <div style={styles.card}>

            <h2>

                {disaster}

            </h2>

            <p>

                Severity:
                {" "}
                {severity}

            </p>

            <p>

                Location:
                {" "}
                {location}

            </p>

        </div>

    );

};

const styles = {

    card:{

        background:"#ffffff",

        padding:"20px",

        borderRadius:"10px",

        boxShadow:
        "0px 4px 14px rgba(0,0,0,0.12)"
    }

};

export default AlertCard;