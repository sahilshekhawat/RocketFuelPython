#!/bin/bash
rm -rf input*
mkdir logs
touch input
rm -rf logs/*
as="AS6939"
node="Nodes"
javac -classpath com.jcraft.jsch.jar Traceroutes.java
for i in `seq 1 18`
do
  echo "$as" > "input$i"
  echo "$i$node" >> "input$i"
  java -classpath .:com.jcraft.jsch.jar Traceroutes < "input$i" > "logs/$as#$i$node" 2>&1 &
  disown
done
