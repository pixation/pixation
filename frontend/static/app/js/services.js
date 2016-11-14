angular.module('pixation.services', [])
    .factory('dashboard', ["$location", "$http", "$log", "$q", function ($location, $http, $log, $q) {
        return {
            getUserFeed: function (page) {
                var deferred = $q.defer();
                var urlToUse = baseUrl + '/api/v1/images/getUserFeed/';
                console.log(urlToUse);
                $http.get(urlToUse).success(function (data) {
                    deferred.resolve(data);
                }).error(function (data) {
                    deferred.reject();
                });
                return deferred.promise;
            },
            getPublicFeed: function(page) {
              var deferred = $q.defer();
              var urlToUse = baseUrl + '/api/v1/images/getPublicFeed/';
              console.log(urlToUse);
              $http.get(urlToUse).success(function (data) {
                  deferred.resolve(data);
              }).error(function (data) {
                  deferred.reject();
              });
              return deferred.promise;
            }
        }
    }])
    .factory('upload', ["$location", "$http", "$log", "$q", function ($location, $http, $log, $q) {
        return {
            uploadImage: function (imageData) {
                var deferred = $q.defer();
                var urlToUse = baseUrl + '/api/v1/images/upload/';
                console.log($http);
                console.log(urlToUse);
                console.log(imageData);
                var fd = new FormData();
                fd.append('image', imageData.image);
                fd.append('public', imageData.public);
                fd.append('display_name', imageData.display_name);
                $http.post(urlToUse, fd, {
                    transformRequest: angular.identity,
                    headers: {'Content-Type': undefined}
                }).success(function (data) {
                    deferred.resolve(data);
                }).error(function (data) {
                    deferred.reject();
                });
                return deferred.promise;
            }
        }
    }])
    .factory('user', ["$location", "$http", "$log", "$q", function ($location, $http, $log, $q) {
        return {
            getUserDashboardImages: function () {
                var deferred = $q.defer();
                var urlToUse = baseUrl + '/api/v1/getUserDashboardImages';
                console.log(urlToUse);
                $http.get(urlToUse).success(function (data) {
                    deferred.resolve(data);
                }).error(function (data) {
                    deferred.reject();
                });
                return deferred.promise;
            },
            getTimeZoneByLatitudeLongitude: function (latitude, longitude) {
                var deferred = $q.defer();
                var urlToUse = 'https://maps.googleapis.com/maps/api/timezone/json?location=' + latitude + ',' + longitude + '&timestamp=' + (Math.floor((new Date().getTime()) / 1000));
                console.log(urlToUse);
                $http.get(urlToUse).success(function (data) {
                    deferred.resolve(data);
                }).error(function (data) {
                    deferred.reject();
                });
                return deferred.promise;

            },
            postPlace: function (placeJson) {
                var deferred = $q.defer();
                var urlToUse = baseUrl + '/api/v1/postData';
                console.log(urlToUse);
                $http.post(urlToUse, placeJson).success(function (data) {
                    deferred.resolve(data);
                }).error(function (data) {
                    deferred.reject();
                });
                return deferred.promise;
            }
        }

    }])
    .factory('image', ["$location", "$http", "$log", "$q", function ($location, $http, $log, $q) {
        return {
            imageAPI: function (data) {
                var deferred = $q.defer();
                var urlToUse = baseUrl + '/api/v1/getUserDashboardImages';
                console.log(data);
                $http.get(urlToUse, data).success(function (data) {
                    deferred.resolve(data);
                }).error(function (data) {
                    deferred.reject();
                });
                return deferred.promise;
            }
        }

    }]);
