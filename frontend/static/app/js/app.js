angular.module('pixation', ['pixation.controllers', 'pixation.services'])
    .config(["$httpProvider", function ($httpProvider) {

        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        // $httpProvider.defaults.headers.post['Accept'] = 'application/json, text/javascript';
        // $httpProvider.defaults.headers.post['Content-Type'] = 'multipart/form-data; charset=utf-8';

    }])
    .directive("fileModel", function () {
        return {
            restrict: 'EA',
            scope: {
                setFileData: "&"
            },
            link: function (scope, ele, attrs) {
                ele.on('change', function () {
                    scope.$apply(function () {
                        var val = ele[0].files[0];
                        scope.setFileData({value: val});
                    });
                });
            }
        }
    });