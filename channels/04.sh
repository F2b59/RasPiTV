killall omxplayer.bin
nohup omxplayer --live -o alsa:hw:CARD=Device rtp://233.32.36.122:7500/3122 > nohup.out 2> nohup.err < /dev/null &
