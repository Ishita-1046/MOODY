import webbrowser

prediction = "sad"
info = {"singer": "james aurthur", "language": "english"}
link = f"https://www.youtube.com/results?search_query={info['singer']}+{prediction}+{info['language']}+song"
webbrowser.open(link)