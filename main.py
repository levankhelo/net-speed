import argparse

parser = argparse.ArgumentParser(description='Parse netowrk results')

parser.add_argument('--filename', type=str, default="speed",
                    help='name of file where network speed airport xml will be downloaded and .XMLinfo will be appended to name')
parser.add_argument('--refresh-time', type=int, default=1,
                    help='refresh rate of display')
parser.add_argument('--convert', action='store_true', default=False,
                    help='convert KiB to KB')
parser.add_argument('--use-mb', action='store_true', default=False,
                    help='convert KiB/KB to Mib/MB')
parser.add_argument('--single', action='store_true', default=False,
                    help='Run application only one time, instead of refreshing display')
args = parser.parse_args()

args.filename = f"{args.filename}.XMLinfo"

import os

def getFile():
    os.system("./getNetSpeedXml.sh")

getFile()

from xml.etree import ElementTree as ET
xml = ET.parse(f'{args.filename}').getroot()

for p in xml.findall('.//root'):
    print(p.find("value"))