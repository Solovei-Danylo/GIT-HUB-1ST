

text = """
Want to contribute?
To report a bug in the Python core, use the Python Bug Tracker.
To report a problem with this web site, use the pythondotorg issue tracker.
To contribute a bug fix or other patch to the Python core, see the Python Developer's Guide.
To contribute to the official Python documentation, use the Issue Tracker to contribute a documentation patch. See also the guide to Helping with Documentation.
To contribute to the official Python website, see the About the Python Web Site page or read the developer guide on Read the Docs.
To announce your module or application to the Python community, use comp.lang.python.announce (or via email, python-announce@python.org, if you lack news access). More info: the announcements newsgroup description
"""
words_count = text.count(" ")
print(type(words_count), "type words_count")
symbols_count = len(text)

print("Words count: ", words_count)
print("Symbol count: ", symbols_count)
