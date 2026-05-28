import React from "react";

const StatCard = ({

    title,

    value,

    icon

}) => {

    return (

        <div
            style={{
                background:"#ffffff",
                padding:"25px",
                borderRadius:"14px",
                boxShadow:
                "0px 4px 14px rgba(0,0,0,0.15)"
            }}
        >

            <h2>

                {icon}

            </h2>

            <h3>

                {title}

            </h3>

            <h1>

                {value}

            </h1>

        </div>

    );

};

export default StatCard;