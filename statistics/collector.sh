#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IPS="${ROOT}/docker/logs/ips.log"
OUTPUT_REPORTS="${ROOT}/reports/$(date +'%Y-%m-%d')"

mkdir -p "$OUTPUT_REPORTS"

echo "IPs:"

while IFS= read -r ip; do

  [[ -z "$ip" ]] && continue

  # ip: 192.168.0.1 -> 192_168_0_1
  dest="$OUTPUT_REPORTS/${ip//./_}"
  mkdir -p "$dest"

  echo "- $ip"

  wget \
    --execute robots=off \
    --quiet \
    --recursive \
    --no-parent --no-directories \
    --accept "*.json"  \
    --directory-prefix="$dest" \
    "http://$ip:42999/"

done < <(
  sed 's/\r$//' "$IPS" |
  sort -u # Keep only unique ips
)

echo
echo "All JSON files have been saved to:"
echo "  $OUTPUT_REPORTS"
echo
echo "You can now run the following script to get a complete report:"
echo "  python3 $ROOT/statistics/compute.py $OUTPUT_REPORTS"
