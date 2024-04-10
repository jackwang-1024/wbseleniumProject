from selenium.webdriver.common.by import By
class Dog:
    def bite(self,thing):
        print("dog bite " + thing)

if __name__ == '__main__':
    dog = Dog()
    getattr(dog,"bite")("mouse")

dict1={"id":By.ID,"name":By.NAME}
print(dict1["id"])
print(dict1["name"])

for i in range(1,3):
    print(i)