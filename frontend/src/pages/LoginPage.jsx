import React, { useState } from "react";
import "../assets/styles/login.css";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const LoginPage = () => {

    const navigate = useNavigate();

    const [formData, setFormData] = useState({
        email: "admin@gmail.com",
        password: "admin123"
    });

    const [loading, setLoading] = useState(false);

    const [error, setError] = useState("");

    const handleChange = (e) => {

        setFormData({
            ...formData,
            [e.target.name]: e.target.value
        });

    };

    const handleSubmit = async (e) => {

        e.preventDefault();

        setLoading(true);

        setError("");

        try {

            const response = await axios.post(
                "http://localhost:5000/api/auth/login",
                formData
            );

            localStorage.setItem(
                "token",
                response.data.token
            );

            localStorage.setItem(
                "user",
                JSON.stringify(response.data.user)
            );

            alert("Login Successful");

            navigate("/dashboard");

        }

        catch (err) {

            setError(
                err.response?.data?.message ||
                "Login Failed"
            );

        }

        finally {

            setLoading(false);

        }

    };

    return (

        <div style={styles.container}>

            <div style={styles.card}>

                <h1 style={styles.title}>
                    Disaster Prediction System
                </h1>

                <h3 style={styles.subtitle}>
                    AI + Satellite Emergency Platform
                </h3>

                {error && (

                    <div style={styles.errorBox}>
                        {error}
                    </div>

                )}

                <form onSubmit={handleSubmit}>

                    <div style={styles.formGroup}>

                        <label>Email</label>

                        <input
                            type="email"
                            name="email"
                            placeholder="Enter Email"
                            value={formData.email}
                            onChange={handleChange}
                            required
                            style={styles.input}
                        />

                    </div>

                    <div style={styles.formGroup}>

                        <label>Password</label>

                        <input
                            type="password"
                            name="password"
                            placeholder="Enter Password"
                            value={formData.password}
                            onChange={handleChange}
                            required
                            style={styles.input}
                        />

                    </div>

                    <button
                        type="submit"
                        style={styles.button}
                        disabled={loading}
                    >

                        {
                            loading
                                ? "Logging in..."
                                : "Login"
                        }

                    </button>

                </form>

                <div style={styles.footer}>

                    Emergency Response Monitoring

                </div>

            </div>

        </div>

    );

};

const styles = {

    container: {

        display: "flex",

        justifyContent: "center",

        alignItems: "center",

        height: "100vh",

        background:
            "linear-gradient(135deg,#0f172a,#1e293b)"
    },

    card: {

        width: "420px",

        background: "#ffffff",

        padding: "35px",

        borderRadius: "14px",

        boxShadow:
            "0px 8px 25px rgba(0,0,0,0.3)"
    },

    title: {

        textAlign: "center",

        color: "#1e3a8a",

        marginBottom: "10px"
    },

    subtitle: {

        textAlign: "center",

        color: "#475569",

        marginBottom: "30px"
    },

    formGroup: {

        marginBottom: "18px"
    },

    input: {

        width: "100%",

        padding: "12px",

        marginTop: "8px",

        borderRadius: "8px",

        border: "1px solid #cbd5e1",

        outline: "none"
    },

    button: {

        width: "100%",

        padding: "14px",

        background: "#2563eb",

        color: "white",

        border: "none",

        borderRadius: "8px",

        cursor: "pointer",

        fontWeight: "bold",

        fontSize: "16px"
    },

    errorBox: {

        background: "#fee2e2",

        color: "#b91c1c",

        padding: "10px",

        borderRadius: "6px",

        marginBottom: "15px"
    },

    footer: {

        marginTop: "20px",

        textAlign: "center",

        color: "#64748b"
    }

};

export default LoginPage;