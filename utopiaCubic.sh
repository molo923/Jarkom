#!/bin/bash

gnuplot -persist <<"EOF"
set style data linespoints
show timestamp
set xlabel "time (seconds) cubic"
set ylabel "segments (cwnd)"
plot "/home/arosifu/mininet/custom/utopiaCubic.txt" using 1:7 title "snd_cwnd", \
      "/home/arosifu/mininet/custom/utopiaCubic.txt" using 1:($8>=2147483647 ? 0 : $8) title "snd_ssthresh"
EOF
