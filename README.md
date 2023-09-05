# whisper-obsidian
Take Obsidian notes with OpenAI's Whisper.

## Getting Started
Required Software:
- Install the Obsidian note taking software at https://obsidian.md/
- Install Python at https://www.python.org/ (this project was tested on ``v3.11.3``)

## Running the code
Once you have installed the software, create a virtual environment inside the project directory using the following command:

```bash
python -m venv env
```

Activate the virtual environment using the command:

```bash
env/Scripts/activate
```

Then run the following command to install all necessary dependancies:

```bash
pip install -r requirements.txt
```

After this, change the path to your Obsidian Vault, currently mine is located in ``C:\\Users\\Gavin\\OneDrive\\Documents\\Obsidian Vault\\`` inside ``note.py`` so change this to match the path to your Obsidian Vault.

Finally run the following command to create a note with OpenAI's Whisper:

```bash
python note.py
```
**Important**: you must have an OpenAI API key, and save it to a ``.env`` file or to your Windows Environment Variables. You can get one by creating an account at https://platform.openai.com/. 

You will be prompted to:
- Add a title to the note, which will be the name of the note inside the Obsidian Vault.
- Choose whether you want to add the title to the note, which would be useful for printing.
- Choose whether you want to place the file inside a folder in the obsidian vault, if you choose yes you can enter the name of the folder.
- Overwrite the existing file (if one already exists).

After recording your audio the Whisper model will be called to transcribe the audio, it will check if you are overwriting and will then save the note.
