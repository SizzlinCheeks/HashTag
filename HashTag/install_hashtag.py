# Open up the HashTag folder and run this script with 'python3 install_hashtag.py'
# The script will copy the hashtag.py file to the /usr/local/bin directory, rename it to hashtag, and set the necessary permissions.
# After the script finishes, you can use the hashtag command directly from the terminal.

import os
import shutil
import platform

def logo(): # Print the logo
    logo = r"""
      _    _           _    _______ 
     | |  | |         | |  |__   __|
     | |__| | __ _ ___| |__   | | __ _  ____
     |  __  |/ _` / __| '_ \  | |/ _` |/ _  \ 
     | |  | | (_| \__ \ | | | | | (_| | ( ) |
     |_|  |_|\__,_|___/_| |_| |_|\__|_|\__  |
                                        __| |
                                       (____/
               Author: John Hilde
    """
    colored_chars = {
        '_': '\033[95m\033[1m_\033[0m',
        '|': '\033[94m\033[1m|\033[0m',
        '\\': '\033[94m\033[1m\\\033[0m',
        '/': '\033[94m\033[1m/\033[0m',
        '(': '\033[94m\033[1m(\033[0m',
        ')': '\033[94m\033[1m)\033[0m',
        '`': '\033[94m\033[1m`\033[0m',
        'Author: John Hilde': '\033[94m\033[1mAuthor: John Hilde\033[0m'
    }
    
    for char, colored_char in colored_chars.items():
        logo = logo.replace(char, colored_char)
        
    print(logo)
    
def get_platform():
    system = platform.system()
    if system == 'Linux':
        return 'linux'
    elif system == 'Darwin':
        return 'macos'
    elif system == 'Windows':
        return 'windows'
    else:
        return None

def install_hashtag():
    # Define the paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    hashtag_script = os.path.join(current_dir, 'hashtag.py')
    platform_name = get_platform()

    if platform_name is None:
        print("Unsupported operating system.")
        return

    if platform_name == 'linux':
        destination_dir = '/usr/local/bin'
    elif platform_name == 'macos':
        destination_dir = '/usr/local/bin'
    elif platform_name == 'windows':
        destination_dir = os.path.join(os.environ['ProgramFiles'], 'Hashtag')

    destination_file = os.path.join(destination_dir, 'hashtag')

    try:
        # Copy the hashtag.py script to the destination directory
        shutil.copy2(hashtag_script, destination_file)

        # Set the copied file's permissions to be executable (Linux and macOS)
        if platform_name in ['linux', 'macos']:
            os.chmod(destination_file, 0o755)

        print("Installation complete. You can now use 'hashtag' as a command.")
    except Exception as e:
        print(f"An error occurred during installation: {str(e)}")

if __name__ == "__main__":
    logo()
    print("Welcome to the HashTag installer!")
    install_hashtag()
