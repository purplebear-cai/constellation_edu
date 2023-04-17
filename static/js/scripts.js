$(document).ready(function () {
    $('#constellation-form').on('submit', function (event) {
        event.preventDefault();
        let constellationName = $('#constellation-name').val();
        $.post('/get_constellation_info', { constellation_name: constellationName }, function (data) {
            $('#constellation-info').html('');
            $('#constellation-map').html('');
            $('#constellation-pictures').html('');

            let infoHtml = '';
            for (const [key, value] of Object.entries(data.constellation_info)) {
                if (key === "famous_star_names") {
                    infoHtml += `<h2>Famous Stars</h2>`;
                    infoHtml += createStarsTable(value);
                } else {
                    infoHtml += `<h2>${key.replace(/_/g, ' ')}</h2><p>${value}</p>`;
                }
            }
            $('#constellation-info').html(infoHtml);

            let mapHtml = `<h2>Constellation Map</h2>
            <video width="100%" controls>
                <source src="${data.constellation_map}" type="video/quicktime">
                Your browser does not support the video tag.
            </video>`;
            $('#constellation-map').html(mapHtml);

            let picturesHtml = `<h2>Constellation Pictures</h2>`;
            for (const picture of data.constellation_info.pictures) {
                picturesHtml += `<img src="${picture}" alt="${constellationName} Constellation Picture" style="max-width: 100%; margin-bottom: 10px;">`;
            }
            $('#constellation-pictures').html(picturesHtml);
        }).fail(function (jqXHR, textStatus, errorThrown) {
            alert(jqXHR.responseJSON ? jqXHR.responseJSON.error : errorThrown);
        });
    });
});


function createStarsTable(mainStars) {
    let tableHtml = `<table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Magnitude</th>
                <th>Distance (light-years)</th>
            </tr>
        </thead>
        <tbody>`;

    for (const star of mainStars) {
        tableHtml += `
            <tr>
                <td>${star.name}</td>
                <td>${star.magnitude}</td>
                <td>${star.distance}</td>
            </tr>`;
    }

    tableHtml += `</tbody></table>`;
    return tableHtml;
}