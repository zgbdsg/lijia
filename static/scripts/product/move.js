window.onload = function () {
    var container = document.getElementsByClassName("dialog-move");
    if (container && container.length > 0) {
        var item = container[0];
        item.onmousedown = function (ev) {
            var oevent = ev || event;

            var distanceX = oevent.clientX - item.offsetLeft;
            var distanceY = oevent.clientY - item.offsetTop;

            document.onmousemove = function (ev) {
                var oevent = ev || event;
                item.style.left = oevent.clientX - distanceX + 'px';
                item.style.top = oevent.clientY - distanceY + 'px';
            };
            document.onmouseup = function () {
                document.onmousemove = null;
                document.onmouseup = null;
            };
            ;
        };
    }
}