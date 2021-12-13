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
# Run the App.py
python3 summary.py --video_src=VIDEOPATH
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
