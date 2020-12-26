import subprocess
import sys
import time
import os
from tkinter import *
import subprocess as Popen
import subprocess as sp
from tkinter import messagebox




class Window(Tk):
    def __init__ (self):
        super(Window, self).__init__()
        self.title("TerminalCreeds Icloud Bypass Tool Free ")
        self.minsize(900,600)
        self.resizable(0,0)
        self.Design()
        self.Buttons()
        self.Prompt()
        
    def Prompt(self):
        self.msg= messagebox.showinfo("TerminalCreeds Icloud Bypass Tool", "Please Make Sure Your Iphone Is Connected To Pc")
        time.sleep(3)
    def Design(self):
    
        device_name=subprocess.Popen(['ideviceinfo -k UniqueDeviceID '], shell=True, stdout=subprocess.PIPE)
        subprocess_return = device_name.stdout.read()

        device_name=subprocess.Popen(['ideviceinfo -k SerialNumber '], shell=True, stdout=subprocess.PIPE)
        subprocess_return1 = device_name.stdout.read()

        imei=subprocess.Popen(['ideviceinfo -k  InternationalMobileEquipmentIdentity'], shell=True, stdout=subprocess.PIPE)
        subprocess_return2 = imei.stdout.read()

        udid=subprocess.Popen(['ideviceinfo -k  ActivationState'], shell=True, stdout=subprocess.PIPE)
        subprocess_return4 = udid.stdout.read()

        product=subprocess.Popen(['ideviceinfo -k  ProductType'], shell=True, stdout=subprocess.PIPE)
        subprocess_return6 = product.stdout.read()
        self.label= Label(self, text="TERMINAL", fg= "Black", bg="white",font=("Times New Roman", 20))
        self.label.place(x=10, y=10)

        self.label1=Label(self, text="CREEDS",fg="red",bg="white", font=("Times New Roman", 20)) 
        self.label1.place(x=151, y=10) 

        self.label2=Label(self, text="UDID",fg="red",bg="white", font=("Times New Roman", 20) )
        self.label2.place(x=100, y=100)
       
        self.label3=Label(self, text="IMEI",fg="red",bg="white", font=("Times New Roman", 20) )
        self.label3.place(x=470, y=100)
       
        self.label4=Label(self, text="SERIAL",fg="red",bg="white", font=("Times New Roman", 20) )
        self.label4.place(x=100, y=150)
       
        self.label5=Label(self, text="ACTIVATION STATUS",fg="red",bg="white", font=("Times New Roman", 20) )
        self.label5.place(x=470, y=150)
        
        self.label6=Label(self, text="PRODUCT",fg="red",bg="white", font=("Times New Roman", 20) )
        self.label6.place(x=100, y=200)

        self.label5=Label(self, text=subprocess_return4,fg="black", font=("Times New Roman", 11) )
        self.label5.place(x=750, y=150)
        self.label4=Label(self, text=subprocess_return1,fg="black", font=("Times New Roman", 11) )
        self.label4.place(x=200, y=150)
        self.label6=Label(self, text=subprocess_return6,fg="black", font=("Times New Roman", 11) )
        self.label6.place(x=250, y=200)
        self.label3=Label(self, text=subprocess_return2,fg="black", font=("Times New Roman", 11) )
        self.label3.place(x=550, y=100)
        self.label22=Label(self, text=subprocess_return,fg="black", font=("Times New Roman", 11) )
        self.label22.place(x=180, y=100)
    
        

    def Buttons(self):
        self.button=Button(self, text="UNTETHERED BYPASS 12.4.8", width=30, fg="black", bg="red", font=("Times New Roman", 18), command=self.Bypass_Ios_12)
        self.button.place(x=50, y=300)

        self.button1=Button(self, text="UNTETHERED BYPASS 13-14", width=30, fg="black", bg="red", font=("Times New Roman", 18), command=self.Bypass_Ios_13_14)
        self.button1.place(x=450, y=300)

        self.button2=Button(self, text="INSTALL LIBRARIES", width=30, fg="black", bg="red", font=("Times New Roman", 18),command=self.Back_End)
        self.button2.place(x=50, y=370)
        self.button3=Button(self, text="RESTORE IPHONE", width=30, fg="black", bg="red", font=("Times New Roman", 18), command=self.Irestore)
        self.button3.place(x=450, y=370)
        self.button4=Button(self, text="JAIL BREAK (OPEN CHECKRA1N)", width=30, fg="black", bg="red", font=("Times New Roman", 18), command=self.CheckRa1n)
        self.button4.place(x=50, y=435)
        self.button5=Button(self, text="GET MORE", width=30, fg="black", bg="red", font=("Times New Roman", 18), command=self.Get_More)
        self.button5.place(x=450, y=435)
    def Back_End(self):
        code=subprocess.Popen(['echo  deb https://assets.checkra.in/debian / | sudo tee -a /etc/apt/sources.list'], shell=True, stdout=subprocess.PIPE)
        subprocess_return = code.stdout.read()
        code=subprocess.Popen(['apt-key adv --fetch-keys https://assets.checkra.in/debian/archive.key ''apt update'], shell=True, stdout=subprocess.PIPE)
        subprocess_return = code.stdout.read()
        code=subprocess.Popen(['apt update'], shell=True, stdout=subprocess.PIPE)
        subprocess_return = code.stdout.read()
        code=subprocess.Popen(['apt install -y python libtool-bin libcurl4-openssl-dev libplist-dev libzip-dev openssl libssl-dev  libcurl4-openssl-dev libimobiledevice-dev libusb-1.0-0-dev libreadline-dev build-essential git make autoconf automake libxml2-dev libtool pkg-config checkra1n sshpass checkinstall'], shell=True, stdout=subprocess.PIPE)
        subprocess_return = code.stdout.read()
        code=subprocess.Popen(['git clone https://github.com/libimobiledevice/libirecovery'], shell=True, stdout=subprocess.PIPE)
        subprocess_return = code.stdout.read()
        code=subprocess.Popen(['git clone https://github.com/libimobiledevice/libideviceactivation.git'], shell=True, stdout=subprocess.PIPE)
        subprocess_return = code.stdout.read()
        code=subprocess.Popen(['git clone https://github.com/libimobiledevice/idevicerestore '], shell=True, stdout=subprocess.PIPE)
        subprocess_return = code.stdout.read()
        code=subprocess.Popen(['git clone https://github.com/libimobiledevice/usbmuxd'], shell=True, stdout=subprocess.PIPE)
        subprocess_return = code.stdout.read()
        code=subprocess.Popen(['git clone https://github.com/libimobiledevice/libimobiledevice'], shell=True, stdout=subprocess.PIPE)
        subprocess_return = code.stdout.read()
        code=subprocess.Popen(['git clone https://github.com/libimobiledevice/libusbmuxd'], shell=True, stdout=subprocess.PIPE)
        subprocess_return = code.stdout.read()
        code=subprocess.Popen(['git clone https://github.com/libimobiledevice/libplist'], shell=True, stdout=subprocess.PIPE)
        subprocess_return = code.stdout.read()
        code=subprocess.Popen(['git clone https://github.com/rcg4u/iphonessh.git'], shell=True, stdout=subprocess.PIPE)
        subprocess_return = code.stdout.read()
        code=subprocess.Popen(['cd ./libplist && ./autogen.sh --without-cython && sudo make install && cd ..'], shell=True, stdout=subprocess.PIPE)
        subprocess_return = code.stdout.read()
        code=subprocess.Popen(['cd ./libusbmuxd && ./autogen.sh && sudo make install && cd ..'], shell=True, stdout=subprocess.PIPE)
        subprocess_return = code.stdout.read()

        code=subprocess.Popen(['cd ./libimobiledevice && ./autogen.sh --without-cython && sudo make install && cd ..'], shell=True, stdout=subprocess.PIPE)
        subprocess_return = code.stdout.read()
        code=subprocess.Popen(['cd ./usbmuxd && ./autogen.sh && sudo make install && cd ..'], shell=True, stdout=subprocess.PIPE)
        subprocess_return = code.stdout.read()
        code=subprocess.Popen(['cd ./libirecovery && ./autogen.sh && sudo make install && cd ..'], shell=True, stdout=subprocess.PIPE)
        subprocess_return = code.stdout.read()
        code=subprocess.Popen(['cd ./idevicerestore && ./autogen.sh && sudo make install && cd ..'], shell=True, stdout=subprocess.PIPE)
        subprocess_return = code.stdout.read()
        code=subprocess.Popen(['cd ./libideviceactivation/ && ./autogen.sh && sudo make && sudo make install && cd ..'], shell=True, stdout=subprocess.PIPE)
        subprocess_return = code.stdout.read()
        code=subprocess.Popen(['idconfig'], shell=True, stdout=subprocess.PIPE)
        subprocess_return = code.stdout.read()
    def Irestore(self):
        restore=subprocess.Popen(['idevicerestore -e -1'], shell=True, stdout=subprocess.PIPE)
        subprocess_return = restore.stdout.read()
    def CheckRa1n(self):
        messagebox.showinfo("Terminal Icloud Bypass Tool ", "Opening Checkra1n Put your Idevice in DFU To Jailbreak Fast.......")
        ra1n=subprocess.Popen(['checkra1n -c '], shell=True, stdout=subprocess.PIPE)
        subprocess_return = ra1n.stdout.read()
    def Bypass_Ios_12(self):
        bypass=subprocess.Popen(['/lib/bypass_scripts/mobileactivationd_12_4_7/./run.sh'], shell=True, stdout=subprocess.PIPE)
        subprocess_return = bypass.stdout.read()
    def Bypass_Ios_13_14(self):
        bypass=subprocess.Popen(['/lib/bypass_scripts/mobileactivationd_13_x/./run.sh'], shell=True, stdout=subprocess.PIPE)
        subprocess_return = bypass.stdout.read()
    def Get_More(self):
        os.system('firefox "terminalcreeds.com"')
   
        






if __name__ == "__main__":
    win = Window()
    win.mainloop()
   