import pygame
import sys
import pyperclip
from pytube import YouTube
import moviepy.editor as mp
import tkinter as tk
from tkinter import filedialog
def convert_video_to_audio():
    root = tk.Tk()
    root.withdraw() 
    video_path = filedialog.askopenfilename(
        title="Select a Video File",
        filetypes=[("Video files", "*.mp4 *.mov *.avi *.mkv"), ("All files", "*.*")]
    )
    if not video_path:
        print("No file selected. Exiting.")
        return
    output_dir = filedialog.askdirectory(title="Select Output Directory")
    if not output_dir:
        print("No output directory selected. Exiting.")
        return
    file_name = video_path.split("/")[-1].split(".")[0]
    audio_path = f"{output_dir}/{file_name}.mp3"

    clip = mp.VideoFileClip(video_path)
    clip.audio.write_audiofile(audio_path)

    print(f"Audio file saved as: {audio_path}")
def download(link):
    TubeObject = YouTube(link)
    TubeObject = TubeObject.streams.get_highest_resolution()
    try:
        TubeObject.download()
        print("Success!\nYou have succesfully downloaded the YouTube video!")
    except:
        ValueError
        print("ERROR. ERROR. ERROR\nUnsupported input type")
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Video Audio App")
font = pygame.font.Font(None, 36)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
MP3_HEIGHT = screen.get_height()
MP3_WIDTH = screen.get_width()
input_box = pygame.Rect(200, 125, 500, 40)
color_inactive = pygame.Color(0, 255, 0)
color_active = pygame.Color(50, 200, 0)
color = color_inactive
active = False
text = ''
smallfont = pygame.font.SysFont('Arial',35)
smallerfont = pygame.font.SysFont('Arial', 15)
instruction = smallfont.render('Paste Youtube link to Download!!' , True , (0, 200, 200))
subtitle = smallerfont.render('psst, Make sure to exit the program after entering the link', True, (0, 150, 150))
conversion = smallfont.render('Convert MP4 to MP3' , True , (255, 0, 0))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False     
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ((MP3_WIDTH//2)-175) <= mouse[0] <= ((MP3_WIDTH//2)+200) and ((MP3_HEIGHT//2)+100) <= mouse[1] <= ((MP3_HEIGHT//2)+140): 
                convert_video_to_audio() 
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    print(text)
                    link = text
                    text = ''
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_v and (pygame.key.get_mods() & pygame.KMOD_CTRL):
                    text += pyperclip.paste()
                else:
                    text += event.unicode
    mouse = pygame.mouse.get_pos()
    screen.fill((60, 25, 60))
    txt_surface = font.render(text, True, color)
    width = max(200, txt_surface.get_width()+10)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
    screen.blit(instruction, (input_box.x-125, input_box.y-80))
    screen.blit(subtitle, (input_box.x-80, input_box.y-30))
    screen.blit(conversion , ((MP3_WIDTH//2)-175,(MP3_HEIGHT//2)+100))
    pygame.draw.rect(screen, color, input_box, 2)
    pygame.display.update()
    pygame.display.flip()
pygame.quit()
download(link)
sys.exit()