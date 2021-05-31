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
> Note: See *OPTIONS* in [arguments guide](https://github.com/levankhelo/net-speed#arguments-guide)

## Arguments guide
### Arguments
```
-h, --help                            show help message
--filename FILENAME, -f FILENAME      name of file where network speed airport xml  will be downloaded and .XMLinfo will be appended to name
--refresh REFRESH, -t REFRESH         refresh rate of display
--convert, -c                         convert KiB to KB
--mb, -m                              convert KiB/KB to Mib/MB
--single, -s                          Run application only one time, instead of refreshing display
```

### Examples
1. `python3 --filename netspeed --refresh 5 --convert` same as `python3 -f netspeed -t 5 -c`
2. `python3 --filename netspeed --single --convert` same as `python3 -f netspeed -s -c`
3. `python3 --single` same as `python3 -s`
4. `python3 --refresh 0.1` same as `python3 -t 0.1`