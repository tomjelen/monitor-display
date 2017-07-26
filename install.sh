#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cat > /lib/systemd/system/monitor-display.service <<EOF
[Unit]
Description=Monitor Display
After=multi-user.target

[Service]
Type=simple
Restart=always
RestartSec=10
WorkingDirectory=$DIR
ExecStart=/usr/bin/python3 $DIR/app.py

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable monitor-display.service
