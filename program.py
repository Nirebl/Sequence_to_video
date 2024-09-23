import os
from models.dir_crawler import DirCrawler
from models.video_maker import VideoMaker


class Program:
    max_threads: int
    dir_crawler: DirCrawler
    video_maker: VideoMaker

    def __init__(self, base_directory: str = "source", max_threads: int = 4, output_directory: str = "./output"):
        self.max_threads = max_threads
        if base_directory == "":
            base_directory = "source"
        if output_directory == "":
            output_directory = "./output"

        self.dir_crawler = DirCrawler(base_directory)
        self.video_maker = VideoMaker(output_dir=output_directory, fps=24)
        try:
            os.makedirs(output_directory, exist_ok=True)
        except Exception:
            pass

    def process(self):
        video_parts: dict[str, [str]] = self.dir_crawler.find_all_video_parts()
        video_names = list(video_parts.keys())
        video_id = 0
        while video_id < len(video_names):
            video_name = video_names[video_id]
            self.video_maker.create_video(video_name, video_parts[video_name])
            video_id += 1

        print("Processing done!")
