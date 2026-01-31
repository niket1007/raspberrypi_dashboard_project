import tkinter as tk
from decouple import config
from Services.Style import SysteminfoStyle
from Services.Static.static import VOLTAGE_STATUS
import subprocess

# Pi CPU Usage and memory count: top -b | head -n 5
# Pi Temperature:  vcgencmd measure_temp
# Pi Voltage check: vcgencmd get_throttled

class SysteminfoPage(tk.Frame):

    UPDATE_INTERVAL_MS = config("system_info_freq", cast=int)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.widgetName = "System Info"

        self.configure(bg=SysteminfoStyle.RETRO_BG)

        top_frame = tk.Frame(self, bg=SysteminfoStyle.RETRO_BG)
        top_frame.pack(**SysteminfoStyle.TopFramePack)

        bottom_frame = tk.Frame(self, bg=SysteminfoStyle.RETRO_BG)
        bottom_frame.pack(**SysteminfoStyle.BottomFramePack)

        self.cpu_label = tk.Label(
            master=top_frame, **SysteminfoStyle.CPULabel)
        self.cpu_label.pack(**SysteminfoStyle.CPULabelPack)

        self.memory_label = tk.Label(
            master=top_frame, **SysteminfoStyle.MemoryLabel)
        self.memory_label.pack(**SysteminfoStyle.MemoryLabelPack)

        self.pi_voltage_label = tk.Label(
            master=bottom_frame, **SysteminfoStyle.VoltageLabel)
        self.pi_voltage_label.pack(**SysteminfoStyle.VoltageLabelPack)

        self.pi_temp_label = tk.Label(
            master=bottom_frame, **SysteminfoStyle.TempLabel)
        self.pi_temp_label.pack(**SysteminfoStyle.TempLabelPack)

        if config("app_platform") != "windows":
            self.populate_data()

    def __get_voltage_status(self) -> str:
        try:
            result = subprocess.run(
                args=['vcgencmd get_throttled'], 
                shell=True, 
                capture_output=True,
                text=True)
            output =  result.stdout.replace("=", " ").replace("\n", "").split(" ")[-1]

            if output in VOLTAGE_STATUS:
                return VOLTAGE_STATUS[output]
            return output
        except Exception as e:
            return "Error"
    
    def __get_temperature(self) -> str:
        try:
            result = subprocess.run(
                args=['vcgencmd measure_temp'], 
                shell=True, 
                capture_output=True,
                text=True)
            output =  result.stdout.replace("=", " ").replace("\n", "").split(" ")[-1]

            if output in VOLTAGE_STATUS:
                return VOLTAGE_STATUS[output]
            return output
        except Exception as e:
            return "Error"
    
    def __get_cpu_memory(self):
        try:
            result = subprocess.run(
                args=['top -b | head -n 5'], 
                shell=True, 
                capture_output=True,
                text=True)
            cpu_usuage = (100 - float(result.stdout.split("\n")[2].split(",")[3].replace("id", "").strip()))
            memory_total = float(result.stdout.split("\n")[3].split(",")[0].replace("MiB Mem :", "").replace("total", "").strip()) 
            memory_free = float(result.stdout.split("\n")[3].split(",")[-1].replace("buff/cache", "").strip())
            memory_usage = ((memory_total - memory_free)/memory_total)*100
            return [cpu_usuage, memory_usage]
        except Exception as e:
            return ["Error", "Error"]
    

    def populate_data(self) -> None:
        voltage_output = self.__get_voltage_status()
        self.pi_voltage_label.config(
            text=f"Voltage Status:\n{voltage_output}")
        
        temperature_output = self.__get_temperature()
        self.pi_temp_label.config(
            text=f"Temp Status:\n{temperature_output}")
        
        cpu_usage, mem_usage = self.__get_cpu_memory()
        self.cpu_label.config(text=f"CPU Status:\n{cpu_usage}%")
        self.memory_label.config(text=f"Memory Status:\n{mem_usage}%")
    
        self.after(self.UPDATE_INTERVAL_MS, self.populate_data)

