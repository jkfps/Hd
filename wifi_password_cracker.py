import random
import string

# The name of the Wi-Fi network you want to connect to
network_name = "your_network_name"

# The minimum and maximum length of the random passwords
password_min_length = 8
password_max_length = 16

# The number of random passwords to try
num_passwords = 10

# A list of all possible characters that can be used in the password
characters = string.ascii_letters + string.digits

# Try a number of random passwords
for i in range(num_passwords):
  # Generate a random password
  password = ''.join(random.choice(characters) for j in range(random.randint(password_min_length, password_max_length)))

  # Attempt to connect to the Wi-Fi network using the random password
  command = f"wpa_supplicant -B -i wlan0 -c <(wpa_passphrase '{network_name}' '{password}')"
  result = subprocess.run(command, shell=True, check=True)

  # If the connection was successful, print a message and exit
  if result.returncode == 0:
    print(f"Connected to network '{network_name}' with password '{password}'")
    exit(0)

# If no connection was successful, print an error message and exit
print(f"Failed to connect to network '{network_name}' after trying {num_passwords} random passwords")
exit(1)