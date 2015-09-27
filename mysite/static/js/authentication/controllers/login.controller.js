/**
* LoginController
* @namespace thinkster.authentication.controllers
*/
(function () {
  'use strict';

  angular
    .module('thinkster.authentication.controllers')
    .controller('LoginController', LoginController);

  LoginController.$inject = ['$location', '$scope', 'Authentication'];

  /**
  * @namespace LoginController
  */
  function LoginController($location, $scope, Authentication) {
    var vm = this;
    var registrationForm = $('.ui.form.login');
    var errorForm = $('.ui.login.error');

    //semantic validation rules and parameters
    (function ($) {
    registrationForm.form({  
        on: 'blur',
        fields: {     
          email: {
            identifier: 'Email',
            rules: [{
              type: 'empty',
              prompt: 'Por favor ingrese su correo electrónico'
            },{
              type: 'email',
              prompt: 'Por favor ingrese un correo electrónico válido'
            }]
          },       
          password: {
            identifier: 'Password',
            rules: [{
              type: 'empty',
              prompt: 'Por favor ingrese su contraseña'
            },{
              type: 'length[6]',
              prompt: 'La contraseña debe tener al menos 6 caracteres'
            }]
          }
        }
      });
    }(jQuery));

    vm.login = login;

    activate();

    /**
    * @name activate
    * @desc Actions to be performed when this controller is instantiated
    * @memberOf thinkster.authentication.controllers.LoginController
    */
    function activate() {
      // If the user is authenticated, they should not be here.
      if (Authentication.isAuthenticated()) {
        $location.url('/');
      }
    }

    /**
    * @name login
    * @desc Log the user in
    * @memberOf thinkster.authentication.controllers.LoginController
    */
    function login() {
      if(!registrationForm.form('validate form')){
        console.log("it's a pitty");
        return;}
      //var auth = Authentication.login(vm.login.email, vm.login.password);
      var err;
      Authentication.login(vm.login.email, vm.login.password)
        .success(loginSuccessFn)
        .error(loginErrFn);

      function loginSuccessFn(data, status, headers, config) {
        Authentication.setAuthenticatedAccount(data.data);
        window.location = '/';
      }
      function loginErrFn(data, status, headers, config) {
        registrationForm.form('add errors', [ data.message ]);
        errorForm.show();
      }

      //console.log("login controller");
      //console.log(auth);
      //console.log($scope.myData);

      //console.log("::::::::::");
    }
  }
})();