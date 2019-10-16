from flask import Flask
from flask import render_template
from flask import flash

# import object holding app-specific configuration
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


lat = -26.527
lon = 153.087
zoom = 13

my_lat_str = str(lat)
my_lon_str = str(lon)
my_zoom_str = str(zoom)


def entry_render(
    link: str,
    title: str = " ",
    salutation: str = "Friend",
    lat_str: str = '0.0',
    lon_str: str = '0.0',
    zoom_str: str = '13',
):
    '''
    entry_render: render Flask template, to display map

    The Leaflet and Mapbox Javascript is different, so a different
    template is used for each. However they all take the same parameters

    Parameters:
    link: str holding the name of the Flask template to be rendered
    title: str holding HTML title to be included in generated HTML
    salutation: str holding greeting displayed to user
    lat_str: str holding latitude of center of map
    lon_str: str holding longitude of center of map
    zoom_str: str holding the zoom level for map

    Returns:
    whatever render_template returns (str holding HTML?)

    Side Effects:
    creates page to be displayed in browser via Flask @app.route
    '''
    return render_template(
        link,
        title=title,
        salutation=salutation,
        lat_str=lat_str,
        lon_str=lon_str,
        zoom_str=zoom_str,
    )


# end entry_render


@app.route('/')
def hello():

    # entry from url
    return entry_render(
        link='index.html',
        title='Web Mapping Example',
        salutation='Buddy',
        lat_str=my_lat_str,
        lon_str=my_lon_str,
        zoom_str=my_zoom_str,
    )


# end index


@app.route('/index')
def index():
    # back to initial screen via Leaflet menu choice
    flash('Leaflet request seen')
    return entry_render(
        'index.html',
        title='Web Mapping Example',
        salutation='Chum',
        lat_str=my_lat_str,
        lon_str=my_lon_str,
        zoom_str=my_zoom_str,
    )


# end index


@app.route('/mapboxmap')
def mapboxmap():
    # back to initial screen via Mapbox menu choice
    flash('Mapbox request seen')
    return entry_render(
        'mapboxmap.html',
        title='Web Mapbox Example',
        salutation='Friend',
        lat_str=my_lat_str,
        lon_str=my_lon_str,
        zoom_str=my_zoom_str,
    )


# end mapboxmap


if __name__ == "__main__":
    app.run()
# end if

