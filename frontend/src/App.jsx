import { Routes, Route } from "react-router-dom";

import LoginPage from "./pages/LoginPage";
import DashboardPage from "./pages/DashboardPage";
import PredictionPage from "./pages/PredictionPage";
import GISPage from "./pages/GISPage";
import AlertsPage from "./pages/AlertsPage";
import SettingsPage from "./pages/SettingsPage";

export default function App() {

    return (

        <Routes>

            <Route path="/" element={<LoginPage />} />

            <Route
                path="/dashboard"
                element={<DashboardPage />}
            />

            <Route
                path="/prediction"
                element={<PredictionPage />}
            />

            <Route
                path="/gis"
                element={<GISPage />}
            />

            <Route
                path="/alerts"
                element={<AlertsPage />}
            />

            <Route
                path="/settings"
                element={<SettingsPage />}
            />

        </Routes>

    );

}