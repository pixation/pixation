angular.module('pixation.controllers', ['pixation.services'])
    .controller('dashboardController', ["$scope", "dashboard", function ($scope, dashboard) {
        $scope.userImages = [];
        dashboard.getUserDashboardImages().then(function (data) {
            $scope.userImages = data.data;
            }
        );
        console.log(baseUrl);
        
    }]);