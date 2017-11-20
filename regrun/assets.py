from flask_assets import Bundle, Environment

# Bundle all css assets
css_all = Bundle("css/bootstrap.css",
                 "css/bootstrap-responsive.css",
                 "css/canary.css",
                 "css/jquery-ui.css",
                 "css/rickshaw.min.css",
                 filters="cssmin",
                 output="css/all.css")

# Bundle all js assets
js_vendor = Bundle(
    "js/jquery.min.js",
    "js/bootstrap.min.js",
    "js/socketio/socket.io.min.js",
    "js/canary.js",
    output="js/vendor.js")

assets = Environment()
assets.register('css', css_all)
assets.register('js_vendor', js_vendor)
