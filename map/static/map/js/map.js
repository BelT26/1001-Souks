// //The below code is adapted from the Google maps documentation

function initMap() {
    const center = { lat: 31.98, lng: -8.01 };
    const map = new google.maps.Map(document.getElementById("map-container"), {
      zoom: 7,
      center: center,
      mapTypeId: 'hybrid'
    });
    const locations = [
        { 
            name: 'Marrakesh',
            coords:  { lat: 31.63, lng: -7.98 },
            contentString: '<div id="content">' +
            '<div id="siteNotice">' +
            "</div>" +
            '<h1 class="map-heading text-center">Marrakesh</h1>' +
            '<div id="bodyContent">' +
            "<p><b>Uluru</b>, also referred to as <b>Ayers Rock</b>, is a large " +
            "sandstone rock formation in the southern part of the " +
            "Northern Territory, central Australia." +
            '<p>Attribution: Uluru, <a href="https://en.wikipedia.org/w/index.php?title=Uluru&oldid=297882194">' +
            "https://en.wikipedia.org/w/index.php?title=Uluru</a> " +
            "(last visited June 22, 2009).</p>" +
            "</div>" +
            "</div>"
        },
        { 
            name: 'Taroudant',
            coords:  { lat: 30.47, lng: -8.875 },
            contentString: '<div id="content">' +
            '<div id="siteNotice">' +
            "</div>" +
            '<h1 class="map-heading text-center">Taroudant</h1>' +
            '<div id="bodyContent">' +
            "<p><b>Uluru</b>, also referred to as <b>Ayers Rock</b>, is a large " +
            "sandstone rock formation in the southern part of the " +
            "Northern Territory, central Australia." +
            '<p>Attribution: Uluru, <a href="https://en.wikipedia.org/w/index.php?title=Uluru&oldid=297882194">' +
            "https://en.wikipedia.org/w/index.php?title=Uluru</a> " +
            "(last visited June 22, 2009).</p>" +
            "</div>" +
            "</div>"
            },
        { 
            name: 'Fez',
            coords:  { lat: 34.02, lng: -5.01 },
            contentString: '<div id="content">' +
            '<div id="siteNotice">' +
            "</div>" +
            '<h1 class="map-heading text-center">Fez</h1>' +
            '<div id="bodyContent">' +
            "<p><b>Uluru</b>, also referred to as <b>Ayers Rock</b>, is a large " +
            "sandstone rock formation in the southern part of the " +
            "Northern Territory, central Australia." +
            '<p>Attribution: Uluru, <a href="https://en.wikipedia.org/w/index.php?title=Uluru&oldid=297882194">' +
            "https://en.wikipedia.org/w/index.php?title=Uluru</a> " +
            "(last visited June 22, 2009).</p>" +
            "</div>" +
            "</div>"
            },
        {
            name: 'Essaouira',
            coords: { lat: 31.51, lng: -9.76 },
            contentString: '<div id="content">' +
            '<div id="siteNotice">' +
            "</div>" +
            '<h1 class="map-heading text-center">Essaouira</h1>' +
            '<div id="bodyContent">' +
            "<p><b>Uluru</b>, also referred to as <b>Ayers Rock</b>, is a large " +
            "sandstone rock formation in the southern part of the " +
            "Northern Territory, central Australia." +
            '<p>Attribution: Uluru, <a href="https://en.wikipedia.org/w/index.php?title=Uluru&oldid=297882194">' +
            "https://en.wikipedia.org/w/index.php?title=Uluru</a> " +
            "(last visited June 22, 2009).</p>" +
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
    
