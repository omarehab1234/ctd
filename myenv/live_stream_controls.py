import tkinter as tk
import cv2


root = tk.Tk()
root.geometry("800x500")
root.title('Hi')
fram1 = tk.Frame(root,bg="#1a5276",width=800,height=500)
fram1.place(x=0,y=0)
manuals = tk.Label(fram1,text=" Press G: Toggle Grayscale | Press R: Record 5s Video | Press Q: Quit",font=("Arial",11),fg="#58d68d",bg="#1a5276")
manuals.place(x=180,y=10)
start_button = tk.Button(fram1, text="Start Recording",width="25",height="2",bg="#d4ac0d",cursor="hand2")
start_button.place(x=600,y=50)
toG2Rgb = tk.Button(fram1, text="Toggle Grayscale",width="25",height="2",bg="#d4ac0d",cursor="hand2")
toG2Rgb.place(x=600,y=120)
quiton = tk.Button(fram1, text="Quit",width="25",height="2",bg="#d4ac0d",cursor="hand2",command=quit)
quiton.place(x=600,y=190)
cv2.VideoCapture(5)
root.mainloop()