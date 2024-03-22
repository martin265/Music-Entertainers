import time
import pyautogui


def auto_text_typer(text, interval=0.1):
    """
    Automatically types the given text with the specified interval.

    Parameters:
    - text (str): The text to be typed.
    - interval (float): The interval between each key press.
    """
    time.sleep(5)  # Give some time to switch to the input field or application
    for char in text:
        pyautogui.write(char)
        time.sleep(interval)


# Example usage:
text_to_type = "Hello, this is an auto text typer using Python!"
auto_text_typer(text_to_type)
