#!/bin/sh

sourcePath=$(dirname "${BASH_SOURCE[0]}")

sudo chmod -R +x ${sourcePath}/src
cat > ${sourcePath}/ip.sh <<EOF
#!/bin/bash
cd ${sourcePath}/src
python3 main.py
EOF

sudo rm /usr/local/bin/ip
sudo ln -s ${sourcePath}/ip.sh /usr/local/bin/ip

echo Added ip to /usr/local/bin

# Change permissions on the newly linked file
sudo chmod +x /usr/local/bin/ip
sudo chmod +x ${sourcePath}/uninstall.command
