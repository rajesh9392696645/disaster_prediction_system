import API from "./api";

const alertService = {

    getAlerts: async () => {

        try {

            const response =
                await API.get(
                    "/alerts"
                );

            return response.data;

        }

        catch (error) {

            throw error;

        }

    },

    createAlert: async (alertData) => {

        try {

            const response =
                await API.post(
                    "/alerts",
                    alertData
                );

            return response.data;

        }

        catch (error) {

            throw error;

        }

    },

    deleteAlert: async (id) => {

        try {

            const response =
                await API.delete(
                    `/alerts/${id}`
                );

            return response.data;

        }

        catch (error) {

            throw error;

        }

    }

};

export default alertService;