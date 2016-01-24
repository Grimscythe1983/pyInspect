# --------------------------------------------
# file name : pyInspect.py
# created by : pjdamian.chrzanowski@gmail.com
# date : 17/01/2016
# license : GNU Public License v3
# --------------------------------------------
# class_diagram_creator, Creates a html file with a class diagram of a python file.
# Copyright (C) 2016 Damian Chrzanowski
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------
# EasyGui version 0.98.0
# Copyright (c) -2016, Stephen Raymond Ferg
# All rights reserved.
# --------------------------------------------
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
# following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following
# disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following
# disclaimer in the documentation and/or other materials provided with the distribution.
# 3. The name of the author may not be used to endorse or promote products derived from this software without
# specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE AUTHOR "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
# AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
# ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
import easygui as eg
import os
import webbrowser

CLASSES_FOUND = {}  # global variable
PROG_TITLE = 'pyInspect v0.7'
if os.name == 'nt':  # different os'es use different file path separators.
    SEPARATOR = '\\'  # for windows
else:
    SEPARATOR = '/'  # for linux and os x


def build_html(in_name):
    """Build the html file based on the information found."""
    # out_str is the output string for the html file
    out_str = """<!DOCTYPE html>
<head>
<style>
body {text-align: center; background: #111; color: #FFF;}
fieldset {width: 210px; float: left; border: 1px solid grey;}
.doc-string {font-size: 0px;color: #0B0;}
.doc-stringbr {display: none;}
.var-dscr {font-size: 0px;color: #b2b266;}
.var-dscrbr {display: none;}
.buttons {position: fixed; top:0px; left:0px;}
.buttons button{background: green; color:white; height: 28px;transition: 0.3s; border: 1px solid green;}
.buttons button:hover{background: #040;}
.buttons button:active{background: #FFF;}
.header {font-size: 11px; color: white; position: fixed; top: 10px; right: 20px;}
</style>
<script>
    state = 0;
    state_1 = 0;
    function br_control(node_class, state_of_br){
        var css_br_state;
        var z;
        if (state_of_br == 0){css_br_state = "display: inline;"}
        else if (state_of_br == 1) {css_br_state = "display: none;"}
        z = document.getElementsByClassName(node_class);
        for (var x=0; x < z.length; x++){
            z[x].setAttribute("style", css_br_state)
        }
    }
    function show_docstrings() {
        if (state == 0) {
            d = document.getElementsByClassName("doc-string")
            for (var x=0; x < d.length; x++){
                d[x].setAttribute("style", "font-size: 12px; transition: 0.5s; opacity: 1;")
            }
            br_control("doc-stringbr", 0);
            state = 1;
        }
        else if (state == 1) {
            d = document.getElementsByClassName("doc-string")
            for (var x=0; x < d.length; x++){
                d[x].setAttribute("style", "font-size: 0px; transition: 0.5s; opacity: 0;")
            }
            setTimeout(function(){br_control("doc-stringbr", 1)}, 400);
            state = 0;
        }
    }
    function show_variables() {
        if (state_1 == 0) {
            d = document.getElementsByClassName("var-dscr")
            for (var x=0; x < d.length; x++){
                d[x].setAttribute("style", "font-size: 12px; transition: 0.5s; opacity: 1;")
            }
            br_control("var-dscrbr", 0);
            state_1 = 1;
        }
        else if (state_1 == 1) {
            d = document.getElementsByClassName("var-dscr")
            for (var x=0; x < d.length; x++){
                d[x].setAttribute("style", "font-size: 0px; transition: 0.5s; opacity: 0;")
            }
            setTimeout(function(){br_control("var-dscrbr", 1)}, 400);
            state_1 = 0;
        }
    }
</script>
</head>
<body>
    <div class="buttons">
        <button onclick="show_docstrings()">Show Docstrings</button>
        <button onclick="show_variables()">Show Variables Information</button>
    </div>
<p class="header">Created with %s</p>
<br><h1>Class diagram for <span style="color:#28ADB5">%s</span></h1>
<h2>Click the buttons in the top left corner to see more details.</h2>""" % (PROG_TITLE, in_name)  # insert file name
    for key in CLASSES_FOUND:  # iterate through the keys of the global var
        out_str += '\n<fieldset><legend style="color:#00ffcc">%s Class</legend>' % key  # insert class name
        out_str += '\n<span class="doc-string">%s</span>' % CLASSES_FOUND[key][2]  # insert the docstring
        if len(CLASSES_FOUND[key][1]) > 0:  # if class's __init__ has variables then ->
            out_str += '\n<fieldset><legend style="color:#ff9900">Variables</legend>'  # insert variables section
            for each_val in CLASSES_FOUND[key][1]:  # iterate through the variables
                # insert the variable's description and its name
                out_str += '\n<span>%s</span><br>' % each_val[0]
                out_str += '\n<span class="var-dscr">%s<br class="var-dscrbr"></span>' % each_val[1]
            out_str += '\n</fieldset>'  # close the variables section
        if len(CLASSES_FOUND[key][0]) > 0:  # if class contains any methods then ->
            out_str += '\n<fieldset><legend style="color:#ff33cc">Methods</legend>'  # insert methods section
            for each_val in CLASSES_FOUND[key][0]:  # iterate through class's methods
                # insert the methods's description and its name
                out_str += '\n<span>%s</span><br>' % each_val[0]
                out_str += '\n<span class="doc-string">%s<br class="doc-stringbr"></span>' % each_val[1]
            out_str += '\n</fieldset>'  # close the methods section
        out_str += '\n</fieldset>'  # close the class's section
    out_str += '\n</body>'  # close the html's body section
    # choose a file
    out_name = eg.filesavebox(msg='Please select a file', title=PROG_TITLE, default='class_diagram.html')
    if out_name is None or out_name == '.':  # if no file has been selected, quit
        quit()
    out_file = open(out_name, 'w')  # open file for saving, wiping its content if it already exists
    out_file.write(out_str)  # save the html source to the file
    out_file.close()  # close the file
    eg.msgbox('Opening ' + out_name + ' in your web browser.', title=PROG_TITLE)  # closing prompt
    webbrowser.open(out_name)  # open created file in a new window in the browser


def welcome_prompt():
    """Welcome prompt with the license information."""
    prompt = """%s
Copyright (C) 2016 Damian Chrzanowski
pyInspect comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome
to redistribute it under certain conditions.
For details refer to COPYING.txt.""" % PROG_TITLE

    eg.msgbox(prompt, title=PROG_TITLE)


def main():
    """Programs main source code."""
    # Still very messy, done it all in only a few hours, so pardon for poor readability
    in_name = eg.fileopenbox(msg='Please select a python file', title=PROG_TITLE)  # select an input file
    if in_name == '.' or in_name is None:  # if no file has been selected, quit
        quit()
    in_file = open(in_name, 'r')  # open the input file in read-only
    in_name = in_name.split(SEPARATOR)[-1]  # extract the file name for furter use
    current_class = ''  # current class being searched and alayzed
    hunt_selfs = False  # look for variables within the __init__ method
    hunt_doc = False  # look for docstring
    hunting = ''  # looking for functions/classes's docstrings
    continuing_doc = False  # multiline docstrings
    doc_string = ''  # multiline docstrings
    current_method_name = ''  # name of the current method being investigated
    for each_line in in_file:  # iterate through every line of the file
        if continuing_doc:  # if the docstring didn't finish in one line, look for more docstring lines
            if ('"""') in each_line:  # check for """ style docstrings in the line (meaning we are comleting it here)
                each_line = each_line.strip()  # strip trailing ends
                each_line = each_line.strip('"""')  # strip the quotations
                # add a newline to the docstring and the lines content
                doc_string += '<br class="doc-stringbr">' + each_line
                if hunting == 'class':  # if we're investigating a class add the docstring to the class
                    CLASSES_FOUND[current_class][2] = doc_string
                elif hunting == 'function':  # if we're investigating a method add the docstring to the class
                    CLASSES_FOUND[current_class][0].append([current_method_name, doc_string])
                continuing_doc = False  # don't look for any more docstring lines on this element. reset the variable
                doc_string = ''  # reset the docstring variable
                hunting = ''  # reset the current element being investigated
                continue  # back to top
            elif ("'''") in each_line:  # check for ''' style docstrings in the line (meaning we are comleting it here)
                each_line = each_line.strip()
                each_line = each_line.strip("'''")
                doc_string += '<br class="doc-stringbr">' + each_line
                if hunting == 'class':
                    CLASSES_FOUND[current_class][2] = doc_string
                elif hunting == 'function':
                    CLASSES_FOUND[current_class][0].append([current_method_name, doc_string])
                continuing_doc = False
                doc_string = ''
                hunting = ''
                continue
            else:  # if the line doesn't have a ''' or """ then add its content to the docstring
                each_line = each_line.strip()  # strip trailing ends
                doc_string += '<br class="doc-stringbr">' + each_line  # add a newline and the content
                continue  # back to top
        if each_line.lower().startswith('class'):  # if a line starts with the word class
            if hunt_doc:  # if we were looking for a docstring, stop it.
                hunt_doc = False  # don not look for a docstring anymore
                if hunting == 'class':  # if a class was investigated
                    CLASSES_FOUND[current_class][2] = 'No Docstring'  # enter 'No Docstring' to the class
                elif hunting == 'function':  # if a method was investigated
                    # enter 'No docstring' to the method's description
                    CLASSES_FOUND[current_class][0].append([current_method_name, 'No Docstring'])
                hunting = ''  # reset what we're looking for
            each_line = each_line.strip().split()[1]  # strip trailing ends and pick up second word(class name)
            if '(' in each_line:  # if the class is defined with brackets then remove them
                each_line = each_line.split('(')[0]  # split at the bracket and pick up the first element(name)
                CLASSES_FOUND[each_line] = [[], [], []]  # create a new entry in the CLASSES_FOUND
                current_class = each_line  # set the current_class class being investigating
            else:  # if the class is defined without brackets , remove the colon from the name
                each_line = each_line.rstrip(':')  # remove the colon
                CLASSES_FOUND[each_line] = [[], [], []]  # create a new entry in the CLASSES_FOUND
                current_class = each_line  # set the current_class class being investigating
            hunt_doc = True  # look for a docstring
            hunting = 'class'  # look for a class docstring
            hunt_selfs = False  # reset the look for __init__ variables
        if 'def ' in each_line.lower():  # if a line has a method definition then ->
            # also check if it is a class type method (starts wiht spaces or tabs)
            if ord(each_line[0]) == 32 or ord(each_line[0]) == 9:
                if '(' in each_line:  # makes sure that it is a method declaration line, has a bracket in it
                    if hunt_doc:  # if we were looking for a docstring, stop it.
                        hunt_doc = False  # don not look for a docstring anymore
                        if hunting == 'class':  # if a class was investigated
                            CLASSES_FOUND[current_class][2] = 'No Docstring'  # enter 'No Docstring' to the class
                        elif hunting == 'function':  # if a method was investigated
                            # enter 'No docstring' to the method's description
                            CLASSES_FOUND[current_class][0].append([current_method_name, 'No Docstring'])
                        hunting = ''  # reset what we're looking for
                    each_line = each_line.strip().split()[1]  # strip and extract the name
                    each_line = each_line.split('(')[0]  # split at the bracket and extract the name
                    if current_class != '':  # if  there is a class being investigated then ->
                        current_method_name = each_line  # set a new method being investigated
                        if each_line == '__init__':  # if the method is __init__ then look for variables
                            hunt_selfs = True
                        else:  # otherwise do not look for variables
                            hunt_selfs = False
                        hunting = 'function'  # investigate a method's docstring
                        hunt_doc = True  # look for docstring
        if hunt_selfs:  # if we're looking for __init__ variables
            if 'self.' in each_line.lower():  # check if a line has a 'self.' in  it
                var_name = each_line.strip().split('=')[0]  # split at the '=' and extract the left side
                var_name = var_name.split('.')[1]  # split at the '.' and extract the variable's name
                for each in CLASSES_FOUND[current_class][1]:  # check if the variable is already in the database
                    if var_name in each:  # if the variable already exists
                        var_name = '('  # set it to a bracket, which makes to code to go back up, on the next if
                        break  # break out of the double's search
                if '(' in var_name:  # if the variable has a bracket then it is in fact a function call, skip.
                    continue  # back up
                else:  # if all checks are correct then ->
                    if '#' in each_line:  # check if the variable has a comment
                        var_description = each_line.split('#')[-1]  # split and exract the comment
                        var_description = var_description.strip()  # strip triling ends
                        # add the variable's name and its comment to the database
                        CLASSES_FOUND[current_class][1].append([var_name, var_description])
                    else:  # if the lines doesnt have a comment add only it's name to the database
                        var_description = ''
                        CLASSES_FOUND[current_class][1].append([var_name, var_description])
        if hunt_doc:  # if we're loooking for docstrings
            if ('"""') in each_line:  # if it's the """ docstring style, and has been found
                # if the line also ends with a """, then its a single line docstring
                if each_line.strip().endswith('"""'):
                    each_line = each_line.strip()  # strip trailing ends
                    each_line = each_line.strip('"""')  # strip the quotations
                    if len(each_line) == 0: # it is a multiline docstring without flake8
                        hunt_doc = False
                        continuing_doc = True
                        continue
                    if hunting == 'class':  # if the class was investigated
                        CLASSES_FOUND[current_class][2] = each_line  # add the class's docstring
                    elif hunting == 'function':  # if a method was investigated
                        # add the current method's name and it's docstring to the database
                        CLASSES_FOUND[current_class][0].append([current_method_name, each_line])
                    hunting = ''  # reset the element being investigated
                    hunt_doc = False  # stop looking for a docstring
                else:  # if it is a multiline docstring then ->
                    doc_string = each_line.strip()  # strip the trailing ends
                    doc_string = doc_string.strip('"""')  # strip the quotations
                    continuing_doc = True  # set the continuing_doc to look for more lines of the docstring
                    hunt_doc = False  # stop the search for the begining of a docstring
            elif ("'''") in each_line:  # same as above, different style docstring
                if each_line.strip().endswith("'''"):
                    each_line = each_line.strip()
                    each_line = each_line.strip("'''")
                    if len(each_line) == 0:  # it is a multiline docstring without flake8
                        hunt_doc = False
                        continuing_doc = True
                        continue
                    if hunting == 'class':
                        CLASSES_FOUND[current_class][2] = each_line
                    elif hunting == 'function':
                        CLASSES_FOUND[current_class][0].append([current_method_name, each_line])
                    hunting = ''
                    hunt_doc = False
                else:
                    doc_string = each_line.strip()
                    doc_string = doc_string.strip("'''")
                    continuing_doc = True
                    hunt_doc = False
    print CLASSES_FOUND
    in_file.close()  # close the file
    build_html(in_name)  # build the html file


if __name__ == '__main__':
    welcome_prompt()  # display a welcome prompt
    main()  # start the program
    quit()  # end program
