# Windows persian keyboard for linux
This script change some Persian character position to windows keyboard layout (FAS to FA)

Key list:
1. 'پ' Character to '\\' key
2. 'ئ' Character to 'm' key
3. '،'(کاما) Character to 'f' key second level(Shift+f)

This script change 'ir' symbols file. The default path of this file is in '/usr/share/X11/xkb/symbols/ir'. You can also enter another path.

```sh
sudo python Change_Persian_Keyboard_To_Windows.py
```
Enter `1` for default path or enter another symbols file path.

*This script is written in such a way that other characters can be easily added to it, so it would be good if others help to complete it.*