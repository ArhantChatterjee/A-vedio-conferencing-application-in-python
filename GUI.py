from vidstream import *
import tkinter as tk
import socket
import threading


global host_name
global host_ip

try:
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print("Hostname :  ",host_name)
    print("IP : ",host_ip)
except:
    print("Unable to get Hostname and IP")
#print(host_ip)
server = StreamingServer(host_ip, 4729)
receiver = AudioReceiver(host_ip,4730)

def start_listening():
    t1 = threading.Thread(target = server.start_server)
    t2 = threading.Thread(target = receiver.start_server)
    t1.start()
    t2.start()

def camera_start_streaming():
    Camera_Client = CameraClient(text_target_ip.get(1.0, 'end-1c'),5050)
    t3 = threading.Thread(target= Camera_Client.start_stream)
    t3.start()

def Screen_sharing():
    Screen_sharing = ScreenShareClient(text_target_ip.get(1.0, 'end-1c'),5050)
    t4 = threading.Thread(target= Screen_sharing.start_stream)
    t4.start()

def Audio_streaming():
    Audio_Sender = AudioSender(text_target_ip.get(1.0, 'end-1c'),5051)
    t5 = threading.Thread(target= Audio_Sender.start_stream)
    t5.start()

window = tk.Tk()
window.title("video Streaming")
window.geometry("500x500")

label_target_ip = tk.Label(window, text = "Target IP ")
label_target_ip.pack()
text_target_ip = tk.Text(window, height= 1)
text_target_ip.pack()

btn_listen = tk.Button(window, text = "Start Listening",width= 50 , command=start_listening)
btn_listen.pack(anchor= tk.CENTER, expand=True)

btn_CAMERA = tk.Button(window, text = "Start Camera Streaming",width= 50, command=camera_start_streaming)
btn_CAMERA.pack(anchor= tk.CENTER, expand=True)

btn_Screen = tk.Button(window, text = "Start Screen SHaring",width= 50,command=Screen_sharing)
btn_Screen.pack(anchor= tk.CENTER, expand=True)

btn_Audio = tk.Button(window, text = "Start Audio Stream",width= 50, command=Audio_streaming)
btn_Audio.pack(anchor= tk.CENTER, expand=True)

window.mainloop()
# Driver code
#get_Host_name_IP() #Function call
#Graphic_user()

