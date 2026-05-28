import React from "react";

import {

    Link

}

from "react-router-dom";

const Sidebar = () => {

    return (

        <div className="sidebar">

            <h2>

                Navigation

            </h2>

            <ul>

                <li>

                    <Link to="/dashboard">

                        Dashboard

                    </Link>

                </li>

                <li>

                    <Link to="/prediction">

                        Prediction

                    </Link>

                </li>

                <li>

                    <Link to="/gis">

                        GIS Map

                    </Link>

                </li>

                <li>

                    <Link to="/alerts">

                        Alerts

                    </Link>

                </li>

                <li>

                    <Link to="/settings">

                        Settings

                    </Link>

                </li>

            </ul>

        </div>

    );

};

export default Sidebar;