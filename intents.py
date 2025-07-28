# This module detects the user's intent using keyword rules

def get_intent(text):
    text = text.lower()  # Convert to lowercase for consistent matching
    
    # Match commands to predefined intent labels
    if "search" in text and "google" in text:
        return "googleSearch"
    elif "youtube" in text:
        return "youtubeSearch"
    elif "music" in text:
        return "downloadMusic"
    elif "word" in text:
        return "startWordProject"
    elif "screenshot" in text:
        return "screenShot"
    elif "lower brightness" in text:
        return "lowerBrightness"
    elif "higher brightness" in text:
        return "higherBrightness"
    elif "high volume" in text:
        return "highVolume"
    elif "low volume" in text:
        return "lowVolume"
    else:
        return None  # Not a known system command
