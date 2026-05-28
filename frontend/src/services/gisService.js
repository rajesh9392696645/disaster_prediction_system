import API from "./api";

const gisService = {

    getMapData: async () => {

        try {

            const response =
                await API.get(
                    "/gis/map-data"
                );

            return response.data;

        }

        catch (error) {

            throw error;

        }

    },

    getAffectedAreas: async () => {

        try {

            const response =
                await API.get(
                    "/gis/affected-areas"
                );

            return response.data;

        }

        catch (error) {

            throw error;

        }

    },

    getSatelliteImagery: async () => {

        try {

            const response =
                await API.get(
                    "/gis/satellite"
                );

            return response.data;

        }

        catch (error) {

            throw error;

        }

    }

};

export default gisService;