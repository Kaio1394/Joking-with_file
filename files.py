class File:
    @staticmethod
    def find_numbers_times(path_of_file: str, word: str) -> int:
        try:
            file = open(path_of_file, 'r')
            times = 0
            for line in file:
                sentence = word
                line = line.lower().split(' ')
                if len(line) == 0:
                    break
                if sentence in line:
                    times += 1
                    continue
            file.close()
            return times
        except (OSError, TypeError) as err:
            print(err)

    @staticmethod
    def write_file(path_of_file: str, text: str, update: bool = False):
        try:
            if update:
                # if true then update a file
                with open(path_of_file, 'a') as update_file:
                    update_file.write(text)
            else:
                # else create a new file and write
                with open(path_of_file, 'w') as write_file:
                    write_file.write(text)
        except (OSError, TypeError) as err:
            print(err)


