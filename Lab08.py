import os

class Dir:
    def duplicates (path:str):
        self.list_of_files = os.listdir(path)
        i = 0
        result = []
        for i in range(len(self.list_of_files)):
            if self._check_in_res_(result, i):
                continue
            with open(self.path + self.list_of_files[i], 'rb') as f:
                main_file = f.readlines()
            added = False
            for j in range(i+1, len(self.list_of_files)):
                with open(self.path + self.list_of_files[j], 'rb') as f:
                    check_file = f.readlines()
                if (str(main_file) == str(check_file)):
                    if added == False:
                        result.append([])
                        result[len(result)-1].append(self.list_of_files[i])
                        added = True
                    result[len(result)-1].append(self.list_of_files[j])

        return result
    
    def _check_in_res_ (self, result, i):
        for j in range(len(result)):
            for o in range(len(result[j])):
                if self.list_of_files[i] == result[j][o]:
                    return true
        return false

if __name__ == '__main__':
    print(Dir.duplicates("../../Python/New/"))
