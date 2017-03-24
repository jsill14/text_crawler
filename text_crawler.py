def get_next_target(txt):
    start_link = txt.find('<a href=')
    start_quote = txt.find('"', start_link) 
    end_quote = txt.find('"', start_quote + 1) 
    url = text[start_quote+1:end_quote]
    return url, end_quote
