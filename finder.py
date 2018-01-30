# coding: UTF-8
import os,filetype
import optparse
import sys
parser = optparse.OptionParser()
parser.add_option('-t', '--filetype',
                  dest="filetype",
                  default="mp4",
                  action="store",
                  )
options, args = parser.parse_args()
# Set the directory you want to start from
rootDir = '/home'
#t=raw_input("Please enter a file type to find : ")
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        try:
           f=filetype.guess(dirName+'/'+fname)
        except IOError:
               pass
        if f is not None:
           if f.extension==options.filetype:
              print "{} video found at".format(f.extension),dirName,fname,f.mime
