import re  # regular expressions
import os
import time

pattern1 = re.compile("^d")  # zaczyna sie od d
print(pattern1.match('dog'))

pattern2 = re.compile('^[dD].*[gG]$') # ^ zaczyna sie .* dowolne znaki dowolna ilosc $ konczy sie
print(pattern2.match('dddooooooooogg'))

postalCode = '88-444'
result = re.search('^[0-9]{2}-[0-9]{3}$', postalCode)

if(result is None):
    print("Błąd kodu pocztowego")
else:
    print("Jest ok")
print('==============================================')
filePattern = re.compile('.{1,}[\.]{1}(pdf|doc|xlsx)$')
os.chdir("C:\\Users\\user\\Desktop")
for content in os.listdir('.'):
    if (re.search(filePattern,content)):
        print(content)

print('==============================================')
filePattern = re.compile('.*[^\.]')
filePattern1 = re.compile('^\w*[^\.]\w*$')
path = "C:\\Users\\user\\Desktop"
os.chdir(path)
for content in os.listdir('.'):
    if (re.search(filePattern,content)):
        print(" %-70s | %10.2f MB" % (content, os.path.getsize(content)/(10**6)))
        print(" %-70s | %10s TIME" % (content, time.ctime(os.path.getctime(content))))
        print(" %-70s | %10s TIME" % (content, time.ctime(os.path.getmtime(content))))
print("======= KATALOGI =======")
for content in os.listdir('.'):
    if (re.search(filePattern1,content)):
        print(" %-70s | %10.2f MB" % (content, os.path.getsize(content)/(10**6)))
        print(" %-70s | %10s TIME" % (content, time.ctime(os.path.getctime(content))))
        print(" %-70s | %10s TIME" % (content, time.ctime(os.path.getmtime(content))))