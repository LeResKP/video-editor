import os
from subprocess import Popen, PIPE                                              
import json
import math


def get_details(path):
    cmd = 'ffprobe -v quiet -print_format json -show_format -show_streams "%s"' % path
    p = Popen(cmd, shell=True, stdout=PIPE)
    s = p.stdout.read()
    # print video, s
    dic = json.loads(s)

    # TODO: We should be able to get only the video stream with ffprobe
    stream = dic['streams'][0]
    if stream['codec_type'] != 'video':
        stream = dic['streams'][1]

    output = {
        'duration': dic['format']['duration'],
        'r_frame_rate': stream['r_frame_rate'],
        'nb_frames':  int(math.ceil(float(dic['format']['duration']) * float(stream['r_frame_rate'].split('/')[0]))),
    }
    return output


def generate_thumbnails(path, time, name):
    filename = os.path.basename(path)
    cmd = 'ffmpeg -ss %s -i %s -s 200x100 -vframes 50 -y /tmp/video_editor/%s-%s-%%3d.png' % (time - 1, path, filename, name)
    print cmd
    p = Popen(cmd, shell=True, stdout=PIPE)
    s = p.stdout.read()
    files = []
    n = '%s-%s-%%03d.png' % (filename, name)
    for i in range(0, 50):
        files += [n % (i+1)]
    print s
    return files
