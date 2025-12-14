#!/usr/bin/env python3
"""
Management script for the Crayon Travel Helper bot.
This script allows you to modify response templates and bot behavior without editing code directly.
"""

import json
import os
from datetime import datetime

def load_config():
    """Load the current configuration from config.py"""
    config_path = "config.py"
    if not os.path.exists(config_path):
        print("config.py not found. Creating a default one...")
        create_default_config()
    # For now, we just return a confirmation that the file exists
    return os.path.exists(config_path)

def create_default_config():
    """Create a default configuration file"""
    default_config = '''# Reddit account credentials
REDDIT_USERNAME = "crayontravel_helper"
REDDIT_PASSWORD = "YOUR_REDDIT_PASSWORD_HERE"

# Reddit API credentials
REDDIT_CLIENT_ID = "YourClientID"
REDDIT_CLIENT_SECRET = "YourClientSecret"

# Bot configuration
REDDIT_USER_AGENT = "TravelBot v1.0 by crayontravel_helper"
TARGET_SUBREDDITS = [
    "travel",
    "solotravel", 
    "TravelHacks",
    "travel_tips",
    "backpacking",
    "digitalnomad",
    "JapanTravel",
    "Tokyo",
    "Paris",
    "ThailandTourism",
    "bali",
    "VisitingIceland",
    "italianlearning",  # travel context
    "EuropeTravelTips"
]  # List of subreddits to monitor
TARGET_STRINGS = [
    "planning",
    "recommend",
    "help with",
    "where should I",
    "best places",
    "tips for",
    "itinerary",
    "visiting",
    "trip advice",
    "travel advice",
    "suggestions",
    "options",
    "overwhelmed",
    "food spots",
    "day trip",
    "must visit",
    "solo travel",
    "first time",
    "beginner"
]  # Keywords to trigger responses
REPLY_TEMPLATES = [
    "That's a great question! Based on my experience, here are some thoughts...",
    "Hey there! I've been to that destination and can definitely help. Here's what I recommend...",
    "I had a similar question recently and learned a lot about this. Here's what helped me...",
    "Great topic! Here are some tips that might be helpful for your situation...",
    "Based on what you're looking for, I'd suggest..."
]  # Generic starter templates

# Bot behavior configuration
SLEEP_DURATION = 60  # Adjust the sleep duration as needed in seconds (1 minute)
MIN_KARMA_THRESHOLD = 500  # Target karma threshold before increasing activity
MAX_COMMENTS_PER_SESSION = 10  # Max comments to engage with per session
MAX_REPLY_PER_POST = 2  # Max replies per post to avoid spam detection
'''
    with open("config.py", "w", encoding="utf-8") as f:
        f.write(default_config)
    print("Default config.py created successfully!")

def modify_target_subreddits():
    """Modify the list of target subreddits"""
    print("\nCurrent target subreddits:")
    with open("config.py", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract current subreddits 
    start_idx = content.find("TARGET_SUBREDDITS = [") + len("TARGET_SUBREDDITS = [")
    end_idx = content.find("]  # List of subreddits to monitor")
    current_subreddits_str = content[start_idx:end_idx]
    
    # Parse the subreddits
    subreddits = []
    for line in current_subreddits_str.split('\n'):
        line = line.strip()
        if line.startswith('"') and line.endswith('"'):
            subreddits.append(line[1:-1])
    
    for i, sub in enumerate(subreddits):
        print(f"{i+1}. {sub}")
    
    print("\nOptions:")
    print("1. Add a subreddit")
    print("2. Remove a subreddit")
    print("3. Replace all subreddits")
    print("4. Go back")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        new_sub = input("Enter subreddit name: ")
        subreddits.append(new_sub)
        print(f"Added {new_sub} to target subreddits")
    elif choice == "2":
        idx = int(input("Enter the number of the subreddit to remove: ")) - 1
        if 0 <= idx < len(subreddits):
            removed = subreddits.pop(idx)
            print(f"Removed {removed} from target subreddits")
        else:
            print("Invalid number")
            return
    elif choice == "3":
        new_list = input("Enter subreddits separated by commas: ")
        subreddits = [s.strip() for s in new_list.split(",")]
        print("Replaced all subreddits")
    elif choice == "4":
        return
    else:
        print("Invalid choice")
        return
    
    # Update the config file
    update_config_section(content, "TARGET_SUBREDDITS", subreddits, "List of subreddits to monitor")

def modify_target_strings():
    """Modify the list of target strings/keywords"""
    print("\nCurrent target strings:")
    with open("config.py", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract current strings 
    start_idx = content.find("TARGET_STRINGS = [") + len("TARGET_STRINGS = [")
    end_idx = content.find("]  # Keywords to trigger responses")
    current_strings_str = content[start_idx:end_idx]
    
    # Parse the strings
    strings = []
    for line in current_strings_str.split('\n'):
        line = line.strip()
        if line.startswith('"') and line.endswith('"'):
            strings.append(line[1:-1])
    
    for i, s in enumerate(strings):
        print(f"{i+1}. {s}")
    
    print("\nOptions:")
    print("1. Add a keyword")
    print("2. Remove a keyword")
    print("3. Replace all keywords")
    print("4. Go back")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == "1":
        new_str = input("Enter keyword: ")
        strings.append(new_str)
        print(f"Added {new_str} to target strings")
    elif choice == "2":
        idx = int(input("Enter the number of the keyword to remove: ")) - 1
        if 0 <= idx < len(strings):
            removed = strings.pop(idx)
            print(f"Removed {removed} from target strings")
        else:
            print("Invalid number")
            return
    elif choice == "3":
        new_list = input("Enter keywords separated by commas: ")
        strings = [s.strip() for s in new_list.split(",")]
        print("Replaced all keywords")
    elif choice == "4":
        return
    else:
        print("Invalid choice")
        return
    
    # Update the config file
    update_config_section(content, "TARGET_STRINGS", strings, "Keywords to trigger responses")

def update_config_section(content, section_name, new_values, comment):
    """Helper to update a list section in the config file"""
    # Format the new values
    formatted_values = []
    for value in new_values:
        formatted_values.append(f'    "{value}",')
    
    # Remove the trailing comma from the last item
    if formatted_values:
        formatted_values[-1] = formatted_values[-1][:-1]  # Remove last comma
    
    new_content = '\n'.join(formatted_values)
    
    # Find and replace the section
    start_marker = f"{section_name} = ["
    end_marker = f"]  # {comment}"
    
    start_idx = content.find(start_marker) + len(start_marker)
    end_idx = content.find(end_marker)
    
    updated_content = content[:start_idx] + f"\n{new_content}\n" + content[end_idx:]
    
    with open("config.py", "w", encoding="utf-8") as f:
        f.write(updated_content)
    
    print(f"{section_name} updated successfully!")

def modify_behavior_settings():
    """Modify the bot's behavior settings"""
    print("\nCurrent behavior settings:")
    with open("config.py", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract current settings
    sleep_duration = extract_variable(content, "SLEEP_DURATION")
    max_comments = extract_variable(content, "MAX_COMMENTS_PER_SESSION")
    max_reply = extract_variable(content, "MAX_REPLY_PER_POST")
    
    print(f"1. Sleep duration between sessions: {sleep_duration} seconds")
    print(f"2. Max comments per session: {max_comments}")
    print(f"3. Max replies per post: {max_reply}")
    
    choice = input("\nWhich setting would you like to change? (1-3, or 'back'): ")
    
    if choice == "1":
        new_value = input(f"Current: {sleep_duration}. Enter new sleep duration in seconds: ")
        try:
            new_value = int(new_value)
            update_variable(content, "SLEEP_DURATION", new_value, 
                           "Adjust the sleep duration as needed in seconds")
        except ValueError:
            print("Please enter a valid number")
    elif choice == "2":
        new_value = input(f"Current: {max_comments}. Enter new max comments per session: ")
        try:
            new_value = int(new_value)
            update_variable(content, "MAX_COMMENTS_PER_SESSION", new_value,
                           "Max comments to engage with per session")
        except ValueError:
            print("Please enter a valid number")
    elif choice == "3":
        new_value = input(f"Current: {max_reply}. Enter new max replies per post: ")
        try:
            new_value = int(new_value)
            update_variable(content, "MAX_REPLY_PER_POST", new_value,
                           "Max replies per post to avoid spam detection")
        except ValueError:
            print("Please enter a valid number")
    elif choice == "back":
        return
    else:
        print("Invalid choice")

def extract_variable(content, var_name):
    """Extract a variable's value from config content"""
    start_idx = content.find(f"{var_name} = ") + len(f"{var_name} = ")
    end_idx = content.find("\n", start_idx)
    value = content[start_idx:end_idx].strip()
    # Remove comments
    if "#" in value:
        value = value.split("#")[0].strip()
    return value

def update_variable(content, var_name, new_value, comment):
    """Update a variable in the config file"""
    start_marker = f"{var_name} = "
    end_idx = content.find("\n", content.find(start_marker))
    
    # Find the end of the line containing the comment
    if "#" in content[content.find(start_marker):end_idx]:
        end_idx = content.find("\n", end_idx)
    
    updated_content = (content[:content.find(start_marker) + len(start_marker)] + 
                      f"{new_value}  # {comment}\n" + 
                      content[end_idx:])
    
    with open("config.py", "w", encoding="utf-8") as f:
        f.write(updated_content)
    
    print(f"{var_name} updated successfully!")

def view_logs():
    """View recent log entries"""
    log_file = "comments_replied_to.txt"
    if os.path.exists(log_file):
        print(f"\nRecent log entries from {log_file}:")
        with open(log_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            # Show last 10 entries
            for line in lines[-10:]:
                print(line.strip())
    else:
        print(f"\nLog file {log_file} not found")

def setup_hf_integration():
    """Help user set up Hugging Face integration"""
    print("\nHugging Face Integration Setup")
    print("="*35)
    print("1. To enable AI-powered contextual responses, you need a Hugging Face token")
    print("2. Get your token from: https://huggingface.co/settings/tokens")
    print("3. Set the HF_TOKEN environment variable with your token")
    print("4. Optionally set HF_MODEL to use a specific model (default: Qwen/Qwen2.5-7B-Instruct)")
    print("\nRecommended models:")
    print("- Qwen/Qwen2.5-7B-Instruct (default - good balance)")
    print("- meta-llama/Llama-3.1-8B-Instruct (high quality)")
    print("- teknium/OpenHermes-2.5-Mistral-7B (natural conversation)")
    print("- microsoft/Phi-3-mini-4k-instruct (lightweight)")

    setup_choice = input("\nWould you like to learn more about setting environment variables? (y/n): ")
    if setup_choice.lower() == 'y':
        print("\nSetting Environment Variables:")
        print("Windows:")
        print("  set HF_TOKEN=your_token_here")
        print("  set HF_MODEL=Qwen/Qwen2.5-7B-Instruct  # optional")
        print("\nLinux/Mac:")
        print("  export HF_TOKEN=your_token_here")
        print("  export HF_MODEL=Qwen/Qwen2.5-7B-Instruct  # optional")

def main_menu():
    """Display the main menu and handle user choices"""
    while True:
        print("\n" + "="*50)
        print("CRAYON TRAVEL HELPER BOT - MANAGEMENT INTERFACE")
        print("="*50)
        print("1. Modify target subreddits")
        print("2. Modify target keywords")
        print("3. Modify behavior settings")
        print("4. View recent activity logs")
        print("5. Hugging Face integration setup")
        print("6. Run the bot")
        print("7. Exit")

        choice = input("\nSelect an option (1-7): ")

        if choice == "1":
            modify_target_subreddits()
        elif choice == "2":
            modify_target_strings()
        elif choice == "3":
            modify_behavior_settings()
        elif choice == "4":
            view_logs()
        elif choice == "5":
            setup_hf_integration()
        elif choice == "6":
            print("Starting the bot...")
            import reddit_bot
            # Note: This won't actually start the bot in a loop here
            # It's just for demonstration purposes
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-7.")

if __name__ == "__main__":
    if load_config():
        print("Crayon Travel Helper Bot Management Interface")
        main_menu()
    else:
        print("Error: Could not load configuration. Please check config.py")