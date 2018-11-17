#!/usr/bin/python
import os
import argparse
import sys
import commands
import re

VERBOSITY = 1

def _log(priority, msg, filename=None):
    if priority <= VERBOSITY:
        print(msg)
        if filename:
            with open(filename, 'a') as fp: 
                fp.write(msg + '\n')

def parse(args):
    parser = argparse.ArgumentParser("Convert video file to audio")
    parser.add_argument("-i", dest="input", action="store", help="input file")
    parser.add_argument("-o", dest="output", action="store", help="output file")
    parser.add_argument("-b", dest="bitrate", action="store", default=128, help="bitrate")
    parser.add_argument("-u", dest="url", action="store", help="URL")
    return parser.parse_args()

def scrape(searchString):
    ##[download] Destination: 
    #pat = re.compile(r'(?:Destination:).*')
    #pat = r'(?:\[ffmpeg\] Merging formats into ).*'
    pat = r'(?<=\[ffmpeg\] Merging formats into {1}).*'
    compiled = re.compile(pat)
    res = re.search(compiled, searchString)
    #retVal = res.group().split(":")[-1].strip()
    potentials = res.group().split('"')
    for p in potentials:
        if '[ffmpeg]' not in p and p:
            retVal = p
    _log(1, 'scraped: {}'.format(retVal))
    return retVal

def ytDL(url):
    dlFilePath = ""
    """%(title)s-%(id)s.%(ext)s"""
    ##ytCmd = "youtube-dl " + url
    ytCmd = "youtube-dl -o \'%(title)s.%(ext)s\' " + url
    _log(1, 'ytCmd: {}'.format(ytCmd))
    #import subprocess
    #p = subprocess.Popen(ytCmd, stdout=subprocess.PIPE)
    #_log(1, p.communicate())

    ytOutput = commands.getoutput(ytCmd)
    _log(1, 'ytOutput: {}'.format(ytOutput))
    ytResultFile = scrape(ytOutput)
    _log(1, 'ytResultsFile: {}'.format(ytResultFile))
    return ytResultFile

def videoToAudio(inputFile, outputFile, bitrate):
    cmd = "ffmpeg -i "
    return outputFile

def convert(args):
    results = parse(args)
    cmd = "ffmpeg -i "
    inputFile = ""
    bitrateText = ""
    outputFile = ""

    if results.url:
        _log(1, 'results.url: {}'.format(results.url))
        inputFile = ytDL(results.url)
    else:
        if results.input:
            inputFile = results.input

    if results.output:
        outputFile = os.path.splitext(results.output)[0] + ".mp3"
    else:
	outputFile = inputFile.strip()
	outputFile = outputFile.title()
	remove_chars = ['(',')','\'','"','!','?','~','&','*','$','%','@','#','+','=','{','}','[',']', ',']
	replace_chars = {'-':'_'}
	remove_words = ['official', 'Official', 'video', 'Video', 'lyrics', 'Lyrics']
	for tc in remove_chars:
	    outputFile = outputFile.replace(tc, '')
	for tc in replace_chars:
	    outputFile = outputFile.replace(tc, replace_chars[tc])
	for item in remove_words:
            outputFile = outputFile.replace(item, '')
	outputFile = outputFile.title()
	outputFile = outputFile.replace(' ', '')
        outputFile = os.path.expanduser('~/mp4s/{}.mp3'.format(os.path.splitext(outputFile)[0]))
        #outputFile = os.path.splitext(inputFile)[0] + ".mp3"

    if results.bitrate == "variable":
        bitrateText = " -q:a 0 -map a "
    else:
        bitrateText = " -b:a " + str(results.bitrate) + "K -vn "

    cmd = cmd + "\"" + inputFile + "\"" + bitrateText + "\"" + outputFile + "\""
    _log(1, 'cmd: {}'.format(cmd))

    if os.path.exists(inputFile):
        ffResults = commands.getoutput(cmd)
	os.remove(inputFile)
    else:
        _log(1, 'inputFile: {}'.format(inputFile))
        _log(1, "inputFile doesn't exist")

if __name__ == "__main__":
    convert(sys.argv)
