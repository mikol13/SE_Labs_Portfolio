# Motion Detection Surveillance System — Core Engine Prototype

This repository contains the working prototype and core logic engine for the **Motion Detection Surveillance System**, designed in accordance with the project's **Software Requirements Specification (SRS v4.0.0)** for the Lodz University of Technology.

---

## The Big Picture: Why this Prototype Exists

The full vision detailed in the SRS describes a complete hardware-software system: a Raspberry Pi microcomputer, live camera feeds, a Flask web dashboard, and automated email alerts. 

Instead of building all of that massive infrastructure at once (which makes finding bugs incredibly difficult), this prototype isolates the **"brains"** of the system. By testing the core motion-tracking logic on a normal computer using a local `video.mp4` file, we prove that the foundational math and detection algorithms work perfectly before deploying to physical hardware.

---

## How the Detection Engine Works (In Simple Terms)

Every second, a video is just a fast series of individual pictures (frames). The core engine inside `motion_detector.py` processes these pictures using four straightforward steps:

1. **Remove Color:** The code converts the frame to grayscale. We only care about shapes and movement, and stripping the color saves computing power.
2. **Smooth the Image:** It applies a gentle blur. This eliminates background "fuzziness" or digital camera static that might look like fake motion.
3. **Spot the Differences:** It takes the current frame and compares it directly to the previous one. Any pixel that changed color gets highlighted.
4. **Filter out the Noise:** It looks at the size of the changed area. If a tiny speck changes (like a shadow shift or a fly), it ignores it. If a large shape changes (like a person walking past), it locks into a **MOTION DETECTED** state.

---

## Built with Test-Driven Development (TDD)

To ensure the system is reliable, the code was written using a **Test-Driven Development** approach. Instead of guessing if the code works, we wrote automated tests *first* (`test_motion_detector.py`) to set strict rules:
* **Rule 1:** If two video frames are exactly identical, the system *must not* trigger a false alarm.
* **Rule 2:** If a large shape suddenly appears out of nowhere, the system *must* detect it instantly.
* **Rule 3:** Once motion is caught, the system state must firmly latch onto "DETECTED" so it doesn't flicker or lose track of the event.

---

## Project Directory Structure

```text
my_surveillance_project/
│
├── venv/                  # Your isolated Python environment
├── motion_detector.py     # The pure object logic (The "Brains")
├── test_motion_detector.py# Automated terminal tests
├── tdd_demo.py            # The main app that runs the video playback
└── video.mp4              # Your local video file used for testing
