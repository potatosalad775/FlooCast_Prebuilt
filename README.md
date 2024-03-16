# FlooCast

A Python application that allows for the control and configuration of FlooGoo USB Bluetooth dongles.

It configures a FlooGoo FMA120 Bluetooth dongle to pair and connect with a Bluetooth headset/speaker for streaming audio or making VoIP calls. It can also configure the dongle to work as an AuraCast sender.

The dongle functions as a standard USB audio speaker and microphone, requiring no drivers on Windows, macOS, or Linux.

## Installation

On Windows, Official App can be downloaded directly from [Microsoft Store](https://www.microsoft.com/store/productId/9NX1CW8VZ6QR).

Pre-compiled executables for various operating systems are also available at Release Tab.
 
## Usage

Once configured, the dongle can automatically reconnect to the most recently used device. Please check the support link for more advanced uses. 
 
## Compiling

Requires python 3.7+ & following modules
- pyserial
- pystray
- serial-tool
- pyinstaller

This fork added pyinstaller support to compile the project.

```Python
cd <Project Location>   # Move to project
pip install             # Install required modules
pyinstaller main.spec   # Compile executable to ./dist
```

## Platform specific notes/issues

On Linux, if you run the app as a non-root user, you might get "Permission denied: '/dev/ttyACM0'" error. 
Please verify the ttyACM0 device is the "dialout" user group and add your $USER to the group.
You may take the following link as a reference,
https://askubuntu.com/questions/133235/how-do-i-allow-non-root-access-to-ttyusb0

## Acknowledgements

