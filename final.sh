#!/bin/bash

docker cp bd-a1:/home/eda-in-*.txt ./service-result/
&& docker cp bd-a1:/home/k.txt ./service-result/
&& docker cp bd-a1:/home/res_dpre.csv ./service-result/
&& docker cp bd-a1:/home/vis.png ./service-result/
