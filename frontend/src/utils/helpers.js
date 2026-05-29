export const formatDate=(date)=>{

    return new Date(date)

    .toLocaleDateString();

};

export const formatTime=(date)=>{

    return new Date(date)

    .toLocaleTimeString();

};

export const capitalize=(text)=>{

    return text.charAt(0)

    .toUpperCase()

    +

    text.slice(1);

};

export const calculateAccuracy=(

    tp,
    tn,
    fp,
    fn

)=>{

    return(

        (

            tp+tn

        )

        /

        (

            tp+tn+fp+fn

        )

        *100

    ).toFixed(2);

};