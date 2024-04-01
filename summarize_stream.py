import base64
import imageio
import requests
from PIL import Image
import io
import json

def capture_and_process_stream(url, headers):
    print("Debug: Firing up the photon capture device, hold on to your butts.")
    cap = imageio.get_reader('<video0>')
    output_file_path = "summary.txt"

    with open(output_file_path, "a") as write_file:
        while True:
            try:
                print("Debug: Attempting to capture a frame...")
                frame = cap.get_next_data()
                print("Debug: Frame captured successfully.")

                buffered = io.BytesIO()
                image = Image.fromarray(frame)
                image.save(buffered, format="PNG")
                encoded_string = base64.b64encode(buffered.getvalue()).decode('utf-8')
                print("Debug: Frame encoded to base64.")

                image_data = [{"data": encoded_string, "id": 12}]
                data = {"prompt": "USER:[img-12]Describe the image.\nASSISTANT:", "n_predict": 128, "image_data": image_data, "stream": True}

                print("Debug: Sending request to server...")
                response = requests.post(url, headers=headers, json=data, stream=True, timeout=10)
                print("Debug: Received response from server.\n\n")

                write_file.write("---"*10 + "\n\n")
                for chunk in response.iter_content(chunk_size=128):
                    content = chunk.decode().strip().split('\n\n')[0]
                    try:
                        content_split = content.split('data: ')
                        if len(content_split) > 1:
                            content_json = json.loads(content_split[1])
                            write_file.write(content_json["content"])
                            print(content_json["content"], end='', flush=True)
                        write_file.flush()  # Flush after every chunk
                    except json.JSONDecodeError:
                        print("JSONDecodeError: Uh-oh! Expecting property name enclosed in double quotes")
            except Exception as e:
                print(f"Debug: There be gremlins in the cogs: {e}")
                break

    cap.close()

# Define the URL and headers
url = "http://localhost:8080/completion"
headers = {"Content-Type": "application/json"}

# Start capturing and processing the video stream with added debugging
capture_and_process_stream(url, headers)
