// from data.js
var tableData = data;

// select the button
var button = d3.select("#filter-btn");

// Event

button.on("click",filterDate);

// Function

function filterDate(){


    //Prevent the page from refreshing
    d3.event.preventDefault();

    //Select Input
    var inputDatetime = d3.select("#datetime");


    //Get the Value of input
    var inputDateValue = inputDatetime.property("value");


    //get filtered date
    var filteredData = tableData.filter(ufo=> (ufo.datetime == inputDateValue));
    
    
    //get the table
    var tbody = d3.select("tbody")
    tbody.html("")



    filteredData.forEach((ufo) => {
        var row = tbody.append("tr");
        Object.entries(ufo).forEach(function([key,value]){
            console.log(key,value);
            
            

            var cell = row.append("td");
            cell.text(value);
        })

    })
                          



}
