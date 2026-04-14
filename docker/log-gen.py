import logging
import time
import random
import os

# ตรวจสอบว่าโฟลเดอร์มีอยู่จริงไหม
log_dir = '/var/log'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

log_file_path = '/var/log/loki.log'
logging.basicConfig(filename=log_file_path, level=logging.INFO, 
                    format='%(asctime)s level=%(levelname)s app=myapp component=%(component)s %(message)s')

def generate_log_entries():
    components = ["database", "backend"]
    # เปลี่ยนจาก range(10) เป็น while True เพื่อให้รันใน Docker ได้ตลอด
    while True:
        log_level = random.choice([logging.INFO, logging.WARNING, logging.ERROR])
        component = random.choice(components)

        if log_level == logging.INFO:
            log_message = "Information: Application running normally"
        elif log_level == logging.WARNING:
            log_message = "Warning: Resource usage high"
        else:
            log_message = "Critical error: Database connection lost"

        logging.log(log_level, log_message, extra={"component": component})
        print(f"Logged: {log_level} - {component}") # ดูผ่าน docker logs
        time.sleep(2) 

if __name__ == "__main__":
    generate_log_entries()