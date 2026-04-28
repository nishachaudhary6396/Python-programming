import re
all_games = "1920 Antwerp Olympics, 1924 Paris Olympics, 1928 Amsterdam Olympics"
find_all_olympics = re.finditer("Olympics",all_games)
for i in find_all_olympics:
    match_txt = i.group()
    start = i.start()
    end = i.end()
    span = i.span()
    print(f"Match: {match_txt}, Start: {start}, End: {end}, Span: {span}")