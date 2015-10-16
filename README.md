Overview
--------
Use your keyboard to control your TiVo.
Record macros.
Playback macros.

Instructions
------------
1. Turn on "Network Remote Control" on your TiVo. This is somewhere in Settings. Maybe Settings->Remote->Network Remote Control.
2. Find the IP address of your TiVo. Write it down.
3. Record your keystrokes.
    ```
    $ python tivo_record_keystrokes.py <tivo-ip-address>
    ```

    Use the following keys to emulate the corresponding TiVo button
    
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
