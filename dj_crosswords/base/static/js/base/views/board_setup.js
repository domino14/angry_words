/**
 * @fileOverview A board setup view.
 */
define([
  'backbone',
  'jquery',
  'views/board_view',
  'models/board',
  'bootstrap'
], function(Backbone, $, BoardView, Board) {
  "use strict";
  return Backbone.View.extend({
    initialize: function() {
      this.board = new Board();
      this.boardView = new BoardView({
        model: this.board,
        width: 400,
        height: 400,
        el: this.$('.modal-body')
      });
    },
    setup: function() {
      this.render();
      // Make the modal visible.
      this.$el.modal();
    },
    // Render the board setup view.
    render: function() {
      this.boardView.render();
    }
  });
});