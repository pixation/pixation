angular.module('pixation.controllers', ['pixation.services'])
    .controller('dashboardController', ["$scope", "dashboard", function ($scope, dashboard) {
        $scope.userImages = [];

        dashboard.getUserDashboardImages().then(function (data) {
                $scope.userImages = data.data;
            }
        );
        console.log(baseUrl);

    }])
    .controller('uploadController', ["$scope", "upload", function ($scope, upload) {
        $scope.userImages = [];

        $scope.model = {public: false};
        $scope.upload = function () {
            upload.uploadImage($scope.model).then(function (data) {
                    if (data.image) {
                        window.location.href = data.image;
                    }
                    console.log(data);
                }
            );
        };

        console.log(baseUrl);

    }]);