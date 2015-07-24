def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)

#maybe it's possible to not write this out as chunks?
#yes, us the content method of r instead of the iter_content method

    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename

This will work and can be used to crawl the page, you just need to add the verifier parameter to the url each time
So here's the url:
https://canvas.uw.edu/eportfolios/23505?verifier=967K9PV1saj8009pBXsUSCnL7WlOneF9qRqLoEc2

This takes you to the first page. From there we can find the list of pages which show up under the div "displaying_contents" and in the <a> class "page_url no-hover"

then we go to https://canvas.uw.edu/eportfolios/23505/Home/<page>?varifier=....
base_url = https://canvas.uw.edu/eportfolios/23505
verifier = "?verifier=967K9PV1saj8009pBXsUSCnL7WlOneF9qRqLoEc2"
@
to go through the pages make a foreach loop or something to walk through the page_urls concatinated with the base_url + Home + page_url + verifier
def download_file(url)
	local_filename	

#
#THIS IS THE WAY TO DO IT. SEE BELOW. WE NEED A FUNCTION THAT MAKES THE REQUEST AND STARTS E
#EXTRACTING STUFF
#WE NEED TO FIGURE OUT WHAT NEEDS TO BE EXTRACTED EXACTLY, BUT WITH CANVAS, THAT'S PREDICTABLE
#ALSO WE CAN ITERATE THROUGH THE VARIOUS PAGES WITHIN ONE PORTFOLIO
#
#works to parse the html but needs some tweaking
import lxml.html
from lxml.cssselect import CSSSelector

# get some html
import requests

r = requests.get('http://url.to.website/')

# build the DOM Tree
tree = lxml.html.fromstring(r.text)

# print the parsed DOM Tree
print lxml.html.tostring(tree)

# construct a CSS Selector
# this can be 'a.page_url' for instance
sel = CSSSelector('div.foo li a')

# Apply the selector to the DOM tree.
results = sel(tree)
print results

# print the HTML for the first result.
match = results[0]
print lxml.html.tostring(match)

# get the href attribute of the first result
print match.get('href')

# print the text of the first result.
print match.text

# get the text out of all the results
data = [result.text for result in results]

# to get all of the hrefs:
for result in results:
	match = [result.get('href')]
	#do something with match...it is an array of all the relative urls

