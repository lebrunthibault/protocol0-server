import os

_ableton_version = os.environ["abletonVersion"]
_ableton_major_version = _ableton_version.split('.')[0]


class SystemConfig:
    LOGGING_DIRECTORY = os.environ.get("LOGGING_DIRECTORY")
    PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
    ABLETON_VERSION = _ableton_version
    ABLETON_MAJOR_VERSION = _ableton_major_version
    ABLETON_EXE = f"Ableton Live {_ableton_major_version} Suite.exe"
    LOG_WINDOW_TITLE = "logs terminal"
    # Midi port names are relative to the Protocol0 script and not this midi backend
    P0_OUTPUT_PORT_NAME = 'P0_OUT'
    P0_INPUT_PORT_NAME = 'P0_IN'
    MIDI_SERVER_WINDOW_TITLE = "midi server"
