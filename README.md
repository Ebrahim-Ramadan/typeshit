# mody-tool-myass

[ilustration](illustration.mp4)
<br/>
you should activate the python env to has the separated env for the project
<br/>
## how the threading delay works:
+ Every time a key is pressed, it cancels the previous timer (if any) and starts a new one.
* If there's no further keypress within the debounce delay, the timer will trigger the `process_buffer` function.
<br/>
`test.txt` is just for typing test