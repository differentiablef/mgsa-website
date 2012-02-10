# ##############################################################################
# Basic Module interface
# Synop: Here you will find the methods used by content modules to interface 
#        with and register information with the main controller
#

# ##############################################################################
# Basic Flask imports

from flask import Blueprint
from flask import url_for

# ##############################################################################
# Name: ContentModule
# Synop: Module object which will be connected with the application object
#        from base
#

class ContentModule(Blueprint):
    _mod_name = None
    _name = {}
    _menus = {}
    _menus_html = {}
    _side_menus = {}
    _side_menus_html = {}
    _side_menu_roles = {}

    def __init__(self, name, modname):
        Blueprint.__init__(self, name, modname, url_prefix="/mod" + name, template_folder='templates')
        self._menus = {}
        self._side_menus = {}
        self._name = name
        self._mod_name = modname
        self._side_menu_roles = {}
        self._menus_html = {}
        self._side_menus_html = {}

    
    def __repr__(self):
        return '<ContentModule: %s @ %s>' % (self._name, self._name)
    

    def add_menu(self, name, target):
        self._menus[name] = target
        self._menus_html[name] = None
    
    # #########################################################################
    # Name: add_side_menu and add_raw_side_menu
    # Synop: using the dict provided, store the side panel information
    # Note: The role is not required and if it is not given the default
    #       is to not check user roles. If it is given, the user must have the 
    #       stated role for the sidepanel to appear
    #
    def add_side_menu(self, name, sidepaneldict, role="default"):
        self._side_menus[name] = sidepaneldict
        self._side_menu_roles[name] = role
        self._side_menus_html[name] = None
        

    def get_menus(self, user=None):
        
        
        # Format for generic main menu entries
        # <a href="{{ url_for(target) }}"><span><b>name</b></span></a>
        chunk = ""
        
        for name, htm in self._menus_html.iteritems():
            if htm is None:
                self._menus_html[name] = "<a href=\"" + url_for(self._menus[name]) + "\"><span><b>" + name + "</b></span></a>\n"
                htm = self._menus_html[name]
            
            chunk += htm

        return chunk
    
    def get_side_menus(self, user=None):
        # jquery is used to render the side panels, but the generic style is 
        # functional.
        #
        #<h3> name </h3>
        #<div>
        #<ul>
        #    <li><a href="{{ subtarget }}"> subname </a></li>
        #</ul>
        #</div>
        chunk = ""
        
        for name, htm in self._side_menus_html.iteritems():
            if htm is None:
                k = "<h3><a href=\"#" + self._name + "\">"+ name + "</a></h3>\n"
                k += "<div><ul>\n"
                for pair in self._side_menus[name]:
                    k += "  <li><a href='" + url_for(pair[1]) + "'>" + pair[0] + "</a>\n"
                k+="</ul><br></div>\n"
                self._side_menus_html[name] = k
                htm = k
        
            if not user is None: 
                rol = self._side_menu_roles[name]
                if rol == "default" or user.has_role(rol):
                    chunk += htm

        return chunk

