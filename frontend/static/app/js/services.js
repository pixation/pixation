angular.module('pixation.services', [])
    .factory('dashboard', ["$location", "$http", "$log", "$q", function ($location, $http, $log, $q) {
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

    }]);
;