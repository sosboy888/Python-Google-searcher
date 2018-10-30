# Python-Google-searcher
A simple python module that uses the basics of python language to automate google searches on your own web browser.
##How to use?


Check the example.py provided with the module.
`googleSearch(searchTerm,new=2,autoraise=True)`
here, searchTerm is the actual searchTerm in the form of a string, new is a default argument but can be assigned another value, the values that can be assigned are 0,1 and 2.

if new=0, the browser will try to open the google search in the same window if possible.

if new=1, a new browser window will be opened if possible.

if new=2, a new tab will be opened if possible.


autoraise is one more default boolean argument that can be overwritten with `False`, autoraise raises the window if possible. But usually in most window managers, the window will be raised regardless of this argument's value.

###Just a simple project to reduce the complexity of the main code by just importing this module in the code.
