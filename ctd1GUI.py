import tkinter as tk
from tkinter import messagebox
import hashlib

def password_check():#for check for the password
    user_pass = hashlib.md5(feild_pass.get().encode('utf-8')).hexdigest()
    hash = hashlib.md5()
    hash.update("SuperHardPassword99".encode('utf-8'))
    the_pass = hash.hexdigest()
    
    
    if user_pass == the_pass :
        return True
    else:
        messagebox.showerror("Invalid password", "check your password")
        feild_pass.delete(0,tk.END)
        return False
    

def checking_name_pass():
    symbols =['`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|','\\',':',';','"','\'','<',',','>','.','?','/']
    user_name = feild_user.get()

    # here to check if he contain any of the symbols
    for i in symbols:   
        if i in user_name:
            feild_user.delete(0, tk.END)
            return
    if user_name == "guest":
        if password_check():
            messagebox.showinfo("Welcome", "Welcome to our system")
        
        
    else:
        messagebox.showerror("Invalid user name", "check your user name")
        feild_user.delete(0,tk.END)
        return
    
    
root = tk.Tk()
root.title("Login")
root.geometry("700x500")
lb_user = tk.Label(root, text="Username: ",font=("Arial" , 12))
lb_user.grid(row=0, column=0, padx=10, pady=20, sticky="w")  # Label in row 0, column 0
feild_user = tk.Entry(root,width="30")
feild_user.grid(row=0, column=1, padx=10, pady=20)  # Entry in row 0, column 1

# Password Field
lb_pass = tk.Label(root, text="Password: ",font=("Arial" , 12))
lb_pass.grid(row=1, column=0, padx=10, pady=10, sticky="w")  # Label in row 1, column 0
feild_pass = tk.Entry(root, width="30")
feild_pass.grid(row=1, column=1, padx=10, pady=10)  # Entry in row 1, column 1

button = tk.Button(root, text="Login",width="20" ,font=("Arial",12),background="grey",cursor="heart",command=checking_name_pass)
button.grid(row=2, column=2, padx=10, pady=10)
root.mainloop()