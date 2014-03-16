define([
  'backbone',
  'jquery',
  'underscore',
  'router',
  'views/board_setup',
  'mustache',
  'text!templates/main_app.html'
], function(Backbone, $, _, Router, BoardSetup, Mustache, MainAppTemplate) {
  "use strict";
  var App;

  App = Backbone.View.extend({
    initialize: function(options) {
      // XXX: Backbone >= 1.1 doesn't auto-attach passed in options.
      this.boards = options.boards;
      this.boardSetupView = new BoardSetup({
        el: $('#options-modal')
      });
      this.router = new Router();
      this.router.on('route:newBoard', _.bind(this.setupNewBoard, this));
      Backbone.history.start({
        root: '/'
      });
      this.render();
    },
    render: function() {
      var context = {
        noBoards: false
      };
      if (_.size(this.boards) === 0) {
        context.noBoards = true;
      }
      this.$el.html(Mustache.render(MainAppTemplate, context));
      return this;
    },
    setupNewBoard: function() {
      console.log('setup new oard')
      this.boardSetupView.setup();
    }
  });
  return App;
});