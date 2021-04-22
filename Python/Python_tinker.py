import tkinter as tk
import cv2
from PIL import ImageTk, Image
import PIL
from threading import Thread

def open_camera():
	cap = cv2.VideoCapture(0)

	def show_camera():
		_, frame = cap.read()
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
		img_from_array = PIL.Image.fromarray(frame)
		imgtk = ImageTk.PhotoImage(image = img_from_array)
		lb_camera.imgtk = imgtk
		lb_camera.configure(image=imgtk)
		lb_camera.after(10, show_camera)

	threadShowCam=Thread(target=show_camera)
	threadShowCam.start()



root = tk.Tk()
root.title('Face Recognition')
root.geometry("+30+30")

canvas = tk.Canvas(root, height=700, width=1300)
canvas.pack()

left_frame = tk.Frame(root)
left_frame.place(relwidth=0.4, relheight=1)

right_frame = tk.Frame(root)
right_frame.place(relwidth=0.6, relheight=1, relx=0.4)

lb_camera = tk.Label(right_frame)
lb_camera.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

btn_open_cam = tk.Button(left_frame, text = 'OPEN CAMERA', font=("Courier, 24"), command = open_camera)
btn_open_cam.place(relx=0.2, rely=0.2)

root.mainloop()
cv2.destroyAllWindows()