#!/bin/bash

gnuplot -persist <<"EOF"
set style data linespoints
show timestamp
set xlabel "time (seconds) reno"
set ylabel "segments (cwnd)"
plot "/home/volkner/mininet/custom/utopiaReno.txt" using 1:7 title "snd_cwnd", \
      "/home/volkner/mininet/custom/utopiaReno.txt" using 1:($8>=2147483647 ? 0 : $8) title "snd_ssthresh"
EOF
