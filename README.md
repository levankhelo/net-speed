# net-speed
Quick, Easy and Free network speed display in terminal

## Prerequisited
### Virtual Environment
This step is optional
```bash
python3 -m pip venv netspeed.env;
source netspeed.env/bin/activate
```
### Requirmenets
Install requirements using `requirements.txt` by following command:
```bash
python3 -m pip install --ignore-installed  -r requirements.txt
```

## Run Application
You can run using predefined file that will be easiest to use:
```bash
/bin/bash run.sh
```
or just use `main.py` to execute script:
```bash
python3 main.py [OPTIONS]
```
> Note: See *OPTIONS* in [arguments guide]()

### Arguments guide
```
  -h, --help                            show this help message and exit
  --filename FILENAME, -f FILENAME      name of file where network speed airport xml  will be downloaded and .XMLinfo will be appended to name
  --refresh REFRESH, -t REFRESH         refresh rate of display
  --convert, -c                         convert KiB to KB
  --mb, -m                              convert KiB/KB to Mib/MB
  --single, -s                          Run application only one time, instead of refreshing display
```