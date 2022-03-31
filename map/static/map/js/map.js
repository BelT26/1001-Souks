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
}
