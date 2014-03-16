/**
 * @fileOverview The model describing a Crosswords board (and the tile pool).
 */
define([
  'backbone'
], function(Backbone) {
  "use strict";
  return Backbone.Model.extend({
    defaults: {
      board: null,
      tiles: null,
      dimension: 15
    }
  });
});