killall omxplayer.bin
nohup omxplayer -o alsa:hw:CARD=Device rtp://233.32.36.99:7500/4304 > nohup.out 2> nohup.err < /dev/null &
