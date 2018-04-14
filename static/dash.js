/*dash board*/

var app = angular.module("NamazuDash", ['ngRoute', 'ngCookies','angular-flot']);

app.factory('tokenInterceptor', function($cookies) {
  var headerName = "Authorization";
  var cookieName = "token";

  return {
    request: function(config) {
      config.headers = config.headers || {};
      console.log($cookies.get('token'));
      if ($cookies.get('token')) {
        config.headers["Authorization"] = 'Token ' + $cookies.get('token');
      }
      return config;
    },
    responseError: function (response) {
      location.href='/#/signin';
    }}});

app.controller('DashLogoutController',
function DashLogout($scope,$http,$cookies,$location,$route)
{
    $scope.logout = function()
    {
        $cookies.remove('token'); 
        $route.reload();
    };
}
);




app.controller('FlotCtrl', ['$scope','$http','$interval', function ($scope,$http,$interval) {
  $scope.ok1 = null;
  $scope.ok2 = null;
  $scope.ok3 = null;
  $scope.options1 = {
    legend: {
      container: '#legend1',
      show: true
    },
yaxis: {
				ticks: 10,
				min: -1.5,
				max: 1.5,
				tickDecimals: 3
			}
  };

$scope.options2 = {
    legend: {
      container: '#legend2',
      show: true
    },
yaxis: {
				ticks: 10,
				min: -0.5,
				max: 0.5,
				tickDecimals: 3
			}
  };
$scope.options3 = {
    legend: {
      container: '#legend3',
      show: true
    },
yaxis: {
				ticks: 10,
				min: -0.5,
				max: 0.5,
				tickDecimals: 3
			}
  };
	$scope.func = function()
         {

	$http({method: 'GET', url: '/api/components/1/'}).then(function(response1)
	{
		$scope.ok1 = response1.data;
		$http({method: 'GET', url: '/api/components/2/'}).then(function(response2)
		{
			$scope.ok2 = response2.data;
			$http({method: 'GET', url: '/api/components/3/'}).then(function(response3)
			{
			$scope.ok3 = response3.data;
			$scope.dataset1 = [{ data: [], yaxis: 1, label: 'X1' },{ data: [], yaxis: 1, label: 'X2' },{ data: [], yaxis: 1, label: 'X3'}];
			$scope.dataset2 = [{ data: [], yaxis: 1, label: 'Y1' },{ data: [], yaxis: 1, label: 'Y2' },{ data: [], yaxis: 1, label: 'Y3' }];
			$scope.dataset3 = [{ data: [], yaxis: 1, label: 'Z1' },{ data: [], yaxis: 1, label: 'Z2' },{ data: [], yaxis: 1, label: 'Z3' }];
			 for (var i = 0; i < 10; i += 1) {
		    		$scope.dataset1[0].data.push([i, $scope.ok1.results[i].XValue]);
				$scope.dataset1[1].data.push([i, $scope.ok2.results[i].XValue]);
				$scope.dataset1[2].data.push([i, $scope.ok3.results[i].XValue]);

				$scope.dataset2[0].data.push([i, $scope.ok1.results[i].YValue]);
				$scope.dataset2[1].data.push([i, $scope.ok2.results[i].YValue]);
				$scope.dataset2[2].data.push([i, $scope.ok3.results[i].YValue]);

				$scope.dataset3[0].data.push([i, $scope.ok1.results[i].ZValue]);
				$scope.dataset3[1].data.push([i, $scope.ok2.results[i].ZValue]);
				$scope.dataset3[2].data.push([i, $scope.ok3.results[i].ZValue]);

			  }
			});
		});
	});
       };
	$interval($scope.func,100);
 
}]);
  



app.controller('MainDashboardBuildings',
function MainDashboard($scope,$http)
{
    $scope.buildings = null;
    $http(
          {
              method: 'GET',
              url: '/api/buildings/'
          }
    ).then(function(response){
        $scope.buildings = response.data;       
    });
});


app.controller('NodeDashController',
               function ResultDash($scope,$http,$routeParams)
    {
        $scope.id = $routeParams.id;
        $scope.node = null;
        $http({
            method: 'GET',
            url:'/api/node/'+$scope.Searchterm
        }).then(function(response)
                {
                    $scope.node = response.data;
                }
        );
    }
);



app.config(function ($httpProvider) {
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';
   $httpProvider.interceptors.push('tokenInterceptor'); 
});

app.config(function($routeProvider) {
    $routeProvider
    .when("/", {
        templateUrl : "/static/templates/dash/index.html",
    })
    .when("/node/:id", {
        templateUrl : "/static/templates/dash/node.html",
    });
});
