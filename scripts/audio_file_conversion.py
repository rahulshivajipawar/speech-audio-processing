import librosa
import ffmpeg
import sys
import os
import pathlib
import shutil

"""
The following script takes in two inputs /path/to/source/ and /path/to/destination. It converts audio_files present (in any format) in the
source directory and converts them into .wav files with 16-bit PCM encoded .wav files

Usage:

    audio_file_file_conversion.py /path/to/source/ /path/to/destination
"""

source_dir = sys.argv[1] # Path to Source directory
dest_dir = sys.argv[2]  # Path to Destination directory

if os.path.isdir(dest_dir) is False:
    os.mkdir(dest_dir)

acceptable_input_file_formats = [".mpg",".mpeg",".mp1",".mp2",".mp3",".mlv",".m1a",".m2a",".mpa",".mpv",".m4a",".mp4",".3gp",".m4b",".m4p", \
    ".m4r",".m4v",".aac",".flac",".wav"]

input_files_list = [] # List of audio files in the source directory which are of the acceptable input file format.

source_dir_pathlib_obj = pathlib.Path(source_dir) # works only for >= Python 3.5

for format in acceptable_input_file_formats:
    searched_files = [str(file) for file in sorted(source_dir_acceptable_input.rglob("*"+format))]
    input_files_list.extend(searched_files)

for file in input_files_list:
    file_pathlib_obj = pathlib.Path(file)
    audio_header = ffmpeg.probe(file)
    output_file = dest_dir.strip('/') + '/' + file_pathlib_obj.name.split('.')[0] + '.wav'
    if audio_header['streams'][0]['codec_name'] is not "pcm_s16le":
        ffmpeg.input(file).output(output_file, acodec = 'pcm_s16le')
    else:
        shutil.copyfile(file,output_file)
