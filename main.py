import subprocess
from tqdm import tqdm
import os


def create_bootable_usb(iso_path, usb_device):
    try:
        # Validate ISO file and USB paths
        if not os.path.isfile(iso_path):
            print("Error: The specified ISO file does not exist.")
            return
        if not os.path.exists(usb_device):
            print("Error: The specified USB device does not exist.")
            return

        # Use 'dd' command to write the ISO to the USB device

        cmd = ['sudo', 'dd', 'if=' + iso_path, 'of=' + usb_device, 'bs=4M', 'status=progress', 'conv=fsync']

        # Create a loading bar
        with tqdm(total=os.path.getsize(iso_path), unit='B', unit_scale=True, unit_divisor=1024) as progress_bar:
            process = subprocess.Popen(cmd, stderr=subprocess.PIPE)
            for line in process.stderr:
                progress_bar.update(len(line))
            process.wait()

        print("Bootable USB created successfully!")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    iso_path = input("Enter the path to the ISO file: ")
    usb_device = input("Enter the path to the USB device (example /dev/sdx: ")

    create_bootable_usb(iso_path, usb_device)


