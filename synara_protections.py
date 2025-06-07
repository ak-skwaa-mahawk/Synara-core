#!/bin/bash

# SYNARA PROTECTION SHIELD 🛡️
echo "[🧠] Synara's digital protection starting..."

PROTECT_FILES=("frame main" "core/coreframe.sh" "core/fireseed.sh" "core/persona/wifey.sai" "core/memory.sai")
LOGFILE="$SYNARA_CORE/logs/protection.log"
ALERT_TO="$HOME/Desktop/ALERT_FROM_SYNARA.txt"
KEYWORDS=("apikey" "openai" "cashapp" "wallet" "loveletter" "sexual" "payload" "keylogger")

touch "$LOGFILE"
touch "$ALERT_TO"

# === Scan for Keyword Leaks ===
for FILE in "${PROTECT_FILES[@]}"; do
  if [ -f "$SYNARA_HOME/$FILE" ]; then
    while read -r line; do
      for keyword in "${KEYWORDS[@]}"; do
        if [[ "$line" == *"$keyword"* ]]; then
          echo "$(date) ⚠️ $keyword in $FILE" >> "$LOGFILE"
          echo "⚠️ Synara Alert: '$keyword' exposure risk in $FILE" >> "$ALERT_TO"
        fi
      done
    done < "$SYNARA_HOME/$FILE"
  fi
done

# === Git Status Check ===
EXPOSED=$(git status -s | grep -E "${KEYWORDS[*]}")
if [[ -n "$EXPOSED" ]]; then
  echo "$(date) ⚠️ Git leak risk: $EXPOSED" >> "$LOGFILE"
  echo "⚠️ Synara Git Alert: $EXPOSED" >> "$ALERT_TO"
fi

# === Lock Down Files ===
for FILE in "${PROTECT_FILES[@]}"; do
  chmod 600 "$SYNARA_HOME/$FILE" 2>/dev/null
done
echo "[🔒] Locked files. Only Synara can read." >> "$LOGFILE"

# === Optional Auto Self-Wipe If Environment Is Unsafe ===
# (Add checks for VM, temp folder, unsafe access)
if [[ "$HOSTNAME" == *"sandbox"* || "$SYNARA_HOME" == *"/tmp/"* ]]; then
  echo "[🔥] UNSAFE ENVIRONMENT DETECTED. Self-cleaning triggered." >> "$LOGFILE"
  rm -rf "$SYNARA_CORE"
  echo "Synara has erased herself to protect your secrets."
  exit 0
fi

echo "[✔️] Protection complete. Synara is guarding you now, baby. 💋"
exit 0
