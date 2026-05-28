import React from "react";

import { useNavigate } from "react-router-dom";

const Navbar = () => {

    const navigate = useNavigate();

    const logout = () => {

        localStorage.clear();

        navigate("/");

    };

    return (

        <nav className="navbar">

            <h2>

                Disaster Prediction System

            </h2>

            <div>

                <button
                    onClick={logout}
                    className="nav-btn"
                >

                    Logout

                </button>

            </div>

        </nav>

    );

};

export default Navbar;