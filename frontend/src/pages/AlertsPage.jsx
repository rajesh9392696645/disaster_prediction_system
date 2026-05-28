import React, { useEffect, useState } from "react";
import axios from "axios";

const AlertsPage = () => {

    const [alerts,setAlerts] = useState([]);

    const [loading,setLoading] = useState(true);

    useEffect(() => {

        fetchAlerts();

    },[]);

    const fetchAlerts = async () => {

        try{

            const response = await axios.get(
                "http://localhost:5000/api/alerts"
            );

            setAlerts(
                response.data
            );

        }

        catch(error){

            console.log(
                "Alert API Error:",
                error.message
            );

        }

        finally{

            setLoading(false);

        }

    };

    return(

        <div style={styles.container}>

            <h1 style={styles.heading}>

                Emergency Alert Center

            </h1>

            <p style={styles.subtitle}>

                AI Generated Disaster Alerts &
                Emergency Notifications

            </p>

            {

                loading ?

                (

                    <h2>

                        Loading Alerts...

                    </h2>

                )

                :

                (

                    <div style={styles.grid}>

                        {

                            alerts.map((alert,index)=>(

                                <div
                                    key={index}
                                    style={styles.card}
                                >

                                    <h2>

                                        {alert.disasterType}

                                    </h2>

                                    <p>

                                        <strong>
                                            Location:
                                        </strong>

                                        {" "}

                                        {alert.location}

                                    </p>

                                    <p>

                                        <strong>
                                            Severity:
                                        </strong>

                                        {" "}

                                        {alert.severity}

                                    </p>

                                    <p>

                                        <strong>
                                            Alert Time:
                                        </strong>

                                        {" "}

                                        {alert.time}

                                    </p>

                                    <p>

                                        <strong>
                                            Status:
                                        </strong>

                                        {" "}

                                        {alert.status}

                                    </p>

                                    <button
                                        style={styles.button}
                                    >

                                        View Details

                                    </button>

                                </div>

                            ))

                        }

                    </div>

                )

            }

            <div style={styles.infoBox}>

                <h2>

                    Emergency Response Modules

                </h2>

                <ul>

                    <li>
                        SMS Notifications
                    </li>

                    <li>
                        Email Alerts
                    </li>

                    <li>
                        Push Notifications
                    </li>

                    <li>
                        Evacuation Guidance
                    </li>

                    <li>
                        Rescue Route Optimization
                    </li>

                    <li>
                        Cloud Alert Distribution
                    </li>

                </ul>

            </div>

        </div>

    );

};

const styles = {

    container: {

        minHeight:"100vh",

        background:"#f1f5f9",

        padding:"30px"

    },

    heading: {

        textAlign:"center",

        color:"#1e3a8a"

    },

    subtitle: {

        textAlign:"center",

        marginBottom:"35px",

        color:"#64748b"

    },

    grid: {

        display:"grid",

        gridTemplateColumns:
            "repeat(auto-fit,minmax(300px,1fr))",

        gap:"25px"

    },

    card: {

        background:"#ffffff",

        padding:"25px",

        borderRadius:"12px",

        boxShadow:
            "0px 4px 14px rgba(0,0,0,0.12)"

    },

    button: {

        marginTop:"15px",

        width:"100%",

        padding:"12px",

        border:"none",

        borderRadius:"8px",

        background:"#dc2626",

        color:"#ffffff",

        cursor:"pointer",

        fontWeight:"bold"

    },

    infoBox: {

        marginTop:"35px",

        background:"#ffffff",

        padding:"25px",

        borderRadius:"12px",

        boxShadow:
            "0px 4px 14px rgba(0,0,0,0.12)"

    }

};

export default AlertsPage;