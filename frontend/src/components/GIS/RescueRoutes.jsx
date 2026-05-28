import React from "react";

const RescueRoutes = () => {

    return (

        <div style={styles.card}>

            <h2>

                Rescue Route Optimization

            </h2>

            <ul>

                <li>

                    Route A — 12 KM

                </li>

                <li>

                    Route B — 18 KM

                </li>

                <li>

                    Route C — 21 KM

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
        "0 4px 12px rgba(0,0,0,0.12)"
    }

};

export default RescueRoutes;