

$(document).ready(function() {
    
	$( "textarea" ).tinymce({
        theme : "advanced",
	    scrollbars: true,
        plugins : "jqueryinlinepopups,style,table,advimage,advlink,preview,contextmenu,paste,fullscreen,xhtmlxtras",
        theme_advanced_buttons1 : "code,preview,|,bold,italic,underline,|,justifyleft,justifycenter,justifyright,justifyfull,|,formatselect,fontselect,fontsizeselect",
        theme_advanced_buttons2 : "styleprops,|,attribs,|,tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,fullscreen",
        theme_advanced_buttons3 : "cut,copy,paste,pastetext,|,bullist,numlist,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,|,forecolor,backcolor",
        theme_advanced_toolbar_location : "top",
        theme_advanced_toolbar_align : "left",
        theme_advanced_statusbar_location : "bottom",
        theme_advanced_resizing : false,        
        theme_advanced_resize_horizontal : 1,
        theme_advanced_resizing_use_cookie : 0,
        content_css: "css/content.css"
    });
    
});
