# IMAGE CLASSIFICATION BOT USING RESNET50 MODEL
# REQUAIRED LIBRARIES: tensorflow, keras, numpy, pillow, tkinter
import tkinter as tk
from tkinter import filedialog, Label, Button
from PIL import Image, ImageTk
import numpy as np
import threading

#CHILL IF YOU GETTING WARNING RELATED TO TENSORFLOW IT WILL NOT AFFECT THE FUNCTIONALITY
#EVEN I ALSO DONT KNOW WHY IT IS SHOWING THAT WARNING
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

# ------------------ GLOBAL VARIABLES ------------------
model = None
predicting = False
_animate_index = 0

img_path = None


# ------------------ FUNCTIONS ------------------

# FUNCTION TO UPLOAD IMAGE
# BY ASKOPEN DO GI5VE ACCESS TO FILE EXPLORER
def upload_image():
    global img_path
    img_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )

    if img_path:
        img = Image.open(img_path)
        img = img.resize((420, 260))
        img = ImageTk.PhotoImage(img)

        image_label.config(image=img)
        image_label.image = img

        result_label.config(text="Image loaded ✅\nClick Predict")


'''HERE IS THE MAIN  FUNCTION OF ALL PROJECT WHICH MANAGE FROM
 LOADING MODEL PROCESS I6MAGE AND DISPLAYING RESULT'''


def predict_image():
    global predicting, _animate_index

    if img_path is None:
        result_label.config(text="⚠ Please upload an image first")
        return

    # Start background prediction so the UI can animate
    def _worker():
        global model, predicting
        try:
            # Prepare image
            img = image.load_img(img_path, target_size=(224, 224))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)

            # Load model if needed
            if model is None:
                model = ResNet50(weights="imagenet")

            # Predict
            preds = model.predict(img_array)
            decoded = decode_predictions(preds, top=3)[0]

            result_text = "\n🏆 Top 3 Predictions:\n\n"
            for i, (imagenet_id, name, prob) in enumerate(decoded, start=1):
                result_text += f"{i}. {name} → {prob*100:.2f}%\n"

            # Show result on main thread
            root.after(0, lambda: result_label.config(text=result_text))
        except Exception as e:
            root.after(0, lambda: result_label.config(text=f"Error: {e}"))
        finally:
            predicting = False

    predicting = True
    _animate_index = 0
    threading.Thread(target=_worker, daemon=True).start()
    _animate_predicting()


# ------------------ GUI DESIGN ETHUN SURU ------------------

#BASE WINDOW SETTING
root = tk.Tk()
root.title("Image Classification Bot - ResNet50")
root.geometry("760x600")
root.configure(bg="#1e1e2f")

# TITLE LABEL
title = Label(
    root,
    text="Image Classification Bot",
    font=("Helvetica", 22, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=20)

# Use a fixed-size frame (pixels) for the image so it doesn't push other widgets off-screen
image_frame = tk.Frame(root, bg="#2a2a3d", width=420, height=260)
image_frame.pack(pady=18)
image_frame.pack_propagate(False)
image_label = Label(image_frame, bg="#2a2a3d")
image_label.pack(expand=True)

# BUTTON CREATING AND POSITIONING (wider, less tall)
button_frame = tk.Frame(root, bg="#1e1e2f")
button_frame.pack(pady=12)

# Hover  and cursor settings
upload_bg = "#4CAF50"
upload_hover = "#45A049"
predict_bg = "#2196F3"
predict_hover = "#1e88e5"

def _on_enter(btn, hover_color):
    try:
        btn.config(bg=hover_color, cursor="hand2")
    except Exception:
        pass

def _on_leave(btn, normal_color):
    try:
        btn.config(bg=normal_color, cursor="arrow")
    except Exception:
        pass

#UPLOAD BUTTON CHI FRAMING ANI STYLING 
upload_btn = Button(
    button_frame,
    text="📁  Upload Image",
    command=upload_image,
    font=("Helvetica", 13),
    bg=upload_bg,
    fg="white",
    width=18,
    height=1,
    relief="flat",
    bd=0,
    activebackground=upload_hover
)

#UPLOAD BUTTON CHYA HO5VER EFFECT SATHI
upload_btn.pack(side="left", padx=10)
upload_btn.bind("<Enter>", lambda e: _on_enter(upload_btn, upload_hover))
upload_btn.bind("<Leave>", lambda e: _on_leave(upload_btn, upload_bg))


#PREDICT CHI FRAMMING AANI STYLING
predict_btn = Button(
    button_frame,
    text="⚡  Predict",
    command=predict_image,
    font=("Helvetica", 13),
    bg=predict_bg,
    fg="white",
    width=18,
    height=1,
    relief="flat",
    bd=0,
    activebackground=predict_hover
)

#HOVERING EFFECT SATHI 
predict_btn.pack(side="left", padx=10)
predict_btn.bind("<Enter>", lambda e: _on_enter(predict_btn, predict_hover))
predict_btn.bind("<Leave>", lambda e: _on_leave(predict_btn, predict_bg))
result_label = Label(
    root,
    text="Upload an image to start",
    font=("Helvetica", 14),
    bg="#1e1e2f",
    fg="white",
    justify="left"
)
result_label.pack(pady=25)

# PREDICTING ANIMATION SATHI 
def _animate_predicting():
    global _animate_index, predicting
    if not predicting:
        return
    dots = ("", ".", "..", "...")
    text = f"🔍 Predicting{dots[_animate_index % len(dots)]}"
    result_label.config(text=text)
    _animate_index += 1
    root.after(400, _animate_predicting)

root.mainloop()