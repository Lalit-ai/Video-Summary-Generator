# Video Summary Generator
    AI based tool that automated the process of generating video summary based upon visual features.

## Setup enviournment

```bash
# Create a Virtual Enviournment "vidsum"
python3 -m pip install --upgrade pip
python3 -m pip install virtualenv

# Create a env
python3 -m venv vidsum

# Activate env
source ./vidsum/bin/activate

# Install Necessary Packages
# git clone repository and extract in vidsum
cd vidsum
pip install -r requirements.txt

# Deactivate env
deactivate
```

## Executing script

```bash
# Run the summary.py
python3 summary.py --video_src=VIDEOPATH
```


## Example Summary Videos
1. https://www.youtube.com/watch?v=YLslsZuEaNE
2. https://www.youtube.com/watch?v=8LjBPQzBCIM

You can see the example summary in example folder


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
