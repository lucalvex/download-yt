import xml.etree.ElementTree as ET
import subprocess
from pathlib import Path

XML_FOLDER = "xmls"
VIDEOS_FOLDER = "videos"

# Create the output directory if it does not exist
Path(VIDEOS_FOLDER).mkdir(exist_ok=True)

for xml_file in Path(XML_FOLDER).glob("*.xml"):
  try:
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Get the video ID
    video_id = root.attrib.get("id", xml_file.stem)

    # Get the video URL
    url = root.find("url")

    if url is not None and url.text:
      print(f"Downloading {video_id}: {url.text}")

      subprocess.run([
        "yt-dlp",
        "-o",
        f"{VIDEOS_FOLDER}/{video_id}.%(ext)s",
        url.text
      ])

  except Exception as e:
    print(f"Error processing {xml_file}: {e}")