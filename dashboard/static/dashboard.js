/*
==========================================
Nova Mission Control Frontend
==========================================
*/


async function updateDashboard(){

    try {

        const response = await fetch("/status");

        const data = await response.json();


        document.getElementById(
            "confidence"
        ).innerHTML =
        data.confidence + "%";


        document.getElementById(
            "bot"
        ).innerHTML =
        data.bot;


        document.getElementById(
            "brain"
        ).innerHTML =
        data.brain;


        document.getElementById(
            "profit"
        ).innerHTML =
        data.profit;


        document.getElementById(
            "trades"
        ).innerHTML =
        data.trades_today;


    }

    catch(error){

        console.log(error);

    }

}


setInterval(

    updateDashboard,

    5000

);


updateDashboard();
