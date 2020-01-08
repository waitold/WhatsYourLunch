change_map = function(name, loc) {
    const url ="https://maps.google.co.jp/maps?output=embed&q=";
    const map = document.getElementById('map');
    const query = name.toString() + loc.toString();
    document.getElementById('form').value = name;
    document.getElementById('location').value = name.toString() + " " + loc.toString();
    map.src = url + query
};
change_place = function (place) {

    document.getElementById("id_place").value = place.toString();
};
change_query = function (query) {

    document.getElementById("id_keyword").value = query.toString()
};
change_radius = function (radius) {

    document.getElementById("id_radius").value = radius
};
