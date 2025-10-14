import subprocess
import sys
from kivy.properties import StringProperty
from CustomScreen.customScreen import CustomScreen
from Logger.Logger import log
from Static.Messages.messages import (
    IST_ON_ENTER_EVENT, IST_WIFI_NAME_INITIATE,
    IST_WINDOWS_PLATFORM, IST_LINUX_PLATFORM, IST_COMMAND_OUTPUT,
    IST_INITIATE_SPEED_TEST, IST_UPDATE_VALUES_ON_SCREEN)

class InternetSpeedTestScreen(CustomScreen):
    wifi_name = StringProperty("N/A")
    download_speed = StringProperty("--")
    upload_speed = StringProperty("--")
    status_text = StringProperty("Press 'Start Test' to begin")

    def on_enter(self):
        log.debug(IST_ON_ENTER_EVENT)
        self.get_wifi_ssid()
        return super().on_enter()

    def get_wifi_ssid(self):
        log.debug(IST_WIFI_NAME_INITIATE)
        try:
            if sys.platform == "win32":
                log.debug(IST_WINDOWS_PLATFORM)
                command_output = subprocess.check_output("netsh wlan show interfaces", shell=True).decode('utf-8')
                for line in command_output.split('\n'):
                    if "SSID" in line and ":" in line:
                        self.wifi_name = line.split(":")[1].strip()
                        break
            else:
                log.debug(IST_LINUX_PLATFORM)
                self.wifi_name = subprocess.check_output("iwgetid -r", shell=True).decode('utf-8').strip()
        except Exception as e:
            log.error(e)
            self.wifi_name = "Unavailable"

    def start_speed_test(self):
        log.debug(IST_INITIATE_SPEED_TEST)
        download = 0.0
        upload = 0.0
        error = False
        try:
            self.ids.start_button.disabled = True
            command_result = subprocess.run(
                args=["speedtest-cli --secure --csv"], 
                capture_output=True, text=True, shell=True, check=True)
            data = command_result.stdout.split(",")
            log.debug(IST_COMMAND_OUTPUT.format({str(data)}))
            download = float(data[-4]) / 1_000_000
            upload = float(data[-3]) / 1_000_000
        except Exception as e:
            log.error(e)
            error = True
        finally:
            self.update_results(download=download, upload=upload, error=error) 
        
    def update_results(self, download, upload, error = False):
        log.debug(IST_UPDATE_VALUES_ON_SCREEN)
        self.download_speed = f"{download:.2f}"
        self.upload_speed = f"{upload:.2f}"
        self.status_text = "Test complete" if not error else "Test Failed"
        self.ids.start_button.disabled = False
        