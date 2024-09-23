import os
import glob


class DirCrawler:
    base_directory = ""
    used_names: [str]
    video_parts: dict[str, [str]]

    def __init__(self, base_directory):
        self.base_directory = base_directory
        self.used_names = []
        self.video_parts = {}

    def file_name_parser(self, file_name: str) -> [str, str, int]:
        file_name = file_name[:len(file_name) - 4]
        counter = 1
        while file_name[len(file_name) - counter].isdigit():
            counter += 1
        separator = file_name[len(file_name) - counter]
        file_name = file_name[:len(file_name) - counter]
        return file_name, separator, counter - 1

    def directory_dfs(self, directory):
        directories = os.listdir(directory)
        for name in directories:
            next_directory = os.path.join(directory, name)
            if os.path.isfile(next_directory) and next_directory.endswith(".jpg"):
                video_name, separator, numerator = self.file_name_parser(os.path.split(next_directory)[1])
                parts = glob.glob(
                    f"{directory}/{video_name}{separator}{'[0-9]' * numerator}.jpg"
                )
                self.used_names.append(video_name)
                if not len(parts) == 0:
                    self.video_parts[video_name] = parts
            else:
                self.directory_dfs(next_directory)

    def find_all_video_parts(self):
        self.directory_dfs(self.base_directory)
        answer = self.video_parts
        self.video_parts = dict()
        return answer
