Name: Prateeti Shah, Email: prateeti@csu.fullerton.edu

Steps to run Server Side code:
1. Add 'Python code for Web Server' to main.py file in python code editor. (I used PyCharm here)
2. Put 'HelloWorld.html' file in the same directory.
3. Run the code using terminal window with the command 'python3 main.py'.
4. Once it shows 'Ready to Serve...' message in the terminal window, run 'http://127.0.0.1/HelloWorld.html' in any browser. (I used Brave browser)
5. The browser will display success message as well as HTML file content.
6. Try to run any other .html file without including it into the directory with different name.
7. It will show '404 File not Found' message.

Steps to run Client Side code:
1. Make a new python file in the same directory.
2. Put 'Python code for Client' in that file.
3. Run 'python3 main.html' first.
4. When we get 'Ready to Serve...' message, run 'python3 Client.py "127.0.0.1" "80" "HelloWorld.html"' command in different terminal window.
5. It will display success message along with the html file content.
6. Try to run any other .html file without including it into the directory with different name.
7. It will show '404 File not Found' message.