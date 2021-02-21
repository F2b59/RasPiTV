killall omxplayer.bin
nohup omxplayer -o alsa:hw:CARD=Device rtp://233.32.36.79:7500/379 > nohup.out 2> nohup.err < /dev/null &
