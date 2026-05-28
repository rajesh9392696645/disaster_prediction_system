import React, { useState } from "react";

const PredictionForm = () => {

    const [formData,setFormData]=useState({

        disasterType:"",

        rainfall:"",

        temperature:"",

        humidity:""

    });

    const handleChange=(e)=>{

        setFormData({

            ...formData,

            [e.target.name]:
            e.target.value

        });

    };

    const handleSubmit=(e)=>{

        e.preventDefault();

        console.log(formData);

        alert(
            "Prediction Request Sent"
        );

    };

    return (

        <div style={styles.card}>

            <h2>

                Prediction Form

            </h2>

            <form onSubmit={handleSubmit}>

                <input

                    type="text"

                    name="disasterType"

                    placeholder="Disaster Type"

                    onChange={handleChange}

                    style={styles.input}

                />

                <input

                    type="number"

                    name="rainfall"

                    placeholder="Rainfall"

                    onChange={handleChange}

                    style={styles.input}

                />

                <input

                    type="number"

                    name="temperature"

                    placeholder="Temperature"

                    onChange={handleChange}

                    style={styles.input}

                />

                <input

                    type="number"

                    name="humidity"

                    placeholder="Humidity"

                    onChange={handleChange}

                    style={styles.input}

                />

                <button style={styles.button}>

                    Predict

                </button>

            </form>

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
    },

    input:{

        width:"100%",

        padding:"12px",

        marginBottom:"15px",

        borderRadius:"8px",

        border:
        "1px solid #cbd5e1"

    },

    button:{

        width:"100%",

        padding:"12px",

        background:"#2563eb",

        color:"white",

        border:"none",

        borderRadius:"8px"

    }

};

export default PredictionForm;