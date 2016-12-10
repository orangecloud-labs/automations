import crypt, re

skip_user = ['daemon','bin','sys','sync','games','man','lp','mail','news','uucp','proxy','www-data','backup','list','irc','gnats','nobody','systemd-timesync','systemd-network','systemd-resolve','systemd-bus-proxy','messagebus','avahi','ntp','sshd','statd','lightdm','pulse','rtkit','mysql']

class col:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def test(salt, hash, username):
	with open("list.txt", "r") as list:
		for line in list:
			dict_line = line.rstrip()
			tried_hash = crypt.crypt(dict_line, salt)
			print("Testing with '" + col.BLUE + dict_line + col.END + "'")
			if tried_hash == salt + hash:
				print(col.GREEN + "Found password for user '" + username + "' is " + col.END + col.BOLD + dict_line + col.END + "\n")
				return None
		print(col.FAIL + "Password not found for user '" + col.END + col.BOLD + username + col.END + col.FAIL + "'" + col.END + "\n")

with open("/etc/shadow", "r") as shadow:
	for line in shadow:
		pattern = re.compile('([a-zA-Z0-9_-]+):(\$\d\$[a-zA-Z0-9_\-\/\.]+\$)?(.*)(:.*){7}')
		matched = pattern.match(line)
		username = matched.group(1)
		if username not in skip_user:
			print(col.BOLD + "TESTING PASSWORD FOR USER '" + username + "'" + col.END + "\n")
			salt = matched.group(2)
			hash = matched.group(3)
			test(salt, hash, username)
