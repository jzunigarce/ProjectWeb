#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import sys
import wget
import zipfile

DS = os.sep

def main(template, name):
    path = os.getcwd() + DS
    dir = path + name
    try:
        if os.path.exists(dir):
            option = input("Does the directory already exists, you want to overwrite it?(s/n): ")
            if option.lower() == 'n':
                return
            shutil.rmtree(dir)
        os.makedirs(dir)
        os.chdir(dir)

    except Exception as e:
        print ("Unexpected error: %s" % e)
        return

    url = getURLTemplate(template)
    if url is None:
	    return 
    file = wget.download(url)
    extractFile(file, dir)
    print('%s %s' %(template, name))

def extractFile(file, path):
    fileType = file[-3:]
    try:
        if fileType.lower() == 'zip':
            with zipfile.ZipFile(file) as z:
                z.extractall(path)
        os.remove(path + DS + file)
    except Exception as e:
        print ("Failed to decompress file %s" % e)

def getURLTemplate(template):    
    if template == 'bootstrap':
        return 'https://github.com/twbs/bootstrap/releases/download/v3.1.1/bootstrap-3.1.1-dist.zip'
    else:
        return None
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Incorrect number of arguments")
    elif not isinstance(sys.argv[1], str) or len(sys.argv[1].strip()) == 0:
        print('Wrong template name')
    elif not isinstance(sys.argv[2], str) or len(sys.argv[2].strip()) == 0:
        print('Wrong project name')
    else:
        main(sys.argv[1].lower(), sys.argv[2])
