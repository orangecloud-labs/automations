from os import system, path
from time import gmtime, strftime


# Executes and prints CMD
def execute_cmd(cmd_string):
    system('clear')
    a = system(cmd_string)
    print('')
    if a == 0:
        print('Command executed correctly')
    else:
        print('Command terminated with error')
    print('')


# Searches for and edits the VHOSTs
def find(vhost_path, param, mod):
    lines_to_write = ''
    with open(vhost_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            ln = ''
            if param in line:
                if (line.split())[0] == 'proxy_pass':
                    ln += '\t\t' + param + ' ' + mod + ';\n'
                elif param == 'proxy_pass':
                    ln += line
                if param == 'server_name':
                    ln += '\t' + param
                    for p in mod:
                        ln += ' ' + p
                    ln += ';\n'
                if param == 'expires':
                    ln += '\t\t' + param + ' ' + mod + ';\n'
                # Can't put 'gzip' only because it would overwritte the other gzip lines
                if line.split()[0] == 'gzip' and (line.split()[1] == 'on;' or line.split()[1] == 'off;'):
                    ln += '\t\t' + param + ' ' + mod + ';\n'
                elif param == 'gzip':
                    ln += line
                if param == 'Host':
                    ln += '\t\t' + 'proxy_set_header ' + param + ' ' + mod + ';\n'
                if param == 'proxy_cache_valid':
                    ln += '\t\t' + param + ' 200' + ' ' + mod + ';\n'

            else:
                ln += line
            lines_to_write += ln
    print('line: ' + lines_to_write)
    with open(vhost_path, 'w') as f:
        f.write(lines_to_write)


# Backups the VHOST to sites-available file with the timestamp
def backup(vhost_path, vhost_name):
    time = strftime("%Y%m%d%H%M%S", gmtime())
    execute_cmd('cp ' + vhost_path + ' ' + '/etc/nginx/sites-available/' + vhost_name + '.' + time)

    return time


# Restores the VHOST, delets the backup
def restore(vhost_path, vhost_name, last_created_time):
    execute_cmd('cp /etc/nginx/sites-available/' + vhost_name + '.' + last_created_time + ' ' + vhost_path)
    execute_cmd('rm /etc/nginx/sites-available/' + vhost_name + '.' + last_created_time)


def main():
    vhost_name = raw_input('Name of the vhost?')
    path = '/etc/nginx/sites-enabled/' + vhost_name
    if not os.path.isfile(path):
        raw_input('File not found\n')
        exit()
    time = backup(path, vhost_name)
    print('file Backed-up\n')
    origin = raw_input('enter the origin URL (Example: http://mydomain.com))\n')
    find(path, 'proxy_pass', origin)
    domain = []
    inp = ''
    if (raw_input('Do you want to use custom domains? y/N\n') != 'n'):
        while True:
            inp = raw_input('Enter the domain name or q to stop\n')
            if (inp == 'q'):
                break
            domain.append(inp)
        find(path, 'server_name', domain)

    if (raw_input('Time to live (Time to cache the file on nginx)? y/N\n') != 'n'):
        ttl = raw_input('Enter the parameter(Example: 1d)\n')
        find(path, 'expires', ttl)
    if (raw_input('Override Cache-Control Header? y/N\n') != 'n'):
        cch = raw_input('Enter the override parameter for the Cache-Control Header(Example: 1d)\n')
        find(path, 'proxy_cache_valid', cch)

    if (raw_input('Do you want to modify Gzip? y/N\n') != 'n'):
        if raw_input('[1]Enable\n[2]Disable\n') == '1':
            gzip = 'on'
        else:
            gzip = 'off'
        find(path, 'gzip', gzip)

    if (raw_input('Do you want to Override Host Header? y/N\n') != 'n'):
        hheader = raw_input('Host Header:\n')
        find(path, 'Host', hheader)

    execute_cmd('nginx -s reload')
    if (raw_input('Do you want to restore the backup file? y/N\n') != 'n'):
        restore(path, vhost_name, time)


main()
