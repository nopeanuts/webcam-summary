# Webcam Frame Analysis with Llama.cpp + LLava

This project provides a Python script to capture frames from a webcam and send them to a local Llama server for analysis. The analyzed results are saved to a text file, allowing you to review summaries or descriptions provided by the server.

## Getting Started

### Prerequisites

- This has only been test on MacOSX with python 3.10
- A webcam connected to your system.
- Llama.cpp and a compatible model from Hugging Face are required to process the webcam frames.
  
### Installation

#### Step 1: Install Llama C++

1. Clone the Llama.cpp repository:
   ```
   git clone https://github.com/ggerganov/llama.cpp
   cd llama.cpp
   ```
2. Build the project:
   - use `make` or `cmake`:
     ```
     make
     # Or with cmake
     cmake --build . --config Release
     ```

#### Step 2: Download the Model

1. Download the required model files from Hugging Face (`https://huggingface.co/cjpais/llava-v1.6-34B-gguf`):
   - `llava-v1.6-34b.Q8_0.gguf` (or any other quantized model)
   - `mmproj-model-f16.gguf`
2. Note the paths where you download these files.

### Running the Server

1. With Llama.cpp built, run the server using the paths to the downloaded model files:
   - **macOS**:
     ```sh
     ./server -m models/llava-v1.6-34b.Q8_0.gguf --mmproj models/mmproj-model-f16.gguf -ngl 1
     ```




### Capturing and Analyzing Webcam Frames

After ensuring the Llama server is up, you can run the provided Python script to start capturing and analyzing frames from your webcam.

```
python summarize_stream.py
```

This script captures frames continuously and sends them to the Llama server for analysis. The server's responses are saved to `summary.txt`.

### Note

- Keep the server running in the background while the Python script is running.
- Ensure you have installed all necessary Python dependencies by running `pip install -r requirements.txt`.

