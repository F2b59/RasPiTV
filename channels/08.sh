killall omxplayer.bin
nohup omxplayer -o alsa:hw:CARD=Device rtp://233.136.0.126:65000/4206 > nohup.out 2> nohup.err < /dev/null &
