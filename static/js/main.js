
// /////////////////////////////////////////////////////////////////////////////
// Section: Global variables
// NOTE: there are other onload handlers, but they are connected in layout.html

var scripts_local = {
    "extern": extern_onload,
    "sijax": sijax_onload
}

// /////////////////////////////////////////////////////////////////////////////
// Section: Global function definitions

// /////////////////////////////////////////////////////////////////////////////
// Name: require 
// Synop: load a script with async turned off.
function require(script, callback) {
    if(typeof(callback) == "undefined")
        callback = function() {};
    
    $.ajax({
        url: $SCRIPT_ROOT + script + ".js",
        dataType: "script",
        cache: true,
        async: false,
        success: callback,
        error: function () {
            throw new Error("Could not load script " + script);
        }
    });
}

// /////////////////////////////////////////////////////////////////////////////
// Name: loadScript
// Synop: loads a local script and executes it
// Note: onload_callback is required

function loadScript(script_name, onload_callback, doc) 
{

    if(typeof(doc) == "undefined")
        doc = document;

    var scrTag = doc.createElement("script");
    scrTag.src = $SCRIPT_ROOT + script_name + ".js";
    scrTag.type = "text/javascript";
    scrTag.onload = onload_callback;
    doc.getElementsByTagName("head")[0].appendChild(scrTag);
    
}

// /////////////////////////////////////////////////////////////////////////////
// Name: loadScript
// Synop: loads a script from given url and executes it
// NOTE: onload_callback is required
function loadScriptURL(script_url, onload_callback, doc) 
{
    if(typeof doc == "undefined")
        doc = document;
    
    var scrTag = doc.createElement("script");
    scrTag.src = script_url;
    scrTag.type = "text/javascript";
    scrTag.onload = onload_callback;
    doc.getElementsByTagName("head")[0].appendChild(scrTag);
}

// /////////////////////////////////////////////////////////////////////////////
// Name: getQueryString
// Synop: return the value of a GET argument
//
function getQueryString(key, default_)
{
	if (default_==null) default_="";
	 
	key = key.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
	var regex = new RegExp("[\\?&]"+key+"=([^&#]*)");
	var qs = regex.exec(window.location.href);
	if(qs == null)
		return default_;
  	else
		return qs[1];
}


// /////////////////////////////////////////////////////////////////////////////
// Name: getModuleName
// Synop: parse the url and extra the name of the module we are currently in
//
function getModuleName()
{
    // basic url scheme is as follows:
    //
    //   baseurl/mod<module_name>/module_view[/?]crap&get_args=crap
    //
    // so baring some future idiocy finding module_name should be as simple 
    // as:
    var sp = window.location.href.split('mod');
    
    if(sp.length > 1) {
        var name = sp[1].split('/')[0];
        return name;
    }
    
    return ""; 
}


// /////////////////////////////////////////////////////////////////////////////
// Name: initialize_site
// Synop: load all various crap and call entry point
function initialize_site(entry_point) 
{
    /* Now mostly handled in layout.html using onload="" tag */

    loadScript("jquery", function() {
        for( scr in scripts_local ) {
            require(scr, scripts_local[scr]);
        }
        
        entry_point();
    });
    
}

// /////////////////////////////////////////////////////////////////////////////
// Name: extern_onload
// Synop: after extern.js has been loaded and executed, this gets called
function extern_onload()
{
    console.log("extern_onload");
}

// /////////////////////////////////////////////////////////////////////////////
// Name: sijax_onload
// Synop: after sijax.js has been loaded and executed, this gets called
function sijax_onload()
{
    
    var ajaxAddress = "/ajax";
    
    if( $MODULE_NAME != "" ) {
        var hh = window.location.href.split('mod')[0];
        
        ajaxAddress = hh + "mod" + getModuleName() + "/ajax";
    }
    
    console.log("sijax_onload");
    
    Sijax.setRequestUri(ajaxAddress);
    Sijax.setJsonUri("/static/js/json2.js");
}
// /////////////////////////////////////////////////////////////////////////////
// Name: mathjax_onload
// Synop: once the mathjax enviornment is loaded this gets called
//        and we configure the whole deal for rendering
function mathjax_onload()
{
    // initialize and configure mathjax
    MathJax.Hub.Config({
        jax: ["input/TeX","output/HTML-CSS"],
        extensions: ["tex2jax.js","MathMenu.js","MathZoom.js"],
        TeX: {
            extensions: ["AMSmath.js","AMSsymbols.js","noErrors.js","noUndefined.js"]
        },
        tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
    });
    
}

// /////////////////////////////////////////////////////////////////////////////
// Name: chromeframe_onload
// Synop: after chromframe script is loaded, test if we need to flash
//        an install message
function chromeframe_onload()
{
    // test for chromeframe and if its needed
    CFInstall.check({
        mode: "overlay",
        destination: "http://uncc-mgsa.chromotopy.org/" 
    });
}

// /////////////////////////////////////////////////////////////////////////////
// Name: document_loaded
// Synop: called once the browser has loaded the main html document
//        this is done by placing
//
//   <script type="text/javascript">
//        document_loaded();
//   </script>
// 
//         At the very end of the document
//
function document_loaded()
{
    console.log("document_loaded");
    
    ////////////////////////////////////////////////////////////////////////////
    // now that everything is loaded and known, we can start
    // dicking with it:
    initialize_site(main);
}

// /////////////////////////////////////////////////////////////////////////////
// Name: window_onload
// Synop: called once the document is done loading
function window_onload(e)
{
    console.log("window_onload");
    
    // request flash messages from server
    Sijax.request('get-messages');
    
    // see what we get
    if(typeof($flash_messages) != "undefined"){
        $flash_messages.forEach(
            function(msg) {
                $("#notify-container").notify("create", msg);
            }
        );
    }
    
    // call the modules onload handler
    if( typeof(module_onload) != "undefined" )
    {
        module_onload();
    }

}

// ////////////////////////////////////////////////////////////////////////////
// Section: Connect events and callbacks

window.onload = window_onload;

// /////////////////////////////////////////////////////////////////////////////
// Section: Main

function main()
{
    console.log("main");
    var menuHeader = $MODULE_NAME;
    // object tag names for various transform bits
    // mozTransfrom
    // msTransform
    // webkitTransform
    // oTransform
    // Transform
    
    // UI initialization
	$( "input:submit" ).button();
	$( "input:button" ).button();
	$( "input:text, input:password, textarea" ).uniform();
	$( "#notify-container" ).notify();
	
	// Setup the user menu, and define the navigationFilter ( see jquery-ui accordion docs )
	
	if( typeof document.getElementsByName("login-form")[0] == "undefined" ) {
        $( "#user-navigation-bar" ).accordion( {
            icons: false, 
            autoHeight: false, 
            navigation: true,
            navigationFilter: function (){
	    	  return menuHeader === this.href.split("#")[1];
	    	}
	    });
	}
    

    
    // check to see if there is a js entry point for the current content 
    // module. If there is, then call it.
    if( typeof(module_init) != "undefined" )
    {
        module_init();
    }
    
    $("body").show();
}

// ////////////////////////////////////////////////////////////////////////////
// Section: Globals

$MODULE_NAME = getModuleName();



