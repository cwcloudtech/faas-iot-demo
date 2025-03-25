import time

def create_cert_locally(file_name, file_content):
    with open(f"{file_name}.pem" , "w") as file:
        file.write(file_content)

    time.sleep(1)
