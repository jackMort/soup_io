// packager build ScrollLoader/*
/*
---

name: Class.Binds

description: Alternate Class.Binds Implementation

authors: Scott Kyle (@appden), Christoph Pojer (@cpojer)

license: MIT-style license.

requires: [Core/Class, Core/Function]

provides: Class.Binds

...
*/

Class.Binds = new Class({

	$bound: {},

	bound: function(name){
		return this.$bound[name] ? this.$bound[name] : this.$bound[name] = this[name].bind(this);
	}

});

/*
---

name: ScrollLoader

description: Fires an event when the user reaches a certain boundary.

authors: Christoph Pojer (@cpojer)

license: MIT-style license.

requires: [Core/Events, Core/Options, Core/Element.Event, Core/Element.Dimension, Class-Extras/Class.Binds]

provides: ScrollLoader

...
*/

(function(){

this.ScrollLoader = new Class({
	
	Implements: [Options, Events, Class.Binds],
	
	options: {
		/*onScroll: fn,*/
		area: 50,
		mode: 'vertical',
		container: null
	},
	
	initialize: function(options){
		this.setOptions(options);
		
		this.element = document.id(this.options.container) || window;
		this.attach();
	},
	
	attach: function(){
		this.element.addEvent('scroll', this.bound('scroll'));
		return this;
	},
	
	detach: function(){
		this.element.removeEvent('scroll', this.bound('scroll'));
		return this;
	},
	
	scroll: function(){
		var z = (this.options.mode == 'vertical') ? 'y' : 'x';
		
		var element = this.element,
			size = element.getSize()[z],
			scroll = element.getScroll()[z],
			scrollSize = element.getScrollSize()[z];
		
		if (scroll + size < scrollSize - this.options.area) return;
		
		this.fireEvent('scroll');
	}
	
});

})();
