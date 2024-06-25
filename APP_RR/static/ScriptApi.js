function iniciarMapa(){
    const cordenadas = {lat:-33.4225469 ,lng: -70.610542};
    const mapa = new google.maps.Map(document.getElementById('mapa'),{
    zoom: 15,
    center: cordenadas
    });
    const Marcador = new google.maps.Marker({
    position: cordenadas,
    map: mapa
    });
}

const URL = 'https://api.thecatapi.com/v1/images/search';
        fetch(URL)
            .then(res => res.json())
            .then(data => {
                const img1 = document.querySelector('#fotollave1');
                img1.src = data[0].url;
                fetch(URL)
                    .then(res => res.json())
                    .then(data => {
                        const img2 = document.querySelector('#fotollave2');
                        img2.src = data[0].url;
                        fetch(URL)
                            .then(res => res.json())
                            .then(data => {
                                const img3 = document.querySelector('#fotollave3');
                                img3.src = data[0].url;
                            });
                    });
            });