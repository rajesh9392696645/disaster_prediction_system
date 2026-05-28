import React from "react";

const LiveChart = () => {

    return (

        <div
            style={styles.card}
        >

            <h2>

                Live Disaster Trend

            </h2>

            <p>

                Flood ↑

            </p>

            <p>

                Wildfire ↓

            </p>

            <p>

                Cyclone ↑

            </p>

        </div>

    );

};

const styles={

    card:{

        background:"#fff",

        padding:"20px",

        borderRadius:"12px",

        boxShadow:
        "0 4px 12px rgba(0,0,0,0.12)"
    }

};

export default LiveChart;