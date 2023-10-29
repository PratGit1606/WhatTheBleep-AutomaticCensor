from moviepy.editor import *
import assemblyai as aai
from functools import cache
import time
start = time.time()

aai.settings.api_key = f"d0f62ca6535b41af888b70dcac976f9e"



def custom_words():
    f_words = open("bad_words.txt","a")
    c_words = open("customwords.txt", "r")
    custom_word = c_words.readlines()
    f_words.writelines(custom_word)
    c_words.close()
    f_words.close()
    print(time.time()-start)

def video_to_audio(video_file):
    clip = VideoFileClip(video_file)
    clip.audio.write_audiofile("result.wav")
    print(time.time()-start)


def audio_to_transcript():
    transcript = aai.Transcriber().transcribe("result.wav")
    subtitles = transcript.export_subtitles_vtt(chars_per_caption=15)
    f = open("subtitles.vtt","w")
    f.write(subtitles)
    f.close()
    print(time.time()-start)


def strip_content_newline(content):
    for i, line in enumerate(content):
        if line == "\n":
            content.pop(i)
        else:
            content[i] = line[0:int(len(line)-1)]
    return content


def censored_words_timestamps(content, words, timing):
    start = '00:00:00.00'
    for i, line in enumerate(content):
        for w in words:
            if w.lower() in line.lower():
                middle= '00:'+content[i-1][0:8]
                end = "00:"+content[i-1][14:22]
                timing.append((start, middle))
                timing.append((middle,end))
                start = end
                content[i]=content[i].replace(w, (" "+("*"*(len(w)-1))))
    return timing, content

def transcript_censor():
    f = open("subtitles.vtt","r")
    f.readline()
    content = f.readlines()
    content = strip_content_newline(content)
    f.close()

    #opening bad_words file
    f_words = open("bad_words.txt","r")
    bad_words = strip_content_newline(f_words.readlines())
    f_words.close()

    #censoring words
    timings = list()
    timings , content= censored_words_timestamps(content, bad_words, timings) 

    return timings  

def subclips_audio_redact(timings,video):
    video_file = VideoFileClip(video)
    subclips=list()
    for i, tup in enumerate(timings):
        if (i%2!=0):
            subclip = video_file.subclip(tup[0],tup[1])
            subclip = subclip.set_audio(None)
            subclips.append(subclip)
        else:
            subclip = video_file.subclip(tup[0],tup[1])
            subclips.append(subclip)
    return subclips


def final_video_construct(subclips):
    final_video = concatenate_videoclips(subclips)
    final_video.write_videofile("/Users/pratham/VideoCensor/assets/censoredvideo.mp4")

def run():
    video_to_audio("/Users/pratham/VideoCensor/.web/public/Test.mp4")
    audio_to_transcript()
    timings = transcript_censor()
    subclips = subclips_audio_redact(timings, "/Users/pratham/VideoCensor/.web/public/Test.mp4")
    final_video_construct(subclips)

    print(time.time()-start)