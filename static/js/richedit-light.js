

$(document).ready(function() {

    $( "textarea" ).tinymce({
        theme : "advanced",
        plugins : "jqueryinlinepopups,table,advimage,advlink,preview,contextmenu,fullscreen",
        theme_advanced_buttons1 : "formatselect,fontsizeselect,|,bold,italic,underline,|,bullist,numlist,|,undo,redo,|,link,unlink,|,code,preview",
        theme_advanced_buttons2 : "",
        theme_advanced_buttons3 : "",
        theme_advanced_toolbar_location : "top",
        theme_advanced_toolbar_align : "left",
        theme_advanced_statusbar_location : "bottom",
        theme_advanced_resizing : false,
        theme_advanced_resize_horizontal : 1,
        theme_advanced_resizing_use_cookie : 0,
	scrollbars: "yes",
	scroll: true,
        height : "400",
        content_css: $SCRIPT_ROOT + "/static/css/content.css",
        skin: "thebigreason"
    });
});
