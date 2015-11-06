Overview
--------
Use your keyboard to control your TiVo.
Record macros.
Playback macros.

Demo video
----------
[![Demo of TiVo macro recorder](http://i.imgur.com/VoYYKPz.jpg)](https://youtu.be/XjQA-riCsYU "Demo of TiVo macro recorder")

Instructions
------------
1. Turn on "Network Remote Control" on your TiVo. This is somewhere in Settings. Maybe Settings->Remote->Network Remote Control.
2. Find the IP address of your TiVo. Write it down.
3. Record your keystrokes.
    ```
    $ python tivo_record_keystrokes.py <tivo-ip-address>
    ```

    Use the following keys to emulate the corresponding buttons on the
    TiVo remote.
    
    TiVo remote      |      PC keyboard
    -----------------|------------------
    UP               |      up arrow
    DOWN             |      down arrow
    LEFT             |      left arrow
    RIGHT            |      right arrow
    SELECT           |      spacebar
    TiVo button      |      t

    Hit 'q' to exit. When you hit 'q', it will print out a list of
    instructions. Save that output to a file. This will be your macro.

    It may look like this:
    ```
    2 KEY_DOWN
    1 KEY_UP
    1 SELECT
    1 SELECT
    ```

4. Playback your macro.
    ```
    $ python tivo_playback_keystrokes.py <macro-file> <tivo-ip-address>
    ```


What can I do with this?
------------------------
Whatever you want! Some ideas:

* Mark all recordings in a folder as "Keep until I delete"
* Transfer all your recordings from one DVR to another
* Set all your One Passes to "Get in HD: Always"

Here's what *I* did with it:

I wrote this to allow me to transfer all my old recordings to my new
TiVo. TiVo currently has no way to bulk transfer recordings, but you
can use the TV UI to transfer a single show at a time. I used my tool
to write a macro to transfer a single show, and then played back the
macro 60 times to transfer all the shows. It worked, the DVR queued up
the transfers, and my DVR spent the next several days transferring
shows. The end result was that I had all my old shows on my new DVR.

Limitations
-----------
The tool simply plays back your button presses. It has no idea what
screen it is on, or what the menu choices are.

Even for a list of identical-looking items, like the recordings in
your My Shows list, sometimes the menu choices will be different for
each. For example, clicking the "Keep until I delete" button on one
recording might immediately change that setting, whereas clicking
"Keep until I delete" on another recording might bring up a conflict
dialog saying that you are running out of disk space. Keep that in
mind when writing your macros.
