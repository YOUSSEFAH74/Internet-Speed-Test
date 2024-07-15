import tkinter as tk
import speedtest


def check_speed():
  s = speedtest.Speedtest()
  s.get_servers()
  download_speed = round(s.download() / (1024 * 1024), 2)
  upload_speed = round(s.upload() / (1024 * 1024), 2)
  download_result.set(f"Download: {download_speed} Mbps")
  upload_result.set(f"Upload: {upload_speed} Mbps")


def clear_results():
  download_result.set("")
  upload_result.set("")


window = tk.Tk()
window.title("Internet Speed Test")
window.config(bg='#5834eb')


download_label = tk.Label(window, text="Download:" , bg='#5834eb',font=('arial',15,'bold'))
download_label.pack()


download_result = tk.StringVar()
download_value = tk.Label(window, textvariable=download_result, bg='#5834eb')
download_value.pack()


upload_label = tk.Label(window, text="Upload:", bg='#5834eb',font=('arial',15,'bold'))
upload_label.pack()


upload_result = tk.StringVar()
upload_value = tk.Label(window, textvariable=upload_result, bg='#5834eb')
upload_value.pack()


start_button = tk.Button(window, text="Start Test", command=check_speed, bg='#5834eb',activebackground='#5834eb')
start_button.pack()


clear_button = tk.Button(window, text="Clear Results", command=clear_results, bg='#5834eb',activebackground='#5834eb')
clear_button.pack()

window.mainloop()
