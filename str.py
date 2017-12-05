s = 'Michel Francisco Michel de Medeiros Michel'
t = 'Michel'
i = 1

#print (s.find(t,i))
#print (s[i:].find(t))
#print (s.find(t)[:i])
#print (s[i:].find(t) + i)
#print (s[i:].find(t[i:]))


#page = '''<div id="top_bin"><a href="/">'''

#print(page.find('<a href='))



page =('<div id="top_bin"><div id="top_content" class="width960"><div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
print(start_link)
start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote + 1)
url = page[start_quote + 1:end_quote]
print(url)
#end_link = page.find('>', 89)
#print(end_link)
#url = page[start_link:end_link]
#print(url)

#print (s.find(s))
#print (s.find('s'))
#print ('s'.find('s'))
#print (s.find(''))
#print (s.find(s + '!!!') + 1)