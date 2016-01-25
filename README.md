# pyInspect
Create a simple class diagram with docstring and variable descriptions.

pyInspect Version 0.7a
---------------------------
Copyright (C) 2016 Damian Chrzanowski
pjdamian.chrzanowski@gmail.com
License : GNU Public License v3

Overview:
Creates a html file that contains all (almost) information about your .py code's classes and their methods.
All information is extracted from the docstrings and from comments in case of __init__ method's variables.

Usage:
 - First, if you do not have EasyGui(c). Get it here https://sourceforge.net/projects/easygui/
 - Alternatively get EasyGui(c) through pip. Go to your command prompt (console in linux) and type in: pip install easygui
 - Windows:
 If you have python 2.7 installed, just double click the pyInspect.py file to launch the program.
 Executable format coming soon.
 - Linux:
 Navigate to the folder in which you have your pyInspect.py file. Right click and select 'open the terminal window here'.
 Type in python pyInspect.py.

TODO:
- Inheritance.
- Code does not recognize comments for self.variable if they are not placed in the same line.
- The reverse. Make a .py file out of a class diagram.

Change Log:

- version 0.7a
    - added the .py file name to the output html file name.
- version 0.7
    - handles non flake8 docstrings.
- version 0.6
    - now creates an animated version of the website.

========================================
License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see:
http://www.gnu.org/licenses/
========================================
pyInspect uses:

EasyGui version 0.98.0
Copyright (c) -2016, Stephen Raymond Ferg
All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following
disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following
disclaimer in the documentation and/or other materials provided with the distribution.
3. The name of the author may not be used to endorse or promote products derived from this software without
specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE AUTHOR “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
