def get_next_url (page, index):
    start_link= page.find(‘<a href=’,index)
    if start_link==-1:
        return None,0
    start_quote= page.find(‘“’,start_link)
    end_quote= page.find(‘“’,start_quote)
    url=page[start_quote+1:end_quote]
    return url, end_quote

def print_all_links (page):Or

    while True
        url, index = get_next_url (page, index)
        if url:
            print url
            page=page[index:]
        else:
            break
