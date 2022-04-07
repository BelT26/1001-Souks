//The below code is based on the map section in the Bootstrap resume walkthrough project

// Creates a new google map and sets the zoom and central location
function initMap() {
    var map = new google.maps.Map(document.getElementById("map-container"), {
        zoom: 7,
        center: {
            lat: 31.66903100668774, 
            lng: -8.003742649163959,
        }
    });

    
// co-ordinates of each of the featured cities
    var locations = [
        { 
            name: 'Marrakesh',
            coords:  { lat: 31.63, lng: -7.98 }
         },
         {
             name: 'Essaouira',
             coords: { lat: 31.51, lng: -9.76 },
         }        
    ];

// maps markers to co-ordinates in the locations array    
    var markers = locations.map(function(location, i) {
        return new google.maps.Marker({
            position: location.coords,
            label: '*'
        });
    });

    var markerCluster = new MarkerClusterer(map, markers, { imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m' });
}


