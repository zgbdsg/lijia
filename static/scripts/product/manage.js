var changeIsExp = {}
var videoList = [];
var isChanged = false;
var isExpOnChange = function (id, that) {
    isChanged = true;
    videoList.map((item)=>{
        if(item.id==id){
            item.isExp=that.checked ? 1 : 0;
            that.parentNode.parentNode.dataset.isexp=item.isExp;
        }
        return item;
    })
    console.log("videoList",videoList);
    //changeIsExp[id] = that.checked ? 1 : 0;
}
var submitIsExp = function () {
    if (!isChanged) {
        alert("Nothing to update")
    } else {
        $.post('/manage/update-video-data',{videoList:JSON.stringify(videoList)}, function (resp) {
            console.log(resp);
            if (resp) {
                alert("更新成功");
                changeIsExp = {}
                location.reload();
            }else{
                alert("更新失败")
            }
        }, "json");
    }
}


var fixHelper = function (e, ui) {
    ui.children().each(function () {
        $(this).width($(this).width());  //在拖动时，拖动行的cell（单元格）宽度会发生改变。 
    });
    return ui;
};

$(function () {
    var initList = $(".item");
    $.each(initList, function (i, value) {
        videoList.push({ id: $(value).attr("data-id"), index: i, isExp: $(value).attr("data-isexp") });
    })
    console.log("initList",videoList);
    $(".videolist tbody").sortable({
        cursor: "move",
        helper: fixHelper,
        axis: "y",                           //行移动
        start: function (e, ui) {
            ui.helper.css({ "background": "#fff" })     //拖动时的行，要用ui.helper
            return ui;
        }
        , sort: function (e, ui) { }
        , stop: function (e, ui) {
            isChanged = true;
            var item = ui.item[0];
            var list = item.parentNode.childNodes;
            let index = 0;
            videoList = [];
            $.each(list, function (i, value) {
                if (value.className && value.className.indexOf("item") > -1) {
                    videoList.push({ id: $(value).attr("data-id"), index: index++, isExp: value.dataset.isexp });
                }
            })
            console.log(videoList);
        }
    })
    $(".videolist tbody").disableSelection(); //移动后固定
})