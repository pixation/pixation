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
    .factory('developer', ["$location", "$http", "$log", "$q", function ($location, $http, $log, $q) {
        return {
            becomeDeveloper: function () {
              var deferred = $q.defer();
              var urlToUse = baseUrl + '/api/v1/developer/makeDeveloper/';
              console.log(urlToUse);
              $http.post(urlToUse).success(function (data) {
                  deferred.resolve(data);
              }).error(function (data) {
                  deferred.reject();
              });
              return deferred.promise;
            },
            getKeys: function () {
              var deferred = $q.defer();
              var urlToUse = baseUrl + '/api/v1/developer/getkeys/';
              console.log(urlToUse);
              $http.get(urlToUse).success(function (data) {
                  deferred.resolve(data);
              }).error(function (data) {
                  deferred.reject();
              });
              return deferred.promise;
            },
            addKey: function (data) {
              var deferred = $q.defer();
              var urlToUse = baseUrl + '/api/v1/developer/makekey/';
              console.log(urlToUse);
              $http.post(urlToUse, data).success(function (data) {
                  deferred.resolve(data);
              }).error(function (data) {
                  deferred.reject();
              });
              return deferred.promise;
            },
            refreshKey: function (data) {
              var deferred = $q.defer();
              var urlToUse = baseUrl + '/api/v1/developer/makeDeveloper/';
              console.log(urlToUse);
              $http.post(urlToUse).success(function (data) {
                  deferred.resolve(data);
              }).error(function (data) {
                  deferred.reject();
              });
              return deferred.promise;
            },
            deleteKey: function (data) {
              var deferred = $q.defer();
              var urlToUse = baseUrl + '/api/v1/developer/makeDeveloper/';
              console.log(urlToUse);
              $http.post(urlToUse).success(function (data) {
                  deferred.resolve(data);
              }).error(function (data) {
                  deferred.reject();
              });
              return deferred.promise;
            },
            modifySources: function (data) {
              var deferred = $q.defer();
              var urlToUse = baseUrl + '/api/v1/developer/makeDeveloper/';
              console.log(urlToUse);
              $http.post(urlToUse).success(function (data) {
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
            imageAPIResize: function (data) {
                var deferred = $q.defer();
                var urlToUse = baseUrl + '/api/v1/resize';
                console.log(data);
                $http.post(urlToUse, data).success(function (data) {
                    deferred.resolve(data);
                }).error(function (data) {
                    deferred.reject();
                });
                return deferred.promise;
            },
            imageAPIRemoval: function (data) {
                var deferred = $q.defer();
                var urlToUse = baseUrl + '/api/v1/remove';
                console.log(data);
                $http.post(urlToUse, data).success(function (data) {
                    deferred.resolve(data);
                }).error(function (data) {
                    deferred.reject();
                });
                return deferred.promise;
            }
        }

    }]);
