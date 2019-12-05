class Phone():
    def update_iphone():
        pass
    def update_android():
        pass

class IIphone:
    def update_iphone(self):
        pass

class IAndroid:
     def update_android(self):
        pass

class Iphone(IIphone):
    def update_iphone(self):
        print("update to 13 version")
        # we don't need this code
        #def update_android(self):
        #print("update to 9.0.1 version")
        

class Android(IAndroid):
    def update_android(self):
        print("update to 9.0.1 version")
        # we don't need this code
        #def update_iphone(self):
        #print("update to 13 version")
        

if __name__ == "__main__"
    android = Android()
    iphone = Iphone()
    android.update_android()
    iphone.update_iphone()
        
