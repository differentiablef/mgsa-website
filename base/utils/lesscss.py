# -*- coding: utf-8 -*-
"""
    flaskext.lesscss
    ~~~~~~~~~~~~~

    A small Flask extension that makes it easy to use LessCSS with your Flask
    application.

    :copyright: (c) 2010 by Steve Losh.
    :license: MIT, see LICENSE for more details.
    
    MODIFIED: 01/22/2012 by Michael Blackmon
    Only run during the debug and development, this is checked by looking for app.debug
        (Note: if this gives alright results might make it into production.)
        
    Moreover, the path search is restricted to static/css/src, and a fixed list of 
    selected project .less files, this list is configured in website.conf by setting 
    WEBSITE_STYLE_SHEETS to an array listing their filenames relative the static/css/src
    path
"""

import os, subprocess

def lesscss(app):
    @app.before_request
    def _render_less_css():
        static_dir = app.root_path + '/' + app.config['WEBSITE_STYLE_SRCDIR']
        less_paths = app.config['WEBSITE_STYLE_SHEETS']
        
        
        for less_path in less_paths:
            fullpath = static_dir + '/' + less_path
            css_path = static_dir + '/../' + os.path.splitext(less_path)[0].replace('.','-') + '.css'
            
            if not os.path.isfile(css_path):
                css_mtime = -1
            else:
                css_mtime = os.path.getmtime(css_path)
            
            less_mtime = os.path.getmtime(fullpath)
            if less_mtime >= css_mtime:
                subprocess.call(['lessc', fullpath, css_path], shell=False)


