#Fake cookies made with <3 by Archer Calder (Merkie)

#generate string [√]
#generate string w/ pattern [√]
#generate every id of mobile apple devices [√]
#generate ios device ids
#generate fake headers
#android?

import random

class fcs:

    def __init__(self):
        pass

    def generate(self, length=None, cbank=None, amount=None):
        if length == None:
            l = 16
        else:
            l = length

        if cbank == None:
            c = "abcdefghijklmnopqrstuvwxyz0123456789"
        else:
            c = "abcdefghijklmnopqrstuvwxyz0123456789"

            if cbank == "a0":
                c = "abcdefghijklmnopqrstuvwxyz0123456789"

            if cbank == "a":
                c = "abcdefghijklmnopqrstuvwxyz"

            if cbank == "0":
                c = "0123456789"

            if cbank == "A":
                c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

            if cbank == "A0":
                c = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        if amount == None:
            a = 1
        else:
            a = amount

        if a == 1 or a < 1:
            generated = ""

            for x in range(l):
                generated += random.choice(c)

            return generated
        else:
            generatedlist = []

            for i in range(a):
                generated = ""

                for x in range(l):
                    generated += random.choice(c)

                generatedlist.append(generated)

            return generatedlist

    def genpattern(self, cbank=None, splitchar=None, pattern=None, amount=None):
        if pattern == None:
            p = [5,5,5]
        else:
            p = pattern

        if splitchar == None:
            s = "-"
        else:
            s = splitchar

        if cbank == None:
            c = "a0"
        else:
            c = cbank

        if amount == None or amount == 1 or amount < 1:
            generated = ""

            for pat in range(len(p)):
                generated += self.generate(length=p[pat], cbank=c)

                if pat != len(p)-1:
                    generated += s

            return generated
        else:
            generatelist = []

            for x in range(amount):
                generated = ""

                for pat in range(len(p)):
                    generated += self.generate(length=p[pat], cbank=c)

                    if pat != len(p)-1:
                        generated += s

                generatelist.append(generated)

            return generatelist

    def gendevice(self, device=None, amount=None):
        if device == None:
            t = "iphone"
        else:
            t = device

        if t == "iphone" or t == "iPhone":
            t = [
            {"id":"iPhone1,1","name":"iPhone"},
            {"id":"iPhone1,2","name":"iPhone 3G"},
            {"id":"iPhone2,1","name":"iPhone 3GS"},
            {"id":"iPhone3,1","name":"iPhone 4"},
            {"id":"iPhone3,2","name":"iPhone 4 GSM Rev A"},
            {"id":"iPhone3,3","name":"iPhone 4 CDMA"},
            {"id":"iPhone4,1","name":"iPhone 4S"},
            {"id":"iPhone5,1","name":"iPhone 5 (GSM)"},
            {"id":"iPhone5,2","name":"iPhone 5 (GSM+CDMA)"},
            {"id":"iPhone5,3","name":"iPhone 5C (GSM)"},
            {"id":"iPhone5,4","name":"iPhone 5C (Global)"},
            {"id":"iPhone6,1","name":"iPhone 5S (GSM)"},
            {"id":"iPhone6,2","name":"iPhone 5S (Global)"},
            {"id":"iPhone7,1","name":"iPhone 6 Plus"},
            {"id":"iPhone7,2","name":"iPhone 6"},
            {"id":"iPhone8,1","name":"iPhone 6s"},
            {"id":"iPhone8,2","name":"iPhone 6s Plus"},
            {"id":"iPhone8,4","name":"iPhone SE (GSM)"},
            {"id":"iPhone9,1","name":"iPhone 7"},
            {"id":"iPhone9,2","name":"iPhone 7 Plus"},
            {"id":"iPhone9,3","name":"iPhone 7"},
            {"id":"iPhone9,4","name":"iPhone 7 Plus"},
            {"id":"iPhone10,1","name":"iPhone 8"},
            {"id":"iPhone10,2","name":"iPhone 8 Plus"},
            {"id":"iPhone10,3","name":"iPhone X Global"},
            {"id":"iPhone10,4","name":"iPhone 8"},
            {"id":"iPhone10,5","name":"iPhone 8 Plus"},
            {"id":"iPhone10,6","name":"iPhone X GSM"},
            {"id":"iPhone11,2","name":"iPhone XS"},
            {"id":"iPhone11,4","name":"iPhone XS Max"},
            {"id":"iPhone11,6","name":"iPhone XS Max Global"},
            {"id":"iPhone11,8","name":"iPhone XR"},
            {"id":"iPhone12,1","name":"iPhone 11"},
            {"id":"iPhone12,3","name":"iPhone 11 Pro"},
            {"id":"iPhone12,5","name":"iPhone 11 Pro Max"}
            ]

        if t == "ipod" or t == "iPod":
            t = [
            {"id":"iPod1,1","name":"1st Gen iPod"},
            {"id":"iPod2,1","name":"2nd Gen iPod"},
            {"id":"iPod3,1","name":"3rd Gen iPod"},
            {"id":"iPod4,1","name":"4th Gen iPod"},
            {"id":"iPod5,1","name":"5th Gen iPod"},
            {"id":"iPod7,1","name":"6th Gen iPod"},
            {"id":"iPod9,1","name":"7th Gen iPod"}
            ]

        if t == "ipad" or t == "iPad":
            t = [
            {"id":"iPad1,1","name":"iPad"},
            {"id":"iPad1,2","name":"iPad 3G"},
            {"id":"iPad2,1","name":"2nd Gen iPad"},
            {"id":"iPad2,2","name":"2nd Gen iPad GSM"},
            {"id":"iPad2,3","name":"2nd Gen iPad CDMA"},
            {"id":"iPad2,4","name":"2nd Gen iPad New Revision"},
            {"id":"iPad3,1","name":"3rd Gen iPad"},
            {"id":"iPad3,2","name":"3rd Gen iPad CDMA"},
            {"id":"iPad3,3","name":"3rd Gen iPad GSM"},
            {"id":"iPad2,5","name":"iPad mini"},
            {"id":"iPad2,6","name":"iPad mini GSM+LTE"},
            {"id":"iPad2,7","name":"iPad mini CDMA+LTE"},
            {"id":"iPad3,4","name":"4th Gen iPad"},
            {"id":"iPad3,5","name":"4th Gen iPad GSM+LTE"},
            {"id":"iPad3,6","name":"4th Gen iPad CDMA+LTE"},
            {"id":"iPad4,1","name":"iPad Air (WiFi)"},
            {"id":"iPad4,2","name":"iPad Air (GSM+CDMA)"},
            {"id":"iPad4,3","name":"1st Gen iPad Air (China)"},
            {"id":"iPad4,4","name":"iPad mini Retina (WiFi)"},
            {"id":"iPad4,5","name":"iPad mini Retina (GSM+CDMA)"},
            {"id":"iPad4,6","name":"iPad mini Retina (China)"},
            {"id":"iPad4,7","name":"iPad mini 3 (WiFi)"},
            {"id":"iPad4,8","name":"iPad mini 3 (GSM+CDMA)"},
            {"id":"iPad4,9","name":"iPad Mini 3 (China)"},
            {"id":"iPad5,1","name":"iPad mini 4 (WiFi)"},
            {"id":"iPad5,2","name":"4th Gen iPad mini (WiFi+Cellular)"},
            {"id":"iPad5,3","name":"iPad Air 2 (WiFi)"},
            {"id":"iPad5,4","name":"iPad Air 2 (Cellular)"},
            {"id":"iPad6,3","name":"iPad Pro (9.7 inch, WiFi)"},
            {"id":"iPad6,4","name":"iPad Pro (9.7 inch, WiFi+LTE)"},
            {"id":"iPad6,7","name":"iPad Pro (12.9 inch, WiFi)"},
            {"id":"iPad6,8","name":"iPad Pro (12.9 inch, WiFi+LTE)"},
            {"id":"iPad6,11","name":"iPad (2017)"},
            {"id":"iPad6,12","name":"iPad (2017)"},
            {"id":"iPad7,1","name":"iPad Pro 2nd Gen (WiFi)"},
            {"id":"iPad7,2","name":"iPad Pro 2nd Gen (WiFi+Cellular)"},
            {"id":"iPad7,3","name":"iPad Pro 10.5-inch"},
            {"id":"iPad7,4","name":"iPad Pro 10.5-inch"},
            {"id":"iPad7,5","name":"iPad 6th Gen (WiFi)"},
            {"id":"iPad7,6","name":"iPad 6th Gen (WiFi+Cellular)"},
            {"id":"iPad7,11","name":"iPad 7th Gen 10.2-inch (WiFi)"},
            {"id":"iPad7,12","name":"iPad 7th Gen 10.2-inch (WiFi+Cellular)"},
            {"id":"iPad8,1","name":"iPad Pro 3rd Gen (11 inch, WiFi)"},
            {"id":"iPad8,2","name":"iPad Pro 3rd Gen (11 inch, 1TB, WiFi)"},
            {"id":"iPad8,3","name":"iPad Pro 3rd Gen (11 inch, WiFi+Cellular)"},
            {"id":"iPad8,4","name":"iPad Pro 3rd Gen (11 inch, 1TB, WiFi+Cellular)"},
            {"id":"iPad8,5","name":"iPad Pro 3rd Gen (12.9 inch, WiFi)"},
            {"id":"iPad8,6","name":"iPad Pro 3rd Gen (12.9 inch, 1TB, WiFi)"},
            {"id":"iPad8,7","name":"iPad Pro 3rd Gen (12.9 inch, WiFi+Cellular)"},
            {"id":"iPad8,8","name":"iPad Pro 3rd Gen (12.9 inch, 1TB, WiFi+Cellular)"},
            {"id":"iPad11,1","name":"iPad mini 5th Gen (WiFi)"},
            {"id":"iPad11,2","name":"iPad mini 5th Gen"},
            {"id":"iPad11,3","name":"iPad Air 3rd Gen (WiFi)"},
            {"id":"iPad11,4","name":"iPad Air 3rd Gen"}
            ]

        if t == "watch" or t == "Watch":
            t = [
            {"id":"Watch1,1","name":"Apple Watch 38mm case"},
            {"id":"Watch1,2","name":"Apple Watch 42mm case"},
            {"id":"Watch2,6","name":"Apple Watch Series 1 38mm case"},
            {"id":"Watch2,7","name":"Apple Watch Series 1 42mm case"},
            {"id":"Watch2,3","name":"Apple Watch Series 2 38mm case"},
            {"id":"Watch2,4","name":"Apple Watch Series 2 42mm case"},
            {"id":"Watch3,1","name":"Apple Watch Series 3 38mm case (GPS+Cellular)"},
            {"id":"Watch3,2","name":"Apple Watch Series 3 42mm case (GPS+Cellular)"},
            {"id":"Watch3,3","name":"Apple Watch Series 3 38mm case (GPS)"},
            {"id":"Watch3,4","name":"Apple Watch Series 3 42mm case (GPS)"},
            {"id":"Watch4,1","name":"Apple Watch Series 4 40mm case (GPS)"},
            {"id":"Watch4,2","name":"Apple Watch Series 4 44mm case (GPS)"},
            {"id":"Watch4,3","name":"Apple Watch Series 4 40mm case (GPS+Cellular)"},
            {"id":"Watch4,4","name":"Apple Watch Series 4 44mm case (GPS+Cellular)"},
            {"id":"Watch5,1","name":"Apple Watch Series 5 40mm case (GPS)"},
            {"id":"Watch5,2","name":"Apple Watch Series 5 44mm case (GPS)"},
            {"id":"Watch5,3","name":"Apple Watch Series 5 40mm case (GPS+Cellular)"},
            {"id":"Watch5,4","name":"Apple Watch Series 5 44mm case (GPS+Cellular)"}
            ]

        if amount == None or amount == 1 or amount < 1:
            return random.choice(t)
        else:
            generatedlist = []

            for x in range(amount):
                generatedlist.append(random.choice(t))

            return generatedlist
