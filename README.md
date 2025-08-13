# FlooCast - Prebuilt

[KR / 한국어](./README_KR.md)

A Pre-compiled Python application that allows for the control and configuration of FlooGoo USB Bluetooth dongles.

It configures a FlooGoo FMA120 Bluetooth dongle to pair and connect with a Bluetooth headset/speaker for streaming audio or making VoIP calls. It can also configure the dongle to work as an AuraCast sender.

The dongle functions as a standard USB audio speaker and microphone, requiring no drivers on Windows, macOS, or Linux.

## Important Notice

You **CANNOT** upgrade firmware with this prebuilt software. 

It requires Qualcomm's proprietary library to upgrade the chipset, but it's not available for anyone, and only compatible on Windows. Please use Official Windows FlooCast software to upgrade the firmware.

## Installation

This repository is hosting compiled executables for various platorms mentioned below.

- Windows (x86_64) - .msi installer
- macOS (arm64 for Apple Silicon) - .dmg image
- macOS (x86_64 for Intel) - .dmg image
- Linux (x86_64) - .appimage bundle

Please refer to [Release Page.](https://github.com/potatosalad775/FlooCast/releases)

On Windows, the official App can be downloaded directly from Microsoft Store.
 
## Usage

Once configured, the dongle can automatically reconnect to the most recently used device. Please check the support link for more advanced uses. 
 
## Platform specific notes/issues

### macOS

Since executables from this repo are signed with Ad-Hoc signature, you have to manually disable quarantine status.

If you try to use application without running command below, system will think this application damaged, and it's totally normal.

Open Terminal application and run this command below.

```
sudo xattr -rd com.apple.quarantine /Applications/FlooCast.app
```

### Linux

On Linux, if you run the app as a non-root user, you might get "Permission denied: '/dev/ttyACM0'" error. 
Please verify the ttyACM0 device is the "dialout" user group and add your $USER to the group.
You may take the following link as a reference,
https://askubuntu.com/questions/133235/how-do-i-allow-non-root-access-to-ttyusb0

## Acknowledgements