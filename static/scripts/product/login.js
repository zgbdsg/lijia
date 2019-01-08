function signLogin() {
    var action = "login";
    $.post('/sign/0/action', { action: action }, function (data) {
    }, "json");
}