import os

class Dir:
    def __init__ (self, path):
        self.path = path
    def duplicates (self):
        list_of_files = os.listdir(self.path)
        i = 0
        result = []
        for i in range(len(list_of_files)):
            br = False
            for j in range(len(result)):
                for o in range(len(result[j])):
                    if list_of_files[i] == result[j][o]:
                        br = True
                        break
                if br:
                    break
            if br:
                continue
            with open(self.path + list_of_files[i], 'rb') as f:
                main_file = f.readlines()
            added = False
            for j in range(i+1, len(list_of_files)):
                with open(self.path + list_of_files[j], 'rb') as f:
                    check_file = f.readlines()
                if (str(main_file) == str(check_file)):
                    if added == False:
                        result.append([])
                        result[len(result)-1].append(list_of_files[i])
                        added = True
                    result[len(result)-1].append(list_of_files[j])

        return result

dir = Dir("D:/Ira/Python/new/")
print(dir.duplicates())