import moviepy.editor as mpy

def adjust_video(inp_file:str, out_file:str):
    '''
    :param inp_file: filepath for input file
    :param out_file: filepath for output file
    :return:
    '''
    assert inp_file, "Need an input path for file"
    assert out_file, "Need an output path for file"
    video = mpy.VideoFileClip(inp_file)
    # first subtract from sides to make it ideal height width ratio
    # with my resolution 2560x1440 we need the width/height ratio to either be:
    #   square or 720/1280 ~ aprox 0.5625
    # to do this we subtract 875 from both sides of the width
    video = video.crop(x1=875, y1=0, x2=2560-875, y2=1440)
    # then resize to usable resolution for shorts
    # since we want 1280x720 we resize the width from its current(810) to 720
    video = video.resize(width=720)
    video.write_videofile(out_file,fps=30)


if __name__ == '__main__':
    inp_file = input('insert filename from turn_into_shorts folder:')
    out_file = input('insert filename to output into shorts folder:')
    if not out_file:
        out_file = inp_file
    adjust_video("turn_into_shorts/"+inp_file, "shorts/"+out_file)

