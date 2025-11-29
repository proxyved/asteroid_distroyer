import tkinter as tk
from tkinter import filedialog
from tkinter import Label, Scale, HORIZONTAL,messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
from rembg import remove
from PIL import Image, ImageTk
import io
import threading

img_path = None
input_image = None
output_image = None
combined_image = None

# Background removal using rembg
def process_image():
    global img_path, output_image
    if not img_path:
        return

    start_loading()

    def worker():
        try:
            with open(img_path, "rb") as f:
                data = f.read()
                removed = remove(data)
            out_img = Image.open(io.BytesIO(removed)).convert("RGBA")
            def on_done():
                global output_image
                output_image = out_img
                update_slider()
                stop_loading()
            root.after(0, on_done)
        except Exception as e:
            def on_error():
                stop_loading()
                messagebox.showerror("Error", f"Processing failed: {e}")
            root.after(0, on_error)

    threading.Thread(target=worker, daemon=True).start()

# Save image krnyasathi fuction 
def save_image():
    global output_image
    if output_image is None:
        return
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if not save_path:
        return  
    try :
        output_image.save(save_path, format="PNG")
        messagebox.showinfo("Success", "Image saved successfully😊!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save image: {e}")

 # Load image (upload button) fiel manegar madhun image select krnyasathi
def upload_image():
    global img_path
    img_path = filedialog.askopenfilename()
    load_input_preview(img_path)

# upload ani DND image cha preview dakhvnyasathi fuction
def load_input_preview(path):
    global input_image
    if not path:
        return

    input_image = Image.open(path).convert("RGBA")
    show_images()

# Drag & Drop function call back krne 
def drop_event(event):
    global img_path
    img_path = event.data.strip("{}")
    load_input_preview(img_path)

#  Before/After slider image sathi function 
def update_slider(value=0):
    global input_image, output_image, combined_image

    if input_image is None or output_image is None:
        return

    # ensure slider value is an int (Scale passes a string)
    try:
        value = int(value)
    except (TypeError, ValueError):
        value = 0

    img1 = input_image.resize((300, 300))
    img2 = output_image.resize((300, 300))

    width = int((value / 100) * 300)

    combined = Image.new("RGBA", (300, 300))
    combined.paste(img1.crop((0, 0, width, 300)), (0, 0))
    combined.paste(img2.crop((width, 0, 300, 300)), (width, 0))

    combined_image = ImageTk.PhotoImage(combined)
    panel_output.config(image=combined_image)
    panel_output.image = combined_image

#  input and empty output dakhavnyasathi function
def show_images():
    if input_image:
        img = input_image.resize((300, 300))
        tk_img = ImageTk.PhotoImage(img)
        panel_input.config(image=tk_img)
        panel_input.image = tk_img

# Loading overlay (appears over output panel while processing)
# (Note: root is created earlier; panel_input/panel_output are created later in GUI SETUP.
#  We create the overlay after panel_output so it can sit on top.)
root = TkinterDnD.Tk()

def start_loading():
    global loading_anim_running
    loading_anim_running = True
    loading_overlay.place(relx=0, rely=0, relwidth=1, relheight=1)
    loading_overlay.lift()

    root.update_idletasks()  # 🔥 IMPORTANT FIX: ensure overlay is rendered immediately

    animate_loading(0)

def animate_loading(i):
    if not loading_anim_running:
        return
    loading_overlay.config(text="Processing" + "." * (i % 4))
    root.after(300, animate_loading, i + 1)

def stop_loading():
    global loading_anim_running
    loading_anim_running = False
    loading_overlay.place_forget()

# GUI SETUP ETHUN STRAT HOTOY 

root.title("VEDANT'S Advanced AI Background Remover (Drag & Drop + Slider)")
root.geometry("750x500")
root.resizable(False, False)

# Labels
Label(root, text="Input (Drop Image Here)", font=("Arial", 14)).place(x=110, y=10)
Label(root, text="Before / After Slider", font=("Arial", 14)).place(x=450, y=10)

# Input and output panels
panel_input = Label(root, bg="#cfcfcf")
panel_input.place(x=50, y=50, width=300, height=300)

panel_output = Label(root, bg="#cfcfcf")
panel_output.place(x=400, y=50, width=300, height=300)

# create loading overlay inside panel_output (so it can be lifted above it)
loading_anim_running = False
loading_overlay = Label(
    panel_output,
    text="Processing",
    bg="#333",
    fg="white",
    font=("Arial", 16),
    anchor="center",
    justify="center",
    wraplength=280,  # keep text inside the panel
)
loading_overlay.place_forget()

# Enable drag-and-drop
panel_input.drop_target_register(DND_FILES)
panel_input.dnd_bind('<<Drop>>', drop_event)

# Buttons (use Segoe UI Emoji so emoji render in color on Windows)
tk.Button(root, text="📁 Upload Image", command=upload_image, width=15, font=("Segoe UI Emoji", 12)).place(x=90, y=380)
tk.Button(root, text="✨ Remove Background", command=process_image, width=20, font=("Segoe UI Emoji", 12)).place(x=290, y=380)
tk.Button(root, text="💾 Save Image", command=save_image, width=15, font=("Segoe UI Emoji", 12)).place(x=520, y=380)
# Slider
slider = Scale(root, from_=0, to=100, orient=HORIZONTAL, length=300, command=update_slider)
slider.set(0)
slider.place(x=400, y=420)

root.mainloop()

#None working code below for reference
# 1> loading animation ready ahhe pn work hot nahi 
# 2> py installer ready ahhe fiel pack krn baki
# 3> GUI styling karu shakto (optional)3