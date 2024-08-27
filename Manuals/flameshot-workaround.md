sudo tee /usr/local/bin/flameshot-gui-workaround > /dev/null <<'EOF'
#!/bin/bash
flameshot gui

EOF

sudo chmod a+x /usr/local/bin/flameshot-gui-workaround