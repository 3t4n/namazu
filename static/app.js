var app = angular.module("NamazuApp", ['ngRoute', 'ngCookies']);



app.config(function ($httpProvider) {
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
});



app.controller('SignInController',
               function SignInController($scope,$http,$location,$window, $cookies)
               {
                   $scope.username="";
                   $scope.password="";
                   $scope.token = null;
                   $scope.SignIn = function()
                   {
                       $http({
                           method: 'POST',
                           url: '/api/auth/login',
                           data: "username="+$scope.username+"&password="+$scope.password
                       }).then(function(response){
                           $scope.token = response.data.auth_token;
                           $cookies.put('token', $scope.token);
                           location.href = '/dashboard';
                       });

                   }
               }

);

app.controller('SignUpController',
               function SignUpController($scope,$http,$location)
               {
                   $scope.username="";
                   $scope.email="";
                   $scope.Nombre="";
                   $scope.Apellidos="";
                   $scope.Password1="";
                   $scope.Password2="";
                   $scope.SignUp = function()
                   {    
                       $http({
                           method: 'POST',
                           url: '/api/auth/register/',
                           data: "username=" + $scope.username + "&first_name="+$scope.Apellidos+"&last_name="+$scope.Apellidos+"&email="+$scope.email+"&password="+$scope.Password1}).then(function(response){
                               $location.url('/success');
                           });

                   }
               }

);


app.config(function($routeProvider) {
    $routeProvider
    .when("/", {
        templateUrl : "static/templates/signin.html"
    })
    .when("/signup", {
        templateUrl : "static/templates/signup.html",
        controller: 'SignUpController'
    })

    .when("/success",
          {
              templateUrl : "static/templates/success.html",
          }
    )

    .when("/signin", {
        templateUrl : "static/templates/signin.html",
        controller: 'SignInController'
    });
});

