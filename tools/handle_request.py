from keywords import library
from time import sleep

library = library.Libray()

class HandleRequest:

    @staticmethod
    def run(case):
        for row in case:
            if type(row[0]) == int and row[1] > 0:
                print(row[3])
                print(row[4], row[5])
                if "input" == row[3]:
                    getattr(library, row[3])((row[4], row[5]), row[6])
                elif "click" == row[3]:
                    getattr(library, row[3])((row[4], row[5]))
                elif "close" == row[3]:
                    getattr(library, row[3])
                else:
                    getattr(library, row[3])(row[6])
                sleep(1)
