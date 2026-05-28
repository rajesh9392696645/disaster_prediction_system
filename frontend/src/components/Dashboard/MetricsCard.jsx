import React from "react";

const MetricsCard = ({

    title,

    value,

    color

}) => {

    return (

        <div
            style={{
                background:"#ffffff",
                padding:"20px",
                borderRadius:"12px",
                boxShadow:
                "0 4px 12px rgba(0,0,0,0.15)",
                borderLeft:
                `6px solid ${color}`
            }}
        >

            <h3>

                {title}

            </h3>

            <h1>

                {value}

            </h1>

        </div>

    );

};

export default MetricsCard;