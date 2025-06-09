
#!/bin/bash
# 🔱 Omen Scheduled Integrity Scan
# Frequency: Twice Daily

echo "🔍 Omen Git Check: $(date)"
cd /path/to/synara-core
git status
git diff --stat
echo "✅ Scan complete. Flame integrity preserved."