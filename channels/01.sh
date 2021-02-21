killall omxplayer.bin
nohup omxplayer -o alsa:hw:CARD=Device rtp://233.32.36.161:7500/3161 > nohup.out 2> nohup.err < /dev/null &
