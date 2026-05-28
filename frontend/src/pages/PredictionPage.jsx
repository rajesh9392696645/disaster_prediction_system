import React, { useState } from "react";
import axios from "axios";

const PredictionPage = () => {

    const [formData, setFormData] = useState({
        disasterType: "",
        temperature: "",
        humidity: "",
        rainfall: ""
    });

    const [prediction, setPrediction] = useState(null);

    const [loading, setLoading] = useState(false);

    const handleChange = (e) => {

        setFormData({

            ...formData,

            [e.target.name]: e.target.value

        });

    };

    const handlePrediction = async (e) => {

        e.preventDefault();

        setLoading(true);

        try {

            const response = await axios.post(

                "http://localhost:5000/api/predict",

                formData

            );

            setPrediction(response.data);

        }

        catch (error) {

            console.log(

                "Prediction Error:",

                error.message

            );

        }

        finally {

            setLoading(false);

        }

    };

    return (

        <div style={styles.container}>

            <h1 style={styles.heading}>

                Disaster Prediction Module

            </h1>

            <p style={styles.subtitle}>

                CNN + LSTM + Satellite Data Analysis

            </p>

            <div style={styles.card}>

                <form onSubmit={handlePrediction}>

                    <div style={styles.formGroup}>

                        <label>

                            Disaster Type

                        </label>

                        <select
                            name="disasterType"
                            value={formData.disasterType}
                            onChange={handleChange}
                            required
                            style={styles.input}
                        >

                            <option value="">

                                Select

                            </option>

                            <option value="Flood">

                                Flood

                            </option>

                            <option value="Wildfire">

                                Wildfire

                            </option>

                            <option value="Cyclone">

                                Cyclone

                            </option>

                            <option value="Landslide">

                                Landslide

                            </option>

                        </select>

                    </div>

                    <div style={styles.formGroup}>

                        <label>

                            Temperature (°C)

                        </label>

                        <input
                            type="number"
                            name="temperature"
                            value={formData.temperature}
                            onChange={handleChange}
                            required
                            style={styles.input}
                        />

                    </div>

                    <div style={styles.formGroup}>

                        <label>

                            Humidity (%)

                        </label>

                        <input
                            type="number"
                            name="humidity"
                            value={formData.humidity}
                            onChange={handleChange}
                            required
                            style={styles.input}
                        />

                    </div>

                    <div style={styles.formGroup}>

                        <label>

                            Rainfall (mm)

                        </label>

                        <input
                            type="number"
                            name="rainfall"
                            value={formData.rainfall}
                            onChange={handleChange}
                            required
                            style={styles.input}
                        />

                    </div>

                    <button
                        type="submit"
                        style={styles.button}
                    >

                        {

                            loading

                            ?

                            "Running AI Model..."

                            :

                            "Predict"

                        }

                    </button>

                </form>

            </div>

            {

                prediction && (

                    <div style={styles.resultCard}>

                        <h2>

                            Prediction Results

                        </h2>

                        <p>

                            <strong>

                                Predicted Risk:

                            </strong>

                            {" "}

                            {prediction.predictedRisk}

                        </p>

                        <p>

                            <strong>

                                Probability:

                            </strong>

                            {" "}

                            {prediction.probability}%

                        </p>

                        <p>

                            <strong>

                                CNN Accuracy:

                            </strong>

                            {" "}

                            {prediction.cnnAccuracy}%

                        </p>

                        <p>

                            <strong>

                                LSTM Accuracy:

                            </strong>

                            {" "}

                            {prediction.lstmAccuracy}%

                        </p>

                    </div>

                )

            }

        </div>

    );

};

const styles = {

    container: {

        minHeight: "100vh",

        background: "#f1f5f9",

        padding: "40px"

    },

    heading: {

        textAlign: "center",

        color: "#1e3a8a"

    },

    subtitle: {

        textAlign: "center",

        marginBottom: "30px",

        color: "#64748b"

    },

    card: {

        background: "#ffffff",

        padding: "30px",

        borderRadius: "12px",

        maxWidth: "650px",

        margin: "auto",

        boxShadow:
            "0px 4px 15px rgba(0,0,0,0.12)"
    },

    formGroup: {

        marginBottom: "18px"

    },

    input: {

        width: "100%",

        padding: "12px",

        marginTop: "8px",

        borderRadius: "8px",

        border: "1px solid #cbd5e1"

    },

    button: {

        width: "100%",

        padding: "14px",

        background: "#2563eb",

        color: "white",

        border: "none",

        borderRadius: "8px",

        cursor: "pointer",

        fontSize: "16px",

        fontWeight: "bold"

    },

    resultCard: {

        background: "#ffffff",

        marginTop: "35px",

        padding: "25px",

        borderRadius: "12px",

        maxWidth: "650px",

        marginLeft: "auto",

        marginRight: "auto",

        boxShadow:
            "0px 4px 15px rgba(0,0,0,0.12)"
    }

};

export default PredictionPage;