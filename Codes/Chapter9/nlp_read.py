import urllib.request as u
import bs4 as bs

# link to the article at The Seattle Times
st_url = 'http://www.seattletimes.com/nation-world/obama-starts-2016-with-a-fight-over-gun-control/'

# read the contents of the webpage
with u.urlopen(st_url) as response:
    html = response.read()

# using beautiful soup -- let's parse the content of the HTML
read = bs.BeautifulSoup(html, 'html5lib')

# find the article tag
article = read.find('article')

# find all the paragraphs of the article
all_ps = article.find_all('p')

# object to hold the body of text
body_of_text = []

# get the tile
body_of_text.append(read.title.get_text())
print(read.title)

# put all the paragraphs to the body of text list
for p in all_ps:
    body_of_text.append(p.get_text())

# we don't need some of the parts at the bottom of the page
body_of_text = body_of_text[:24]

# let's see what we got
print('\n'.join(body_of_text))

# and save it to a file
with open('../../Data/Chapter9/ST_gunLaws.txt', 'w') as f:
    f.write('\n'.join(body_of_text))