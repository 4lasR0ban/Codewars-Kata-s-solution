# Codewars Kyu 5

# Extract the domain name from the URL

# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.

import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')