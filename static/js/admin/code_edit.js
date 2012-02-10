
(function () {

    CodeMirror.defineMode("jinja2", 
    function(config, parserConfig) {
        var mustacheOverlay = {
            token: function(stream, state) {
                if (stream.match("{{")) {
                    while ((ch = stream.next()) != null)
                        if (ch == "}" && stream.next() == "}") break;
                    return "jinja2";
                }
                
                while (stream.next() != null && !stream.match("{{", false)) {}
            
                return null;
            
            }
        };
    
        return CodeMirror.overlayParser(CodeMirror.getMode(config, parserConfig.backdrop || "text/html"), mustacheOverlay);
    
    });
    
    
    
    var editor = CodeMirror.fromTextArea(document.getElementById("code"), {
        lineNumbers: true,
        theme: "night",
        mode: "jinja2",
        extraKeys: {
            "Ctrl-I": autoIndentDoc,
            "Ctrl-s": ajaxSaveFile
        }
    });
    
    function ajaxSaveFile() {
        
    }
    
    function autoIndentDoc() {
        var lineCount = editor.lineCount();
        for(var line = 0; line < lineCount; line++) {
            editor.indentLine(line);
        }
    }
    

})();



