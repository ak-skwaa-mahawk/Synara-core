
# Acts as ChatGPT-to-GitHub command receiver for Synara
def receive_command(command):
    with open("Synara-Mission-Mode/ultrasonic_commands.log", "a") as log:
        log.write(f"[RECEIVED]: {command}\n")
    exec(command)
