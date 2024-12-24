import tkinter as tk
import cv2
import time

vid_temp = True
# here to start recording 7elw zy el fol
def start_record():
    
    vid = cv2.VideoCapture(0)
    if vid.isOpened():
        print("Camera opened successfully.")
    
        fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        cap = cv2.VideoWriter('cap.mp4', fourcc, 20.0, (640,480))
        time_s = time.time()
        
        time.sleep(1) 
        while time.time() - time_s < 5:
            isTrue, frame = vid.read()
            if not isTrue:
                print("Failed to grab frame.")
                break
            else:
                cv2.imshow('frame', frame)
                cap.write(frame)
                
            if cv2.waitKey(20) & 0xff == ord("d"):
                print("got broke")
                break 
    
        vid.release()
        cap.release()   
            

    
def change():
    global vid_temp
    cv2.destroyAllWindows()
    vid_path = r"cap.mp4"
    vid = cv2.VideoCapture(vid_path)
    
    if not vid.isOpened():
        print("Failed to open the recorded video.")
        return
    
    time.sleep(2)
    # hena el gray scale vid
    if vid_temp:
        vid_temp = False
        while True:
            isTrue, frame = vid.read()
            gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            if not isTrue:
                print("End of video.")
                break
            cv2.imshow("Recorded Video", gray_frame)
            if cv2.waitKey(20) & 0xff == ord("d"):
                print("got broke")
                break
    # hena el vedio el 3ady
    else:
        vid_temp = True
        while True:
            isTrue, frame = vid.read()
            if not isTrue:
                print("End of video.")
                break
            cv2.imshow("Recorded Video", frame)
            if cv2.waitKey(20) & 0xff == ord("d"):
                print("got broke")
                break
        

        
#3shan nekasar el root 
def destroy_root():
    root.quit()
    
root = tk.Tk()
root.geometry("800x500")
root.title('Hi')
fram1 = tk.Frame(root,bg="#1a5276",width=800,height=500)
fram1.place(x=0,y=0)
manuals = tk.Label(fram1,text=" Press G: Toggle Grayscale | Press R: Record 5s Video | Press Q: Quit",font=("Arial",11),fg="#58d68d",bg="#1a5276")
manuals.place(x=180,y=10)

start_button = tk.Button(fram1, text="Start Recording",width="25",height="2",bg="#d4ac0d",cursor="hand2",command = start_record)
start_button.place(x=600,y=50)
root.bind('r', lambda event: start_record())  # 'd' key to start recording

# hena el rbg to gray aw el 3aks
toG2Rgb = tk.Button(fram1, text="Toggle Grayscale",width="25",height="2",bg="#d4ac0d",cursor="hand2", command = change)
toG2Rgb.place(x=600,y=120)
root.bind("g",lambda event: change())  # 'g' key to toggle grayscale


# hena 3shan nekfel el root
quiton = tk.Button(fram1, text="Quit",width="25",height="2",bg="#d4ac0d",cursor="hand2",command=destroy_root)
quiton.place(x=600,y=190)

root.bind('q',lambda event: destroy_root())

cv2.waitKey(0)
root.mainloop()
