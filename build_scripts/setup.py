import os

os.chdir(deps_dir)

# Build mediapipe
execbuildscript(os.path.dirname(os.path.realpath(__file__)) +"/build_mediapipe.py")