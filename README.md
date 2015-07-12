# ncmpcpp cheat sheet

Cheat sheet generator for ncmpcpp, [click here for the cheat sheet.](http://pkgbuild.com/~jelle/ncmpcpp/)

Dependencies
------------

* Python 3.x (tested on 3.4)
* Python-jinja


Generating the cheat sheet
--------------------------

Since I haven't found a way to get the key mapping of ncmpcpp from the source code, we copy text from ncmpcpp help screen.
Open ncmpcpp, select the text by pressing the shift key and copy it to a file named 'keys.txt'.

Now run generate_keys.txt which takes the 'keys.txt' file, parses it, reads the jinja template from templates and creates an
index.html page in the html directory.

To view the generated page, just run

 $BROWSER html/index.html
