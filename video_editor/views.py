from pyramid.view import view_config
from . import ffmpeg


@view_config(route_name='home', renderer='index.mak')
def my_view(request):
    path = "/home/lereskp/dev/github/video-editor/video_editor/static/test.webm"
    details = ffmpeg.get_details(path)
    return {'project': 'video_editor', 'details': details}


@view_config(route_name="thumbnails", renderer='json')
def func(request):
    p = request.GET.get('p')
    s = int(request.GET.get('s'))
    e = int(request.GET.get('e'))
    s_files = ffmpeg.generate_thumbnails(p, s, 'start')
    e_files = ffmpeg.generate_thumbnails(p, e, 'end')

    return {
        'thumbnails_s': s_files,
        'thumbnails_e': e_files,
    }
