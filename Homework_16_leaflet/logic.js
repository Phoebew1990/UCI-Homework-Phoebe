
  var lightMap = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/streets-v11",
    accessToken: API_KEY
  });

  var link = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_week.geojson";
  var earthquakes = new L.LayerGroup();

 


  d3.json(link, function(earthquakeData){
      function markerSize(magnitude){
          return magnitude * 3
      }
      console.log(earthquakeData)
      var earthquakes = L.geoJson(earthquakeData,{
          pointToLayer: function(feature,latlng){
              return L.circleMarker(latlng)
          },
        style:styleInfo
      })

      function chooseColor(depth){
          switch (true){
              case depth < 2:
                  return "#E0F2F7";
              case depth >=2 && depth <5:
                  return "#58ACFA";
              case depth >= 5 && depth <7:
                  return "#0040FF";
              case depth >7:
                  return "#0B2161";
          }
      }

      function styleInfo(feature){
          return {
              opacity: 1.5,
              fillOpacity: 1.5,
              fillColor: chooseColor(feature.properties.mag),
              color: "white",
              radius: markerSize (feature.geometry.coordinates[3]),
              stroke: true,
              weight: 0.5
          };
      }

  var baseMaps = {
        "LightMap": lightMap
    };
  
    var overlayMaps = {
      "Earthquakes": earthquakes
  };
  var myMap = L.map("map", {
    center: [50.4374,51.2402],
    zoom: 5,
    layers: [lightMap,earthquakes]
  
  });
  L.control.layers(baseMaps,overlayMaps).addTo(myMap);

  //Legend
  var legend = L.control({
    position: "bottomright"
  });

  
  legend.onAdd = function() {
    var div = L.DomUtil.create("div", "info legend");
    var grades = [0, 2, 5, 7,"+"];
    var colors = [
      "#E0F2F7",
      "#58ACFA",
      "##0040FF",
      "#0B2161"
    ];

    // Looping through
    for (var i = 0; i < 4; i++) {
      div.innerHTML +=
        "<i style='background: " + colors[i] + "'></i> " +
        grades[i] + (grades[i + 1] ? "&ndash;" + grades[i + 1] + "<br>" : "+");
    }
    return div;
  };

  // Finally, we our legend to the map.
  legend.addTo(myMap);

  })









 