killall omxplayer.bin
nohup omxplayer -o alsa:hw:CARD=Device rtp://233.136.0.65:7500/4201 > nohup.out 2> nohup.err < /dev/null &
