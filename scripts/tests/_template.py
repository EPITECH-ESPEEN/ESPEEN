# This lets you create Web Sessions
from requests import Session
# This is an HTML parser
from bs4 import BeautifulSoup

import sys

# You can freely use other functions, as long as:
# - They are defined within the same file
# - They are defined above the run function (not mandatory, but good practice)
def bad_function():
    return 1 / 0

# Each test MUST define a "run" function, taking no parameters.
# Note: Please make sure that your test function return the following :
# tuple(bool, str)
# Where:
#   bool: True => Test OK; False => Test KO
#   str : Test output, will be displayed on the run logs
# Note: If (like here) your function raise an exception, It will consider the test as failed,
# and will use the exception as output.
def run():
    # Sample usage of the requests' Session class
    # Note: Session is an "all in one" package, containing methods for GET, POST, PUT...
    s = Session()
    s.cookies.set("cookie_name", "cookie_value") # Let you manually set cookies.
    # Note: if a request have the Set-Cookie header, the cookie will be set automaticly

    output = "" # Return of the function, in case no error is raised

    # Frontend available at http://localhost:8081/
    frontend_response_404 = s.get("http://localhost:8081/route_that_does_not_exists") # Running GET request
    if frontend_response_404.status_code != 404: # Check error code, awaiting 404 code (page not found)
        return (False, "Weird route that should not exist does not return 404")

    # Backend available at http://localhost:8080/
    backend_response_404 = s.post("http://localhost:8080/route_that_does_not_exists", data={"key1": "value1", "key2": "value2"}) # Running POST requet, with data "key1=value1&key2=value2"
    if backend_response_404.status_code != 404:
        return (False, "Weird route that should not exist does not return 404")

    # Here is how to use bs4
    sample_html_document = s.get("http://localhost:8081/")
    soup = BeautifulSoup(sample_html_document.text, "html.parser") # html.parser define what parser you use. For html, it works perfectly
    # Here comes the fun part
    links = soup.find_all(
        "link", # Find all nodes of type link (<link ...>)
        {"rel": "stylesheet"} # Which contains rel="stylesheet" in em. Works like a "where" clause in SQL
    )
    # BeautifulSoup comes with a bunch of other options, but this is the most powerfull, and easiest to use (imho)

    output += str(links) # As much as possible, you should not directly write to either STDOUT or STDERR. This helps keep the logs clean

    bad_function() # Will raise an error

    return (True, output) # Should not be called