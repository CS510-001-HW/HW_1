#!/bin/bash
cd dataset1/ && grep -r -l "sample" | xargs grep -c "CSC510" | grep -E ":[3-9]$" | rev | sort -k1,1nr | rev | awk -F: '{print $1, $2}' | xargs -I{} sh -c 'file=$(echo "{}" | awk "{print \$1}"); count=$(echo "{}" | awk "{print \$2}"); size=$(ls -l "$file" | awk "{print \$5}"); echo "$file" "$count" "$size"' | sort -k2,2nr -k3,3nr | awk "{print \$1}" | sed 's/file_/filtered_/'

