from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

gui = Tk()
gui.geometry("480x480")
gui.title("GUI LOGIN")


icon = PhotoImage(file='Icon.png')
gui.iconphoto(True,icon)
gui.config(background='#333333')


def signin():
    import mysql.connector

    # Koneksi database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1843322Abc?",
        database="school"
    )

    mycursor = mydb.cursor()

    # Mengambil input GUI
    username = user_entry.get()
    password = password_entry.get()

    sql = """
        SELECT * FROM login_siswa
        WHERE Nama = %s AND Password = %s
    """

    mycursor.execute(sql, (username, password))

    result = mycursor.fetchone()

    if result:
        messagebox.showinfo(title="Login", message="You Successfully Logged In")
                # Mengosongkan input
        user_entry.delete(0, 'end')
        password_entry.delete(0, 'end')
    else:
        print("Username atau password salah")

    mycursor.close()
    mydb.close()
    
    
#Halaman Awal#
frame = Frame(bg='#333333')
Login_label = Label(frame, 
                    text='Login', 
                    font=("Arial", 25, "bold"), 
                    fg='white', bg='#333333')
user_label = Label(frame, 
                   text='Ussername',
                   font=("Arial", 16),
                   fg='white', bg='#333333')
user_entry  = Entry(frame, font=("Arial", 16))
password_label = Label(frame, 
                       text='Password',
                       font=("Arial", 16), 
                       fg='white', bg='#333333')
password_entry = Entry(frame, 
                       show='*', 
                       font=("Arial", 16))
login_button = Button(frame, 
                      text='LOGIN',
                      font=("Arial", 16), 
                      fg='white', bg='#FF3399', 
                      command=signin)
signup_label = Label(frame, 
                     text='tekan signup apaila belum memiliki akun', 
                     font=("Arial", 8),
                     fg='white', bg='#333333')
signup_button = Button(frame, 
                       text='SignUp', 
                       font=("Arial", 8), 
                       fg='white', bg='#FF3399',)
#Place#
Login_label.grid(row=0,column=1,pady=16)
user_label.grid(row=1,column=0)
user_entry.grid(row=1,column=1)
password_label.grid(row=2,column=0)
password_entry.grid(row=2,column=1)
login_button.grid(row=4,column=1, pady=16)
signup_label.grid(row=6, column=1)
signup_button.grid(row=6,column=2)


frame.pack()


gui.mainloop()