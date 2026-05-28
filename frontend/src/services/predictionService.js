import API from "./api";

const predictionService = {

    predictDisaster: async (payload) => {

        try {

            const response =
                await API.post(
                    "/predict",
                    payload
                );

            return response.data;

        }

        catch (error) {

            throw error;

        }

    },

    getPredictionHistory: async () => {

        try {

            const response =
                await API.get(
                    "/predict/history"
                );

            return response.data;

        }

        catch (error) {

            throw error;

        }

    }

};

export default predictionService;