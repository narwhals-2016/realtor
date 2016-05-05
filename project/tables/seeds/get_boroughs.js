// getting boroughs for each neighborhood off maps.nyc.census website
var neighborhood = $("svg.V_DCP_NEIGHBORHOOD").children;
var nbBorough = {};

for (var i = 0; i < neighborhood.length; i++) {
    var borough = neighborhood[i].id;
    var nb = neighborhood[i].getAttribute("title");
    nbBorough[nb] = borough
}