change_map = function(name) {
    const url ="https://maps.google.co.jp/maps?output=embed&q=";
    const map = document.getElementById('map');
    map.src = url + name
};
