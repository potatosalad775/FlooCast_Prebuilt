# FlooCast - Prebuilt

[EN / English](./README.md)

본 전용 프로그램은 FlooGoo USB 블루투스 동글을 설정하고 조작하기 위해 미리 컴파일된 Python 애플리케이션입니다.

해당 프로그램은 FlooGoo FMA120 블루투스 동글을 조작하는데 사용됩니다. 오디오 스트리밍 및 VoIP 통화를 위해 블루투스 장치를 연결하거나, 동글이 AuraCast 발신 장치로 동작하도록 할 수도 있습니다.

동글은 일반적인 USB 오디오 및 마이크 장치로 동작하며, Windows, macOS, Linux를 비롯한 환경에서 별도의 드라이버를 필요로 하지 않습니다.

## 설치

본 레포지토리는 아래 시스템들을 위해 미리 컴파일 과정을 마친 FlooGoo 애플리케이션을 호스팅하고 있습니다.

- Windows (x86_64) - .msi installer
- macOS (arm64 for Apple Silicon) - .dmg image
- macOS (x86_64 for Intel) - .dmg image
- Linux (x86_64) - .appimage bundle

[Release Page.](https://github.com/potatosalad775/FlooCast/releases)를 참조해주시기 바랍니다.

윈도우의 경우, Microsoft Store에서 미리 컴파일된 공식 애플리케이션을 다운로드 받을 수 있습니다.
 
## 사용법

전용 프로그램을 통한 설정을 마치고 나면, 동글은 자동으로 가장 최근에 사용된 기기와 연결을 시도합니다. 보다 자세한 내용은 지원 페이지를 참고하시기 바랍니다.
 
## 시스템 별 안내사항

### macOS

본 프로그램은 Ad-Hoc 서명 과정을 거친 만큼, 사용자가 직접 애플리케이션 격리 상태를 해제해주어야 사용할 수 있습니다. 

아래 명령어를 수행하지 않은 채 프로그램을 실행시키면, 앱이 손상되어 열 수 없다는 안내가 표시될 수 있습니다. 이는 정상적인 상황입니다.

터미널 애플리케이션을 실행한 뒤, 아래 명령어를 수행해주세요.

```
sudo xattr -rd com.apple.quarantine /Applications/FlooCast.app
```

FlooCast.app 프로그램이 '응용 프로그램' 폴더가 아닌 다른 위치에 있다면, 명령어 뒤 경로를 수정해주어야 합니다.

### Linux

On Linux, if you run the app as a non-root user, you might get "Permission denied: '/dev/ttyACM0'" error. 
Please verify the ttyACM0 device is the "dialout" user group and add your $USER to the group.
You may take the following link as a reference,
https://askubuntu.com/questions/133235/how-do-i-allow-non-root-access-to-ttyusb0

## Acknowledgements

