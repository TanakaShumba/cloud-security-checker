# Simulated Cloud Security Configuration Checker

services = {
    'S3 Bucket': {'public_access': True},
    'EC2 Instance': {'ssh_open': True},
    'RDS Database': {'encrypted': False}
}

def check_security(configs):
    for service, settings in configs.items():
        for setting, value in settings.items():
            if value:
                print(f"WARNING: {service} has insecure setting: {setting}")
            else:
                print(f"{service} setting {setting} is secure")

if __name__ == "__main__":
    print("Running Cloud Security Config Checker...\n")
    check_security(services)
