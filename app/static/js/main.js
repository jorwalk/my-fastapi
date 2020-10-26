$(document).ready(function () {
    var client_id = Date.now()
    document.querySelector("#ws-id").textContent = client_id;
    let sock = `ws://localhost:5000/ws/${client_id}`
    var ws = new WebSocket(sock);

    var list = $("#imagesRow").append('<ul></ul>').find('ul');
    ws.onmessage = function (event) {
        var msg = JSON.parse(event.data);
        switch (msg.message) {
            case "file":
                list.append('<li><img class="img-fluid" src="' + msg.path + '"/></li>');
                break;
            case "text":
                list.append('<li><p>' + msg.response + '</p></li>');
                list.append('<li><img class="img-fluid" src="' + msg.path + '"/></li>');
                break;
        }
    };
    ws.onopen = function (event) {
        console.log("WebSocket is open now.");
    };
    ws.onclose = function (event) {
        console.log("WebSocket is closed now.");
    };

    function encodeImgtoBase64(element) {
        var img = element.files[0];
        var reader = new FileReader();
        reader.onloadend = function () {
            var msg = {
                type: "message",
                result: reader.result
            };
            ws.send(JSON.stringify(msg))
        }
        reader.readAsDataURL(img);
    }

    $("#uploadImage").on('change', function () {
        encodeImgtoBase64($(this)[0])
    });
})