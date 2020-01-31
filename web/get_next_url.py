
def get_next_url (page, index):
    start_link= page.find(‘<a href=’,index)
    start_quote= page.find(‘“’,start_link)
    end_quote= page.find(‘“’,start_quote)
    url=page[start_quote+1:end_quote]
    return url
