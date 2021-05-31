import os, time
from xml.etree import ElementTree as ET
import argparse
import signal
import sys

parser = argparse.ArgumentParser(description='Parse netowrk results')

parser.add_argument('--filename','-f', type=str, default="speed",
                    help='name of file where network speed airport xml will be downloaded and .xml.tmp will be appended to name')
parser.add_argument('--refresh','-t', type=float, default=1,
                    help='refresh rate of display')
parser.add_argument('--convert','-c', action='store_true', default=False,
                    help='convert KiB to KB')
parser.add_argument('--mb','-m', action='store_true', default=False,
                    help='convert KiB/KB to Mib/MB')
parser.add_argument('--single','-s', action='store_true', default=False,
                    help='Run application only one time, instead of refreshing display')
args = parser.parse_args()

args.filename = f"{args.filename}.xml.tmp"



def getFile():
    os.system(f"./getNetSpeedXml.sh {args.filename}")

getFile()

def calculate():

    global xml, speed, max, unit

    xml = ET.parse(f'{args.filename}').getroot()

    speed = int(xml.find('lastTxRate').get('value'))
    max = int(xml.find('maxRate').get('value'))
    unit = "Kib"

    if args.mb:     
        speed = speed/1024
        max = max/1024
        if args.convert:
            unit = "MB"
        else:
            unit = "MiB"

    if args.convert:
        speed = speed*8
        max = max*8
        if not args.mb:
            unit = "KB"


if not args.single:
    print(chr(27)+"[2J")

def display():
    global xml, speed, max, unit
    if not args.single:
        print(f"Total: {int((speed/max)*100)}%\tSpeed: {speed}/{max} {unit}",end="\r")
    else:
        print(f"Total: {int((speed/max)*100)}%\tSpeed: {speed}/{max} {unit}")

def signal_handler(sig, frame):
    args.single = True
    run()
    os.remove(args.filename)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def run():
    getFile()
    calculate()
    display()
    if not args.single:
        time.sleep(args.refresh)
        run()
run()


