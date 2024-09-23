from moviepy.editor import *
from natsort import natsorted


class VideoMaker:
    output_dir: str = ""
    fps: int

    def __init__(self, output_dir: str = "", fps: int = 24):
        self.output_dir = output_dir
        if not output_dir.endswith("/"):
            self.output_dir += "/"
        self.fps = fps

    def create_video(self, video_name: str, video_part: [str]):
        print(f"Creating video {video_name}")
        if len(video_part) == 0:
            return
        video_part: [str] = natsorted(video_part, reverse=False)
        ImageSequenceClip(video_part, fps=self.fps).write_videofile(
            f"./{self.output_dir}{video_name}.mov",
            codec="mjpeg",
        )
        print(f"Video {video_name} created")
