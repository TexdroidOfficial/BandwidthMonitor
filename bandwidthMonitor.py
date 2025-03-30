import customtkinter
import time
import psutil

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("Test")
    
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login", font=("Roboto", 24))
label.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Close", command=root.destroy)
button.pack(pady=12, padx=10)

root.mainloop()


last_received = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent
last_total = last_received + last_sent

jumpstart = time.time()
finish_line = jumpstart + 15

received_total = 0
sent_total = 0
absolute_total = 0
counter = 0

while time.time() < finish_line:
    bytes_received = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_total = bytes_received + bytes_sent
    
    new_received = bytes_received - last_received
    new_sent = bytes_sent - last_sent
    new_total = bytes_total - last_total
    
    mb_new_received = new_received / 1024 / 1024
    mb_new_sent = new_sent / 1024 / 1024
    mb_new_total = new_total / 1024 / 1024
    
    print(f"{mb_new_received:.2f} MB received, {mb_new_sent:.2f} MB sent, {mb_new_total:.2f} MB total,")
    
    received_total += mb_new_received
    sent_total += mb_new_sent
    absolute_total += mb_new_total
    counter += 1

    last_received = bytes_received
    last_sent = bytes_sent
    last_total = bytes_total
    
    time.sleep(1)
    
if counter > 0:
    avg_received = received_total / counter
    avg_sent = sent_total / counter
    avg_total = absolute_total / counter

    print(f"\nAverage received: {avg_received:.2f} MB/s")
    print(f"Average sent: {avg_sent:.2f} MB/s")
    print(f"Average total: {avg_total:.2f} MB/s")
else:
    print("\nNo network traffic data collected.")
    
print("Network monitoring finished after 15 seconds.")