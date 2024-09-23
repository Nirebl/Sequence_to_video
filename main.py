from program import Program

if __name__ == '__main__':
    print("Введите путь до папки в которой лежат секвенции, по стандарту ./source")
    dir_input: str = input()
    print("Введите путь до папки в которую рендерить секвенции, по стандарту ./output")
    dir_output: str = input()
    videoProcessor = Program(base_directory=dir_input, output_directory=dir_output)
    videoProcessor.process()
