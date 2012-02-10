
function getQuerystring(key, default_)
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

// // Old way
//var menuHeader = getQuerystring('menu');

// New Way
var menuHeader = getModuleName();

$(document).ready( function() {
    	// object tag names for various transform bits
    	// mozTransfrom
    	// msTransform
    	// webkitTransform
    	// oTransform
    	// Transform
    	
    // UI initialization
	$( "input:submit" ).button();
	$( "input:button" ).button();
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
	$("input:text, input:password, textarea").uniform();
	
});

MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
