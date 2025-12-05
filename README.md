# 🖐️ Hand Gesture Mouse Control

Control your computer mouse with just your hand gestures! No keyboard, no physical mouse needed - just wave your hand in front of your webcam.

## ✨ What Does It Do?

This project uses your webcam and computer vision to turn your hand into a wireless mouse:

- **👆 Point to Move**: Raise your index finger and move it around to control the cursor
- **👌 Pinch to Click**: Bring your thumb and index finger together to click
- **🎯 Smooth Tracking**: Smart smoothing prevents jittery cursor movements

Perfect for presentations, touchless control, or just showing off some cool tech!

## 🎥 How It Works

The app uses MediaPipe's hand tracking to detect your hand landmarks in real-time. When your index finger is raised (pointing upward), it maps your finger position to screen coordinates. Pinch your thumb and index finger together, and it registers as a mouse click.

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed, then grab these dependencies:

```bash
pip install opencv-python mediapipe pyautogui
```

### Running the Project

1. **Clone this repo**:
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```

2. **Fire it up**:
   ```bash
   python main.py
   ```

3. **Start gesturing**!
   - A window will open showing your webcam feed with hand tracking overlays
   - Raise your index finger and move your hand to control the mouse
   - Pinch thumb and index finger together to click
   - Press `q` to quit

## 🎮 Gesture Guide

| Gesture | Action |
|---------|--------|
| Index finger raised | Move cursor |
| Thumb + Index pinch (< 0.05 distance) | Left click |
| Press `q` | Exit application |

## ⚙️ Configuration

You can tweak these parameters in `main.py` for better performance:

- **Detection confidence** (`min_detection_confidence`): Higher values = more accurate but slower
- **Tracking confidence** (`min_tracking_confidence`): Affects tracking stability
- **Smoothing factor** (currently `0.2`): Lower = smoother but slower response
- **Click distance** (currently `0.05`): Threshold for pinch detection

## 🔧 Troubleshooting

**Cursor too jittery?** Increase the smoothing factor or adjust the minimum movement threshold.

**Clicks not registering?** Try increasing the pinch distance threshold from `0.05` to `0.07`.

**Hand not detected?** Make sure you have good lighting and your hand is clearly visible to the webcam.

## 🛠️ Built With

- **OpenCV** - Video capture and processing
- **MediaPipe** - Hand landmark detection
- **PyAutoGUI** - Mouse control automation

## 💡 Future Ideas

- Add right-click gesture
- Implement scrolling with hand movements
- Add gesture for drag-and-drop
- Multi-hand gestures for different actions
- Calibration mode for better accuracy

## 📝 License

Feel free to use this project however you'd like!

## 🤝 Contributing

Got ideas to make this better? Pull requests are welcome! Whether it's adding new gestures, improving accuracy, or fixing bugs - I'd love to see what you come up with.

---

**Tip**: This works best with good lighting and a clean background. Have fun controlling your computer like a wizard! 🧙‍♂️
