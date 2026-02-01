#!/usr/bin/env sh
set -euo pipefail

HOST_IP="$(ip -4 route get 1.1.1.1 | awk '{for(i=1;i<=NF;i++) if ($i=="src") {print $(i+1); exit}}')"

# Build setup.sh and substitutes __IP__ and __PORT_ZIP__
mkdir -p "$SH_DST_FOLDER"
(
    OUT="$SH_DST_FOLDER/$SH_DST_FILE"
    cd "$SH_SRC_FOLDER"
    cat $SH_SRC_FILES > "$OUT"
    sed -i "s/__IP__/${HOST_IP}/g" "$OUT"
    sed -i "s/__PORT_ZIP__/${PORT_ZIP}/g" "$OUT"
    sed -i "s/__PORT_SUBJECTS__/${PORT_SUBJECTS}/g" "$OUT"
    chmod +x "$OUT"
)

# Build zip
mkdir -p "$ZIP_DST_FOLDER"
rm -f "$ZIP_DST_FOLDER/$ZIP_DST_FILE"
(
  cd "/app"
  zip -r "$ZIP_DST_FOLDER/$ZIP_DST_FILE" $ZIP_SRC_ITEMS
)

