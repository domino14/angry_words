/* global requirejs,define */
requirejs.config({
  baseUrl: '/static/js/base',
  /*
   * Due to Django's style of having static directories per app, and because
   * our libs live in the djAerolith/static directory, we must append this
   * ugly path to every library file in order for the optimizer (r.js) to
   * work properly.
   */
  paths: {
    jquery: '../../../../static/lib/jquery-1.11.0',
    bootstrap: '../../../../static/lib/bootstrap/js/bootstrap',
    underscore: '../../../../static/lib/underscore-1.4.4',
    csrfAjax: '../../../../static/js/common/csrf_ajax',
    Raphaël: '../../../../static/lib/raphael',
    mustache: '../../../../static/lib/mustache',
    text: '../../../../static/lib/require/text',
    backbone: '../../../../static/lib/backbone-1.0.0'
  },
  shim: {
    underscore: {
      exports: '_'
    },
    bootstrap: {
      deps: ['jquery'],
      exports: '$.fn.modal'
    },
    backbone: {
      deps: ['underscore', 'jquery'],
      exports: 'Backbone'
    }
  }
});

define([
  'module',
  'jquery',
  'views/app'
], function (module, $, App) {
  "use strict";
  $(function() {
    var app;
    app = new App({
      el: $('#app-view'),
      boards: JSON.parse(module.config().boards)
    });


  });
});