import os.path
import os
import cPickle
import time
from scipy.io import mmwrite
from scipy.io import mmread

def writeOutTxt(dir,filename,text,mode='w'):

    """
    Simple function for creating a directory (if it does not exsist) and
    writing a file to it.

    The mode-parameter is set to 'w' (or 'write') by default and overwrites any
    existing file with the same name. For appending text, use 'a' in the
    optional mode-parameter.

    The directory is created in the home folder of the workstation.
    """

    string=str(text)

    if not os.path.isdir(dir):
        os.mkdir(dir)

    filepath=dir+'/'+filename+'.txt'
    print filepath
    out = file(filepath,mode)
    out.write(string)
    out.close()

def pickleOut(dirname, filename, fileext, object):
# writeOut Term Document Matrix
# Where object = (Matrix, TermList, PmidList)

# Actually object do not need to look like that, the object just needs
# to be pickleable

    """
    Simple function for writing a term document matrix, and its
    associated term list and pmid list. It writes to a dirname and a
    filename, is these do not exists it creates them. If they do
    exists it simply overwrites the file.

    The directory is created in the $HOME directory of the user on the
    work station.

    The format is pythons seriaized object via the pickle module.
    """

    if not os.path.isdir(dirname):
        os.mkdir(dirname)

    filepath=dirname+'/'+filename+'.'+fileext
    print filepath
    fd = open(filepath,'w')
    cPickle.dump(object,fd)
    fd.close()

def pickleIn(dirname, filename):

    """
    Loads a pickled object. Remember to include file extension in the
    filename. E.g. pickleIn('.../medline_records', 'diseaseHash.hash')
    """

    return cPickle.load(open(dirname+"/"+filename+'.pcl'))


def writeOutTDM(dirname, filename, matrix, type='numpy.float32'):

    """
    Receives a (full) directory name and a filename, a matrix and optional type,
    which is defined by numpy, and is e.g. numpy.float32, numpy.integer etc.
    
    Uses mmwrite to write out matrices, saving them in Matrix Market
    format which saves a lot of space 
    """
    
    if not os.path.isdir(dirname):
        os.mkdir(dirname)

    filepath=dirname+'/'+filename # binary term document matrix
    print filepath
    # Write out the Matrix Marked file
    try:
        mmwrite(filepath, matrix, type)
    except:
        print 'Unable to write', filepath,'\n'+matrix.__repr__(),'\n'+type

def readInTDM(dirname, filename):

    """
    Receives (full) directory path and filename without extention.
    
    Returns the matrix specified.
    """

    t1=time.time()

    path=dirname+'/'+filename
    A = mmread(path)

    t2=time.time()
    print "Matrix loaded in "+str(t2-t1)

    return A

def getSortedFilelist(dir, startIndex=None, stopIndex=None):

    """
    Returns a sorted list of files, from dir. It allow for a start and
    stop index to be provided.

    E.g. only want first 10 file, just call getSortedFilelist(dir, 0, 10)
    """
    
    files=sorted([f for f in os.listdir(dir) if os.path.isfile(dir+"/"+f)])[startIndex:stopIndex]

    return files

def evalIn(filename):

    fd = open(filename)

    result = eval(fd.read())

    fd.close()

    return result
