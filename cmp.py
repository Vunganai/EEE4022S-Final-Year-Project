from fileinput import filename
import ffmpy

def compressvideo(fname):
    input_name = fname
    crf = 24 #crf can range from 18 to 24 with 24 being the greatest level of compression
    output_name = "output4_5.mp4"
    inp={input_name:None}
    outp = {output_name:'-vcodec libx264 -crf %d'%crf}
    ff=ffmpy.FFmpeg(executable='C:\\FFmpeg\\bin\\ffmpeg.exe', inputs=inp,outputs=outp)
    #print(ff.cmd) # just to verify that it produces the correct ffmpeg command
    ff.run()
    print('done!')

compressvideo("test1.mp4")

