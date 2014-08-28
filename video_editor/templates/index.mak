<html>
<head>
  <link rel="stylesheet" href="/static/bootstrap-3.2.0-dist/css/bootstrap.min.css">

  <script src="/static/jquery-1.11.1.min.js"></script>
  <script src="/static/bootstrap-3.2.0-dist/js/bootstrap.min.js"></script>

  <script>
    $(document).ready(function() {
        $("#go").click(function() {
          var startTime = $('#start-time').val();
          var endTime = $('#end-time').val();
          var videoPath = $('#video-path').val();
          if (! startTime || ! endTime) {
              return false;
          }

          $.getJSON("/thumbnails.json", {s: startTime, e:endTime, p:videoPath}, function( data ) {
            console.log('done', data);
            $.each(data.thumbnails_s, function() {
              $('#thumbnails-s').append($('<img>').attr('src', '/static/generated/' + this));
            });
            $.each(data.thumbnails_e, function() {
              $('#thumbnails-e').append($('<img>').attr('src', '/static/generated/' + this));
            });
          });
        })
    });

  </script>
</head>
<body>

  <video controls="true">
  <source src="http://x2frantastiquecom.a9english.com/static/Ne-Le-Dis-A-Personne-2.mp4">
  </video>

  <br />
  <br />
  <div class="form-group">
    <label>Video path</label>
    <input type="text" class="form-control" id="video-path" value="/home/lereskp/dev/github/video-editor/video_editor/static/test.webm" />
  </div>

  <div id="video-details-pane">
    ${details}
  </div>

  <div class="form-group">
    <label>Start time</label>
    <input type="text" class="form-control" id="start-time" value="2" />
  </div>
  
  <div id="thumbnails-s"></div>

  <div class="form-group">
    <label>End time</label>
    <input type="text" class="form-control" id="end-time" value="4" />
  </div>

  <div id="thumbnails-e"></div>

  <button id="go">Get thumbnails</button>


</body>
</html>
