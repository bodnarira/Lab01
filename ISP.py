class IIphone:
    def update_iphone(self):
        pass

class PhoneCall:
     def call(self):
        pass

class Iphone(PhoneCall, IIphone):
    def update_iphone(self):
        print("update to 13 version")
    def call(self):
        

class Android(PhoneCall):
    def call(self):
        print("I'm calling to you")
        

if __name__ == "__main__"
    android = Android()
    iphone = Iphone()
    android.update_iphone()  #error
    iphone.update_iphone()
    android.call()
    iphone.call()
        
