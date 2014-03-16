/**
 * @fileOverview The main router for Crossword Game.
 */
define([
  'backbone'
], function(Backbone) {
  "use strict";
  return Backbone.Router.extend({
    routes: {
      'board-setup': 'newBoard'
    }
  });
});