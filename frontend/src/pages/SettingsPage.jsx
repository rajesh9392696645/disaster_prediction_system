import React, { useState } from "react";

const SettingsPage = () => {

    const [settings,setSettings] = useState({

        username:"Admin",

        email:"admin@gmail.com",

        notifications:true,

        satelliteAPI:true,

        cnnModel:true,

        lstmModel:true,

        theme:"Light"

    });

    const handleChange = (e) => {

        const {name,value,type,checked} = e.target;

        setSettings({

            ...settings,

            [name]:
                type==="checkbox"
                ? checked
                : value

        });

    };

    const saveSettings = () => {

        alert(
            "Settings Saved Successfully"
        );

        console.log(settings);

    };

    return(

        <div style={styles.container}>

            <h1 style={styles.heading}>

                System Settings

            </h1>

            <p style={styles.subtitle}>

                Disaster Prediction System Configuration

            </p>

            <div style={styles.card}>

                <h2>

                    User Configuration

                </h2>

                <div style={styles.formGroup}>

                    <label>

                        Username

                    </label>

                    <input
                        type="text"
                        name="username"
                        value={settings.username}
                        onChange={handleChange}
                        style={styles.input}
                    />

                </div>

                <div style={styles.formGroup}>

                    <label>

                        Email

                    </label>

                    <input
                        type="email"
                        name="email"
                        value={settings.email}
                        onChange={handleChange}
                        style={styles.input}
                    />

                </div>

            </div>

            <div style={styles.card}>

                <h2>

                    AI Model Configuration

                </h2>

                <div style={styles.switchRow}>

                    <label>

                        CNN Model

                    </label>

                    <input
                        type="checkbox"
                        name="cnnModel"
                        checked={settings.cnnModel}
                        onChange={handleChange}
                    />

                </div>

                <div style={styles.switchRow}>

                    <label>

                        LSTM Model

                    </label>

                    <input
                        type="checkbox"
                        name="lstmModel"
                        checked={settings.lstmModel}
                        onChange={handleChange}
                    />

                </div>

            </div>

            <div style={styles.card}>

                <h2>

                    Satellite Configuration

                </h2>

                <div style={styles.switchRow}>

                    <label>

                        Enable Satellite API

                    </label>

                    <input
                        type="checkbox"
                        name="satelliteAPI"
                        checked={settings.satelliteAPI}
                        onChange={handleChange}
                    />

                </div>

            </div>

            <div style={styles.card}>

                <h2>

                    Notification Settings

                </h2>

                <div style={styles.switchRow}>

                    <label>

                        Enable Alerts

                    </label>

                    <input
                        type="checkbox"
                        name="notifications"
                        checked={settings.notifications}
                        onChange={handleChange}
                    />

                </div>

            </div>

            <div style={styles.card}>

                <h2>

                    Appearance

                </h2>

                <select
                    name="theme"
                    value={settings.theme}
                    onChange={handleChange}
                    style={styles.input}
                >

                    <option>

                        Light

                    </option>

                    <option>

                        Dark

                    </option>

                </select>

            </div>

            <button
                onClick={saveSettings}
                style={styles.button}
            >

                Save Settings

            </button>

        </div>

    );

};

const styles = {

    container:{

        minHeight:"100vh",

        background:"#f8fafc",

        padding:"35px"

    },

    heading:{

        textAlign:"center",

        color:"#1e3a8a"

    },

    subtitle:{

        textAlign:"center",

        color:"#64748b",

        marginBottom:"35px"

    },

    card:{

        background:"#ffffff",

        padding:"25px",

        borderRadius:"12px",

        marginBottom:"25px",

        boxShadow:
            "0px 4px 14px rgba(0,0,0,0.12)"
    },

    formGroup:{

        marginTop:"15px"

    },

    input:{

        width:"100%",

        padding:"12px",

        marginTop:"8px",

        borderRadius:"8px",

        border:"1px solid #cbd5e1"
    },

    switchRow:{

        display:"flex",

        justifyContent:"space-between",

        marginTop:"20px"
    },

    button:{

        width:"100%",

        padding:"15px",

        background:"#2563eb",

        color:"#ffffff",

        border:"none",

        borderRadius:"10px",

        cursor:"pointer",

        fontSize:"16px",

        fontWeight:"bold"
    }

};

export default SettingsPage;