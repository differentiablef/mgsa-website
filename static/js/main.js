
// /////////////////////////////////////////////////////////////////////////////
// Section: Global function definitions

// /////////////////////////////////////////////////////////////////////////////
// Name: loadScript
// Synop: loads a local script and executes it
// Note: onload_callback is required

function loadScript(script_name, onload_callback, doc) 
{

    if(typeof doc == "undefined")
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
// Name: initialize_scripts
// Synop: load all various
function initialize_scripts() 
{
    // Load scripts
    for( scr in scripts_local ) {
        loadScript(scr, scripts_local[scr]);
    }
    
    for( scr in scripts_url ) {
        loadScriptURL(scr, scripts_local[scr]);
    }
    
}


// /////////////////////////////////////////////////////////////////////////////
// Section: Document Event Callbacks

function window_onload()
{
    var menuHeader = getModuleName();
    // object tag names for various transform bits
    // mozTransfrom
    // msTransform
    // webkitTransform
    // oTransform
    // Transform
    
    // UI initialization
	$( "input:submit" ).button();
	$( "input:button" ).button();
	$("input:text, input:password, textarea").uniform();
	$("#notify-container").notify();
	
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
	} else {
	    console.log( typeof document.getElementsByName("login-form")[0] )
	}
	
}


function extern_onload()
{
    console.log("extern_onload");
}

function sijax_onload()
{
    console.log("sijax_onload");
}

function mathjax_onload()
{
MathJax.Hub.Config({
  jax: ["input/TeX","output/HTML-CSS"],
  extensions: ["tex2jax.js","MathMenu.js","MathZoom.js"],
  TeX: {
    extensions: ["AMSmath.js","AMSsymbols.js","noErrors.js","noUndefined.js"]
  }
});
    // initialize and configure mathjax
    MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
}

function chromeframe_onload()
{
    // test for chromeframe and if its needed
    CFInstall.check({
        mode: "overlay",
        destination: "http://uncc-mgsa.chromotopy.org/" 
    });
}
// /////////////////////////////////////////////////////////////////////////////
// Section: Main

// /////////////////////////////////////////////////////////////////////////////
// Section: Global variables

var scripts_local = {
    "extern" : extern_onload,
    "sijax" : sijax_onload
};

var scripts_url = {
    "http://ajax.googleapis.com/ajax/libs/chrome-frame/1/CFInstall.min.js" : chromeframe_onload,
    "http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML" : mathjax_onload
};

// Load all the scripts
initialize_scripts();

// Connect the events to their callback
window.onload = window_onload;





