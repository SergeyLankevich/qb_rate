import urllib.request

with open('page_example.txt', 'w') as f:
    print(str(urllib.request.urlopen("http://www.nfl.com/player/jordanta'amu/2562752/profile").read()), file=f)