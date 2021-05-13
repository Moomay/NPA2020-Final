from netmiko import ConnectHandler

def main():
    username = 'admin'
    password = 'cisco'
    secret = 'secret'

    device_ip = "10.0.15.116"

    device_params = {'device_type': 'cisco_ios',
                    'ip': device_ip,
                    'username' : username,
                    'password' : password
    }
    config_set = [
        "int lo 61070215", "ip add 192.168.1.1 255.255.255.0"
    ]
    with ConnectHandler(**device_params) as ssh:
        ssh.send_config_set(config_set)

main()
