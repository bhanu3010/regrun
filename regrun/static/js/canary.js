$(document).ready(function () {
    var userId;
    jQuery.support.cors = true;
    var namespace = '/regrun';
    var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);
    socket.on('connect', function () {
        socket.emit('subscribe');
        console.log("just connected to test namespace");
        socket.on('run_log', function (msg) {
            console.log("Received msg from server" + msg);
        });
    });

    $("#schedule-form").click(function (event) {
        event.preventDefault();
        params = {
            'requester': $("#requester").val(),
            'env_id': $("#env_id").val(),
            'interface': $("#interface").val(),
            'template': $("#template").val(),
            'custom_path': $("#custom_path").val(),
            'userid': userId
        };

        console.log(params);
        socket.emit("run_schedule", {"data": params}
        );
        return false;

    });

    socket.on('userid', function (msg) {
        userId = msg.userid;
    });

    socket.on("response", function (data) {
        console.log("Received" + data['args']);
        run_log = "run_log_" + data['req_id'];
        run_log_status = "run_log_status_" + data['req_id'];
        $("#" + run_log_status).removeClass();
        $("#" + run_log_status).addClass("label label-info");
        $("#" + run_log_status).text("RUNNING");
        $('#' + run_log).append(data['args'] + "<br>");

    });

    socket.on('error', function (msg) {
        $("#error").removeClass('hidden');
        $('#error').addClass("alert alert-danger alert-dismissable fade in");
        $("#error").text(msg['data']);
    });

    socket.on("exit", function (data) {
        console.log('Received ' + data['status']);
        console.log('Received ' + data['req_id']);
        run_log_status = "run_log_status_" + data['req_id'];
        status = data['status'];
        if (status == 'SUCCESS') {
            $("#" + run_log_status).removeClass();
            $("#" + run_log_status).addClass("label label-success");
            $("#" + run_log_status).text(data['status']);
        } else if (status == 'FAILED') {
            $("#" + run_log_status).removeClass();
            $("#" + run_log_status).addClass("label label-important");
            $("#" + run_log_status).text(data['status']);
        }
    });

    socket.on("redirect", function (data) {
        window.location = data.url;
    });

})