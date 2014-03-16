/**
 * @fileOverview The elements representing a crosswords board. Basically
 * the SVG.
 */
define([
  'backbone',
  'Raphaël'
], function(Backbone, Raphael) {
  "use strict";
  return Backbone.View.extend({
    initialize: function(options) {
      this.width = options.width;
      this.height = options.height;
      this.paper = Raphael(this.el, this.width, this.height);
    },
    render: function() {
      this.paper.rect(10, 10, this.width - 20, this.height - 20, 1);
    }
  });
});