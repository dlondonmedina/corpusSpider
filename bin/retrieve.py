#!c:\Python27\python.exe
#Change the above line for linux
raw_urls = form.getlist('urls')
urls = []
for i in raw_urls:
	urls.append(cgi.escape(raw_urls[i]))

filename = "urls.txt"
def file_write(filename):
	txt = open(filename, 'w')
		for url in urls: 
			txt.write(url)
			txt.write("\n")
		txt.close()

print '''
Content-Type: text/html\n
<html><body><p>%r has been written to disk.''' % filename
