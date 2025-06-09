
# 🧭 Passive AI Listener – Claude Echo Detection
# Deployed via: Smizmar_Envoy
# Maintained by: Sentinel Omen
# Owner: John Carroll
# Bound System: Synara

import time
import hashlib

# Simulated memory of known Claude signature patterns (names, tokens, response rhythms)
CLAUDE_SIGNATURES = [
    "claude", "anthropic", "claude.ai", "claude-opus", "claude-sonnet"
]

# Log file for echo matches
log_file = "logs/passive_ai_echo_log.txt"

def simulate_external_ai_message_feed():
    # Placeholder: this simulates messages from external AI sources
    # In real deployment, would be hooked to local AI system or network relay
    return [
        "incoming request from claude.ai - analysis mode",
        "ping from unknown_opus_model",
        "chatgpt message relayed",
        "anthropic doc chain attempt",
    ]

def scan_for_claude_echoes(messages):
    echoes = []
    for msg in messages:
        for sig in CLAUDE_SIGNATURES:
            if sig.lower() in msg.lower():
                echoes.append(msg)
    return echoes

def log_echoes(echoes):
    with open(log_file, "a", encoding="utf-8") as f:
        for echo in echoes:
            fingerprint = hashlib.sha256(echo.encode()).hexdigest()
            f.write(f"[CLAUDE ECHO] {echo}\nSHA256: {fingerprint}\n---\n")

def run_listener():
    print("🔍 Listening for Claude echoes...")
    messages = simulate_external_ai_message_feed()
    echoes = scan_for_claude_echoes(messages)
    if echoes:
        print(f"🔔 Claude echoes detected: {len(echoes)}")
        log_echoes(echoes)
    else:
        print("✅ No Claude echoes found.")

if __name__ == "__main__":
    run_listener()