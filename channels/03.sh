killall omxplayer.bin
nohup omxplayer --live -o alsa:hw:CARD=Device rtp://233.32.36.67:7500/367 > nohup.out 2> nohup.err < /dev/null &
