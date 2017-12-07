# Modify the get_next_target procedure so that
# if there is a link it behaves as before, but
# if there is no link tag in the input string,
# it returns None, 0.

# Note that None is not a string and so should
# not be enclosed in quotes.

# Also note that your answer will appear in
# parentheses if you print it.

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    else:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote

#page =('<div id="top_bin"><div id="top_content" class="width960"><div class="udacity float-left">')
#url,end_quote = get_next_target(page)
#print(url, end_quote)

def get_page(url):
    try:
        import urllib.request
        page = urllib.request.urlopen(url).read().decode("utf-8")
        return page
    except Exception as inst:
        print(inst)
        return ''

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print(url)
            page = page[endpos:]
        else:
            break

page =('<div id="top_bin"><div id="top_content" class="width960"><div class="udacity float-left"><a href="http://udacity.com"><div class="udacity float-left"><a href="http://google.com">')
#print_all_links(page)
print_all_links(get_page('http://xkcd.com/353'))