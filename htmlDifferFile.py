#!/usr/bin/python
import difflib
import sys

def read_file(filename=""):
    try:
        file_handle = open(filename, 'rb')
        text = file_handle.read().splitlines()
        file_handle.close()
        return text
    except IOError as error:
        print('Read file error '+ str(error))
        sys.exit()

try:
     textfile1 = sys.argv[1]
     textfile2 = sys.argv[2]
except Exception, e:
     print "Error :" + str(e)
     sys.exit

text1lines = read_file(textfile1)
text2lines = read_file(textfile2)

diff = difflib.Differ()
different = diff.compare(text1lines, text2lines)
print '\n'.join(list(different))

htmlDiff = difflib.HtmlDiff()

print htmlDiff.make_file(text1lines, text2lines)