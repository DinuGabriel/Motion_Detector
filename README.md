# Motion Detection System

This project is a simple motion detection system implemented in Python using OpenCV and Bokeh.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [License](#license)

## Overview

This motion detection system captures video from a webcam and detects motion within the video frames. When motion is detected, it records the start and end times of the motion events and displays them on an interactive graph using Bokeh.

## Features

- Real-time motion detection using OpenCV.
- Recording of motion event timestamps.
- Interactive motion graph with tooltips using Bokeh.

## Requirements

- Python 3.x
- OpenCV (cv2)
- pandas
- Bokeh

## Usage

Run the motion detection code:
- python motion_detector.py

The motion detector will open your webcam feed, and you can press 'q' to exit the program.

After running the motion detector, you can visualize the recorded motion events by running:
- python visualize_motion.py

The visualization will be saved as an HTML file named Graph.html.