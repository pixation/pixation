angular.module('pixation.controllers', ['pixation.services'])
.controller('dashboardController', ["$scope", "dashboard", function ($scope, dashboard) {
  $scope.userImages = [];
  $scope.pageUser = 1;
  $scope.pagePublic = 1;
  $scope.publicImages = [];
  $scope.userImages = [];
  $scope.showMoreUser = function() {
    dashboard.getUserFeed($scope.pageUser).then(function (data) {
      $scope.userImages.push(...data.results);
      $scope.pageUser++;
      console.log(data.results);
    }
  );
};
$scope.showMorePublic = function() {
  dashboard.getPublicFeed($scope.pagePublic).then(function (data) {
    $scope.publicImages.push(...data.results);
    $scope.pagePublic++;
    console.log(data.results);

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
.controller('imageController', ['$scope', 'image', function($scope, imageService) {
  $scope.editMode = false;
  $scope.data = [];
  $scope.model = {};
  $scope.model.option = 1;
  $scope.edit = function() {
    console.log('Im here');
    $scope.editMode = true;
  }
  var canvas = document.getElementById('canvas');
  var image = document.getElementById('image');
  var context = canvas.getContext('2d');
  $scope.submit = function() {
    if ($scope.model.option == 1) {
      // Handling Option 1
      if ($scope.model.height == null || $scope.model.width == null) {
        return;
      }
      imageService.imageAPIResize({image: image.src.substr(image.src.lastIndexOf("/")+1),
                            height: parseInt($scope.model.height),
                            width: parseInt($scope.model.width)})
            .then(function(data) {
          console.log(data);
      });
    }
    else if ($scope.model.option == 2) {
      console.log($scope.data);
      newData = []
      if ($scope.data.length < 3) {
        console.log('Too Short');
        return;
      }
      $scope.imgsrc = image.src;
      for (var i = 0; i < $scope.data.length; i++) {
        newData.push({x: $scope.data[i].x*($scope.naturalWidth/$scope.width)|0,
                      y: $scope.data[i].y*($scope.naturalHeight/$scope.height)|0});
      }
      console.log(newData);
      imageService.imageAPIRemoval({points: newData,
                                    image: image.src.substr(image.src.lastIndexOf("/")+1)})
                   .then(function(data) {
                      console.log(data);
      });
    }

  }
  $scope.doMouseDown = function(event) {
    if ($scope.model.option == 1) {
      $scope.clear();
      return;
    }
    console.log('Here')
    console.log(event)
    var event = event;
    $scope.x = event.layerX;
    $scope.y = event.layerY;
    $scope.addData();
    $scope.$apply();
  }
  angular.element(document).ready(function () {
    $scope.width = image.width;
    $scope.height = image.height;
    $scope.naturalWidth = image.naturalWidth;
    $scope.naturalHeight = image.naturalHeight;
    console.log();
    canvas.width = image.width;
    canvas.height = image.height;
    context.drawImage(image, 0,0, image.naturalWidth, image.naturalHeight, 0,0,image.width, image.height);
    canvas.addEventListener("click", $scope.doMouseDown, true);
    });
    $scope.clear = function() {
      context.drawImage(image, 0,0, $scope.naturalWidth, $scope.naturalHeight, 0,0,$scope.width, $scope.height);
      $scope.data = [];
    }


  $scope.data = [

  ];

  $scope.addData = function() {
    var id = 0;
    if($scope.data.length > 0) {
      id = $scope.data[$scope.data.length-1].id + 1;
    }
    $scope.amount = 5;

    var p = {id: id, x: $scope.x, y: $scope.y, amount: $scope.amount};
    $scope.data.push(p);
    // $scope.x = '';
    // $scope.y = '';
    draw($scope.data);
  };

  $scope.removePoint = function(point) {
    console.log(point);
    for(var i=0; i<$scope.data.length; i++) {
      if($scope.data[i].id === point.id) {
        console.log("removing item at position: "+i);
        $scope.data.splice(i, 1);
      }
    }

    context.clearRect(0,0,600,400);
    draw($scope.data);
    console.log($scope.data);
  }

  function draw(data) {
    for(var i=0; i<data.length; i++) {
      drawDot(data[i]);
      if(i > 0) {
        drawLine(data[i], data[i-1]);
      }
    }
  }

  function drawDot(data) {
    context.beginPath();
    context.arc(data.x, data.y, data.amount, 0, 2*Math.PI, false);
    context.fillStyle = "yellow";
    context.fill();
    context.lineWidth = 1;
    context.strokeStyle = "#666666";
    context.stroke();
  }

  function drawLine(data1, data2) {
    context.beginPath();
    context.moveTo(data1.x, data1.y);
    context.lineTo(data2.x, data2.y);
    context.strokeStyle = "green";
    context.lineWidth = 5;
    context.stroke();
  }

  draw($scope.data);
  $scope.$watch(function(scope) { return scope.editMode },
    function(newValue, oldValue) {
      if (newValue == true && oldValue == false) {

      }
    });
}]);
