import struct
import pygame
from tkinter import filedialog

def load_t1nklas(filename):
    """Load .t1nklas image data."""
    with open(filename, "rb") as f:
        magic = f.read(4)
        if magic != b"T1NK":
            raise ValueError("Invalid file format")
        
        width, height, depth = struct.unpack("<HHB", f.read(5))
        pixels = list(struct.iter_unpack("BBBB", f.read(width * height * 4)))
        
        return width, height, depth, pixels

def create_dark_gray_surface(width, height):
    """Create a dark gray surface."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    dark_gray = (30, 30, 30, 255)  # Dark gray color
    surface.fill(dark_gray)
    return surface

def view_t1nklas():
    """Open a file dialog to select and view a .t1nklas image."""
    file_path = filedialog.askopenfilename(filetypes=[("T1NKLAS Files", "*.t1nklas")])
    if not file_path:
        print("No file selected.")
        return
    
    width, height, _, pixels = load_t1nklas(file_path)
    
    # Initialize Pygame
    pygame.init()
    
    # Set the initial window size
    window_width, window_height = 800, 600
    
    screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
    pygame.display.set_caption("T1NKLAS Viewer")
    
    # Create the image surface once
    image_surface = pygame.image.frombuffer(bytearray([component for pixel in pixels for component in pixel]), (width, height), "RGBA")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                window_width, window_height = event.w, event.h
                screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
        
        dark_gray_surface = create_dark_gray_surface(window_width, window_height)
        screen.blit(dark_gray_surface, (0, 0))
        
        scale_factor = min(window_width / width, window_height / height)
        scaled_width = int(width * scale_factor)
        scaled_height = int(height * scale_factor)
        
        # Scale the image surface to fit the new window size
        scaled_surface = pygame.transform.scale(image_surface, (scaled_width, scaled_height))
        
        # Center the scaled surface on the screen
        x_offset = (window_width - scaled_width) // 2
        y_offset = (window_height - scaled_height) // 2
        screen.blit(scaled_surface, (x_offset, y_offset))
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    view_t1nklas()
