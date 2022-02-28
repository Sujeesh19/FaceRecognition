import CapturingImages
import FaceDetection
import Emailautomation
import FaceTrain

print("Press 1 for Capture test")
print("Press 2 for train image")
print("Press 3 for detect face amd sending email")
print("Press 4 for exit")

def main():
    while True:
        try:
            n = int(input("Enter your choice: "))

            if n == 1:
                capture()

            elif n == 2:
                train()

            elif n == 3:
                detect()

            elif n == 4:
                print("Thank You")
                break

            else:
                print("Invalid Choice. Enter 1-4")
                Main()

        except ValueError:
            print("Invalid Choice. Enter 1-4\n Try Again")


def capture():
    CapturingImages.Capture_images()
    key = input("Enter any key to return main menu")
    main()

def train():
    FaceTrain.train_faces()
    key = input("Enter any key to return main menu")
    main()

def detect():
    fileName = FaceDetection.detectFaces()
    key = input("Enter any key to return main menu")
    mail(fileName)
    main()

def mail(fileName):
    s = input("Enter your email id: ")
    Emailautomation.sendingEmail(s, fileName)
    key = input("Enter any key to return main menu")
    main()

if __name__ == "__main__":
    main()
