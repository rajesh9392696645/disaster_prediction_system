import React, { useEffect, useState } from "react";
import axios from "axios";

const DashboardPage = () => {

    const [metrics, setMetrics] = useState({
        floodAccuracy: 94,
        wildfireAccuracy: 92,
        activeAlerts: 0,
        emergencyCases: 0
    });

    const [loading, setLoading] = useState(true);

    useEffect(() => {

        fetchDashboardData();

    }, []);

    const fetchDashboardData = async () => {

        try {

            const response = await axios.get(
                "http://localhost:5000/api/dashboard"
            );

            setMetrics(response.data);

        }

        catch (error) {

            console.log(
                "Dashboard API Error:",
                error.message
            );

        }

        finally {

            setLoading(false);

        }

    };

    if (loading) {

        return (

            <div style={styles.loading}>
                Loading Dashboard...
            </div>

        );

    }

    return (

        <div style={styles.container}>

            <h1 style={styles.heading}>
                Disaster Prediction Dashboard
            </h1>

            <p style={styles.subtitle}>
                AI + Satellite Monitoring System
            </p>

            <div style={styles.grid}>

                <div style={styles.card}>

                    <h3>Flood Detection Accuracy</h3>

                    <h1 style={styles.metric}>
                        {metrics.floodAccuracy}%
                    </h1>

                </div>

                <div style={styles.card}>

                    <h3>Wildfire Detection Accuracy</h3>

                    <h1 style={styles.metric}>
                        {metrics.wildfireAccuracy}%
                    </h1>

                </div>

                <div style={styles.card}>

                    <h3>Active Alerts</h3>

                    <h1 style={styles.metric}>
                        {metrics.activeAlerts}
                    </h1>

                </div>

                <div style={styles.card}>

                    <h3>Emergency Cases</h3>

                    <h1 style={styles.metric}>
                        {metrics.emergencyCases}
                    </h1>

                </div>

            </div>

            <div style={styles.section}>

                <h2>System Overview</h2>

                <p>
                    This dashboard monitors
                    satellite imagery,
                    IoT environmental data,
                    CNN/LSTM predictions,
                    emergency alerts,
                    and rescue planning.
                </p>

            </div>

            <div style={styles.section}>

                <h2>Disaster Modules</h2>

                <ul>

                    <li>Flood Prediction</li>

                    <li>Wildfire Detection</li>

                    <li>Cyclone Tracking</li>

                    <li>Drought Monitoring</li>

                    <li>Landslide Analysis</li>

                </ul>

            </div>

        </div>

    );

};

const styles = {

    container: {

        padding: "30px",

        background: "#f8fafc",

        minHeight: "100vh"

    },

    heading: {

        color: "#1e3a8a",

        textAlign: "center"

    },

    subtitle: {

        textAlign: "center",

        color: "#64748b",

        marginBottom: "30px"

    },

    grid: {

        display: "grid",

        gridTemplateColumns:
            "repeat(auto-fit,minmax(250px,1fr))",

        gap: "20px"

    },

    card: {

        background: "#ffffff",

        padding: "25px",

        borderRadius: "12px",

        boxShadow:
            "0px 4px 12px rgba(0,0,0,0.15)",

        textAlign: "center"
    },

    metric: {

        color: "#2563eb",

        fontSize: "38px"

    },

    section: {

        marginTop: "40px",

        background: "#ffffff",

        padding: "25px",

        borderRadius: "12px",

        boxShadow:
            "0px 4px 12px rgba(0,0,0,0.12)"
    },

    loading: {

        display: "flex",

        justifyContent: "center",

        alignItems: "center",

        height: "100vh",

        fontSize: "24px"
    }

};

export default DashboardPage;