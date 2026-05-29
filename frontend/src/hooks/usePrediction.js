import {

    useState

}

from "react";

import predictionService

from "../services/predictionService";

const usePrediction=()=>{

    const [loading,setLoading]=

        useState(false);

    const [result,setResult]=

        useState(null);

    const [error,setError]=

        useState("");

    const runPrediction=

    async(payload)=>{

        try{

            setLoading(true);

            setError("");

            const response=

                await predictionService

                .predictDisaster(

                    payload

                );

            setResult(response);

        }

        catch(err){

            setError(

                err.message ||

                "Prediction Failed"

            );

        }

        finally{

            setLoading(false);

        }

    };

    return{

        loading,
        result,
        error,
        runPrediction

    };

};

export default usePrediction;