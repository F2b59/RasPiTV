killall omxplayer.bin
nohup omxplayer --live -o alsa:hw:CARD=Device rtp://233.136.0.58:7500/58 > nohup.out 2> nohup.err < /dev/null &
