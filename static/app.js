window.addEventListener('load', function() {
  var images = document.querySelectorAll('.image'); // Select all <img> elements
  var targetDivs = document.querySelectorAll('.target-div'); // Select all elements with 'data-target-div' attribute

  for (var i = 0; i < images.length; i++) {
    var image = images[i];
    var targetDiv = targetDivs[i];

    processImage(image, targetDiv);
  }
});

function processImage(image, targetDiv) {
  var canvas = document.createElement('canvas');
  var context = canvas.getContext('2d');

  canvas.width = image.width;
  canvas.height = image.height;
  context.drawImage(image, 0, 0, canvas.width, canvas.height);
  var imageData = context.getImageData(0, 0, canvas.width, canvas.height).data;
  var colorFrequencies = {};

  for (var i = 0; i < imageData.length; i += 4) {
    var r = imageData[i];
    var g = imageData[i + 1];
    var b = imageData[i + 2];
    var rgb = 'rgb(' + r + ', ' + g + ', ' + b + ')';

    if (colorFrequencies[rgb]) {
      colorFrequencies[rgb]++;
    } else {
      colorFrequencies[rgb] = 1;
    }
  }

  var majorityColor = getMajorityColor(colorFrequencies);
  var lighterColor = tinycolor(majorityColor).lighten(10).toString();
  targetDiv.style.backgroundColor = lighterColor;
}

function getMajorityColor(colorFrequencies) {
  var maxFrequency = 0;
  var majorityColor = '';

  for (var color in colorFrequencies) {
    if (colorFrequencies[color] > maxFrequency) {
      maxFrequency = colorFrequencies[color];
      majorityColor = color;
    }
  }

  return majorityColor;
}

