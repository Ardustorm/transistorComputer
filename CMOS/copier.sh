#!/bin/bash
for file in $(ls *_Gate.*); do cp "$file" "Gate_${file/_Gate/}";done
