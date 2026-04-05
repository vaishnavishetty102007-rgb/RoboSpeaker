import pyttsx3


if __name__=="__main__":
    print("Welcome to RoboSpeaker! Created by Vaishnavi")
    while True:
        x=input("What would you like to say?")
        print("Enter 'exit' to quit")
        if x.lower()=="exit":
            print("Goodbye!")
            break
        command=pyttsx3.init()
        command.say(x)
        command.setProperty('rate',150)
        command.setProperty('volume',1.0)
        command.runAndWait()
        command.stop()


