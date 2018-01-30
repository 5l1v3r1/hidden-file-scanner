import os,filetype
 
# Set the directory you want to start from
rootDir = '/home'
for dirName, subdirList, fileList in os.walk(rootDir):
    #print('Found directory: %s' % dirName)
    for fname in fileList:
        try:
           f=filetype.guess(dirName+'/'+fname)
        except IOError:
               pass
        if f is not None:
           if f.mime=='video/mp4':
              print "video found at",dirName,fname,f.mime,f.extension
