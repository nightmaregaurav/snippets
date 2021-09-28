1. Download latest version BS
2. Place the file in the same directory as crack
3. Open terminal in the folder and give: 
    java --illegal-access=permit -javaagent:BurpSuiteLoader_v2021.8.jar -noverify -jar burpsuite_pro_vXXXX.X.X.jar
4. Launch Keygen: java -jar burploader-old.jar
5. Paste the key and click next
6. Copy the request from the main window and paste in keygen
7. Copy the response from keygen and paste in main window and click next
8. Move all files to opt:
    mkdir /opt/burp
    mv BurpSuiteLoader_v2021.8.jar /opt/burp/
    mv burpsuite_pro_vXXXX.X.X.jar /opt/burp/
    mv burp-suite-icon.png /opt/burp/
9. Generate launcher script:
    echo "java --illegal-access=permit -javaagent:/opt/burp/BurpSuiteLoader_v2021.8.jar -noverify -jar /opt/burp/burpsuite_pro_vXXXX.X.X.jar" > /opt/burp/burpsuite.sh
10. Give RWX permission: chmod 777 /opt/burp/burpsuite.sh
11. Symlink to bin: ln -s /opt/burp/burpsuite.sh /bin/burpsuite
12. Add desktop launcher entry: sudo mv burp.desktop /usr/share/applications/


<<Replace XXXX.X.X with your burp version>>