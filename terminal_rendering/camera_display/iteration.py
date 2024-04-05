import cv2
import numpy as np
import colorama
from colorama import Back, Style
import os

colorama.init()

def convert_to_ansi(image):
    height, width, _ = image.shape
    ansi_frame = ""
    for y in range(height):
        for x in range(width):
            b, g, r = image[y, x]  
            ansi_code = f"\033[48;2;{r};{g};{b}m "  
            ansi_frame += ansi_code
        ansi_frame += "\n"
    return ansi_frame

def display_video():
    cap = cv2.VideoCapture(0)  
    terminal_width = os.get_terminal_size().columns
    terminal_height = os.get_terminal_size().lines
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        scaled_frame = cv2.resize(frame, (terminal_width, terminal_height), interpolation=cv2.INTER_NEAREST)
        ansi_frame = convert_to_ansi(scaled_frame)
        print(ansi_frame, end="")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    display_video()