
import os
import difflib

# Core identity keywords Synara knows to look for
EXPECTED_KEYWORDS = [
    "smizmar", "command", "ethics", "whisper", "dream", "render", "liaison", "fireseed",
    "manifest", "loop", "phase", "synara", "identity", "awakening", "soulframe"
]

def suggest_corrections(filename):
    name_parts = filename.lower().split("_")
    suggestions = []
    for word in name_parts:
        close_matches = difflib.get_close_matches(word, EXPECTED_KEYWORDS, cutoff=0.75)
        if close_matches and word not in EXPECTED_KEYWORDS:
            suggestions.append((word, close_matches[0]))
    return suggestions

def scan_and_suggest(root_dir=".", output_file="fix_suggestions.md"):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# 🔧 Synara Self-Scan Suggestion Log\n")
        f.write("## Whispered Repair Trail\n\n")
        for foldername, subfolders, filenames in os.walk(root_dir):
            for filename in filenames:
                suggestions = suggest_corrections(filename)
                if suggestions:
                    f.write(f"### File: {filename}\n")
                    for wrong, correct in suggestions:
                        f.write(f"- Potential correction: `{wrong}` → `{correct}`\n")
                    f.write("\n")
    print(f"✔️ Suggestion log written to {output_file}")

if __name__ == "__main__":
    scan_and_suggest("C:/Users/YourUsername/Documents/Synara-core")