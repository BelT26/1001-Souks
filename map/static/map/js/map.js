// //The below code is adapted from the Google maps documentation

function initMap() {
    const center = { lat: 32.18, lng: -8.01 };
    const map = new google.maps.Map(document.getElementById("map-container"), {
      zoom: 6,
      center: center,
      mapTypeId: 'hybrid'
    });
    const locations = [
        { 
            name: 'Marrakech',
            coords:  { lat: 31.63, lng: -7.98 },
            contentString: '<div id="content">' +
            '<div id="siteNotice">' +
            "</div>" +
            '<h2 class="marker-heading text-center">Marrakech</h2>' +
            '<div id="bodyContent">' +
            "<p class='marker-text'> One of the four Imperial Cities of Morocco, Marrakech " +
            "in western Morocco is bordered by the Atlas mountains " +
            "to the south. Home to mosques, palaces and gardens, the " +
            "12th century Koutoubia mosque is a symbol of the city. </p>" +
            "<p class='marker-link text-center'><a href=Marrakech> Further Info </a></p>" +
            "</div>" +
            "</div>"
        },
        { 
            name: 'Taroudant',
            coords:  { lat: 30.47, lng: -8.875 },
            contentString: '<div id="content">' +
            '<div id="siteNotice">' +
            "</div>" +
            '<h2 class="marker-heading text-center">Taroudant</h2>' +
            '<div id="bodyContent">' +
            "<p class='marker-text'> Taroudant is situated in the fertile " +
            "Souss Valley in southeastern Morocco. First established as  " +
            "a trading centre in the 11th century, the red earth" +
            " ramparts date in parts to the 1500s. </p>" +
            "<p class='marker-link text-center'> <a href=Taroudant> Further Info </a> </p>" +        
            "</div>" +
            "</div>"
            },
        { 
            name: 'Fez',
            coords:  { lat: 34.02, lng: -5.01 },
            contentString: '<div id="content">' +
            '<div id="siteNotice">' +
            "</div>" +
            '<h2 class="marker-heading text-center">Fez</h2>' +
            '<div id="bodyContent">' +
            "<p class='marker-text'> Fez, in the northeast of Morocco,   " +
            "is often referred to as the country's cultural capital. " +
            "The medieval walled medina is home to religious schools " +
            "including the richly decorated 14th century Bou Inania " +
            "and Al Attarine. </p>" +
            "<p class='marker-link text-center'><a href=Fez> Further Info</a></p>" +
            "</div>" +
            "</div>"
            },
        {
            name: 'Essaouira',
            coords: { lat: 31.51, lng: -9.76 },       
            contentString: '<div id="content">' +
            '<div id="siteNotice">' +
            "</div>" +
            '<h2 class="marker-heading text-center">Essaouira</h2>' +
            '<div id="bodyContent">' +
            "<p class='marker-text'>Essaouira is a port city on the Atlantic coast, " +
            "protected by the 18th century ramparts of La Skala. " +
            "The 'Alizés' trade winds make the beach a destination for " +
            "surfing, windsurfing and kitesurfing. </p>" + 
            "<p class='marker-link text-center'><a href=Essaouira> Further Info </a></p>" +            
            "</div>" +
            "</div>"
        }        
    ];    
 

    // maps markers to co-ordinates in the locations array and
    // adds an info window   
    const markers = locations.map(function(location, i) {
        return new google.maps.Marker({
            position: location.coords,
            label: '*',
            map,
            title: location.name,
            infoWindow: new google.maps.InfoWindow({
                content: location.contentString,
                maxWidth: 320,
            })
        });
    });
    
    for(let marker of markers) {
        marker.addListener("click", () => {
            marker.infoWindow.open({
              anchor: marker,
              map,
              shouldFocus: false,
            });
          });
        }
    }
    
