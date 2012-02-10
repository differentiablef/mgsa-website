$.widget( "custom.borderContent", {
		
		options: {
			// configurables
			angle: -0.30, // In Degrees :(
			leftSideWidth: 12,
			//lightPosition: "top-right", // "top-left" "bottom-left" "bottom-right"verticalAlign: "bottom",
			horizColor: "#cccccc",
			vertColor: "#dddddd"
			
			// callbacks
			
		},

		// the constructor
		_create: function() {
			var elem  = this.element;
			// this.element
			var angle = this.options.angle;
			var angleDeg = angle * (180.0 / Math.PI);
			var supAngle = -Math.PI/2.0 - angle; 
			var supAngleDeg = supAngle * (180.0 / Math.PI);
			
			var sideWidth = this.options.leftSideWidth;
			var yoff = -(sideWidth/2.0)*Math.tan(angle);
			
			var bottomHeight = 2.0 * yoff;
			var xoff = -(bottomHeight/2.0)*Math.tan(supAngle);
			
			var height = elem.outerHeight();
			var width = elem.outerWidth();
			var cont = elem.html();
			
			
			elem.html(
			    "<div style=\"display: none;\" class=\"border-content\">"  + cont + "</div>" +
			    "<div style=\"display: none;\" class=\"border-left\"></div>" +
			    "<div style=\"display: none;\" class=\"border-right\"></div>" +
			    "<div style=\"display: none;\" class=\"border-bottom\"></div>" 
			);
			
			var dleft = elem.find(".border-left");
			var dright = elem.find(".border-right");
			var dbottom = elem.find(".border-bottom");
			var dcontent = elem.find(".border-content");
			
			//height = height + dcontent.paddingTop + dcontent.paddingBottom;				
			//width = width + dcontent.paddingLeft + dcontent.paddingLeft; 
			dcontent.css({
				display: "block",
				position: "relative",
				verticalAlign: "bottom",
				left: sideWidth + "px",
				
				height: height + "px",
				width: (width - sideWidth) + "px"
			});
			
			dleft.css('transform', "skewY(" + angleDeg + "deg)");
			dleft.css({
				display: "block",
				position: "relative",
				verticalAlign: "bottom",
				webkitTransform: "skewY(" + angleDeg + "deg)",
				mozTransform: "skewY(" + angleDeg + "deg)",
				oTransform: "skewY(" + angleDeg + "deg)",
				msTransform: "skewY(" + angleDeg + "deg)",
				transform: "skewY(" + angleDeg + "deg)",
				top: yoff - height + "px",
				height: height + "px",
				width: sideWidth + "px"
			});
			dright.css('transform', "skewY(" + angleDeg + "deg)");
			dright.css({
				display: "block",
				position: "relative",
				verticalAlign: "bottom",
				webkitTransform: "skewY(" + angleDeg + "deg)",
				mozTransform: "skewY(" + angleDeg + "deg)",
				oTransform: "skewY(" + angleDeg + "deg)",
				msTransform: "skewY(" + angleDeg + "deg)",
				transform: "skewY(" + angleDeg + "deg)",
				top: ( yoff - 2.0 * height) + "px",
				left: (width - sideWidth) + "px",
				height: (height)+ "px",
				width: sideWidth + "px"
			});
			
			dbottom.css('transform',  "skewX(" + supAngleDeg + "deg)");
			dbottom.css({
				display: "block",
				position: "relative",
				width: (width - sideWidth) + "px",
				height: bottomHeight + "px",
				left: xoff + "px",
				top: (2.0*yoff- 2.0*height-bottomHeight + 1 ) + "px", 
				webkitTransform: "skewX(" + supAngleDeg + "deg)",
				transform: "skewX(" + supAngleDeg + "deg)",
				mozTransform: "skewX(" + supAngleDeg + "deg)",
				msTransform: "skewX(" + supAngleDeg + "deg)",
				oTransform: "skewX(" + supAngleDeg + "deg)"
			});
						
			elem.height(height+30);
			elem.width(width);
			//$("#base").css({webkitTransform: "scale(10,10)"})

		},

		// not much
		_refresh: function() { },


		// events bound via _bind are removed automatically
		// revert other modifications here
		_destroy: function() {
			// remove added elements
			
		},

		_setOptions: function() {
			$.Widget.prototype._setOptions.apply( this, arguments );
			this._refresh();
		},

		
		_setOption: function( key, value ) {
			
			// Test Validity of options
			
			$.Widget.prototype._setOption.call( this, key, value );
		}
	});
	
	
	// Decoration
	// $("#content-sidepane").borderContent();	
	