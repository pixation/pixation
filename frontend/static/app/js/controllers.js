angular.module('pixation.controllers', ['pixation.services'])
    .controller('dashboardController', ["$scope", "dashboard", function ($scope, dashboard) {
        $scope.userImages = [];
        $scope.pageUser = 1;
        $scope.pagePublic = 1;
        $scope.publicImages = [];
        $scope.userImages = [];
        $scope.showMoreUser = function() {
          dashboard.getUserFeed($scope.pageUser).then(function (data) {
                  $scope.userImages.push(data.data);
                  $scope.pageUser++;
              }
          );
        };
        $scope.showMorePublic = function() {
          dashboard.getPublicFeed($scope.pagePublic).then(function (data) {
                  $scope.publicImages.push(data.data);
                  $scope.pagePublic++;
              }
          );
        };
        $scope.showMoreUser();
        $scope.showMorePublic();

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

    }])
    .controller('imageController', ['$scope', 'upload', function($scope, upload) {
      $scope.edit = function() {
        console.log('Im here');
      }
    }]);
