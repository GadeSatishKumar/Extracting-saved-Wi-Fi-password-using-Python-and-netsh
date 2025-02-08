import subprocess

# Get the list of Wi-Fi profiles
command = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode()
profiles = [i.split(":")[1].strip() for i in command.split("\n") if "All User Profile" in i]

for i in profiles:
    # Get the password for each Wi-Fi profile
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode()
        key_content = [b.split(":")[1].strip() for b in results.split("\n") if "Key Content" in b]
        
        # Print profile name and password
        if key_content:
            print("{:<30} | {}".format(i, key_content[0]))
        else:
            print("{:<30} | {}".format(i, "No password found"))
    
    except subprocess.CalledProcessError:
        print(f"Error retrieving details for {i}")
        input("")