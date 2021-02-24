killall omxplayer.bin
nohup omxplayer --live -o alsa:hw:CARD=Device rtp://233.136.44.27:7500/4106 > nohup.out 2> nohup.err < /dev/null &
