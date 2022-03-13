# white-noise

Tiny little script to build a white noise machine. We use this to keep our little one sleeping at night. I run it on a raspberry pi (raspbian). Just scp the script (and your mp3) to something like /pi/home, then edit /etc/profile to run your script on bootup. Make sure that raspbian is configured to always start the command line on bootup and not launch in desktop mode.
