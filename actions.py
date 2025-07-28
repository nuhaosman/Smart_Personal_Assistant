import webbrowser                     # For opening URLs
# import pyautogui                      # For screenshots and automation
import subprocess                     # To launch applications like Word
import screen_brightness_control as sbc  # Brightness control
import os                             # For executing system commands

# Function to perform system actions based on recognized intent
def perform_action(intent, query):
    try:
        if intent == "googleSearch":
            # Extract search term and open Google search
            search_term = query.split("search")[-1]
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
            return "Performed Google search."
        
        elif intent == "youtubeSearch":
            # Extract term and open YouTube search
            term = query.split("youtube")[-1]
            webbrowser.open(f"https://www.youtube.com/results?search_query={term}")
            return "Searched YouTube."
        
        elif intent == "downloadMusic":
            # Placeholder – not implemented
            return "Music download placeholder – not implemented."
        
        elif intent == "startWordProject":
            # Launch Microsoft Word
            subprocess.Popen(["start", "winword"], shell=True)
            return "Opened Microsoft Word."
        
        elif intent == "screenShot":
            # Take and save screenshot
            filename = "assets/screenshots/screenshot.png"
            pyautogui.screenshot().save(filename)
            return f"Screenshot saved: {filename}"
        
        elif intent == "lowerBrightness":
            # Reduce screen brightness
            sbc.set_brightness(30)
            return "Lowered screen brightness."
        
        elif intent == "higherBrightness":
            # Increase screen brightness
            sbc.set_brightness(80)
            return "Increased screen brightness."
        
        elif intent == "highVolume":
            # Set system volume to max (using NirCmd)
            os.system("nircmd.exe setsysvolume 65535")
            return "Volume set to high."
        
        elif intent == "lowVolume":
            # Set system volume to low
            os.system("nircmd.exe setsysvolume 1000")
            return "Volume set to low."
        
        else:
            return "Unknown command."
    
    except Exception as e:
        return f"Error performing action: {e}"
