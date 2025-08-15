function eventRecorder() {
  var eventRecorder = document.createElement('div');
  eventRecorder.innerHTML = '<button id="start">Start</button><button id="stop">Stop</button><button id="play">Play</button><button id="clear">Clear</button>';
  document.body.appendChild(eventRecorder);
  var start = document.getElementById('start');
  var stop = document.getElementById('stop');
  var play = document.getElementById('play');
  var clear = document.getElementById('clear');
  var events = [];
  var timer;
  stop.addEventListener('click', function() {
    clearInterval(timer);
  });
  play.addEventListener('click', function() {
    var i = 0;
    var timer = setInterval(function() {
      if (i < events.length) {
        document.dispatchEvent(events[i]);
        alert(events[i]);
        i++;
      } else {
        clearInterval(timer);
      }
    }, 1000);
  });
  clear.addEventListener('click', function() {
    events = [];
  });
}
