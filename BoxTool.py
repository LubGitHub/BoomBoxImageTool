from PIL import Image
import argparse
import math

parser = argparse.ArgumentParser(
                    prog='Python Boombox Tools',
                    description='What the program does',)
                    
parser.add_argument('-c', '--cut', action='store_true')
parser.add_argument('-f', '--fill', action='store_true')
parser.add_argument('-hi', '--height', action='store_true')

args = parser.parse_args()

im = Image.open("import.png").convert("L")

ImgSyq = list(Image.Image.getdata(im))

if (args.cut == True):

    with open("output_cut.mcfunction", "w") as test:
        for n in range(0,len(ImgSyq)):
    
            h = ImgSyq[n]
            x = (n % 105) - 52
            z = math.floor(n/105-52)
            
            if h == 0:
                test.writelines("fill "+str(x)+" 12 "+str(z)+" "+str(x)+" 62 "+str(z)+" air \n")

elif (args.fill == True):

    with open("output_fill.mcfunction", "w") as test:
        for n in range(0,len(ImgSyq)):
    
            h = ImgSyq[n]
            x = (n % 105) - 52
            z = math.floor(n/105-52)
            
            if h != 0:
                test.writelines("fill "+str(x)+" 1 "+str(z)+" "+str(x)+" "+str(int(h/4-0.75))+" "+str(z)+" bedrock \n")
            
elif (args.height == True):

    with open("output_height.mcfunction", "w") as test:
        for n in range(0,len(ImgSyq)):
        
            h = ImgSyq[n]
            x = (n % 105) - 52
            z = math.floor(n/105-52)
            
            if h == 0:
                test.writelines("fill "+str(x)+" 12 "+str(z)+" "+str(x)+" 62 "+str(z)+" air \n")
            else:
                test.writelines("clone "+ str(x) +" 12 "+ str(z) +" "+ str(x) +" 33 "+ str(z) +" "+ str(x) +" "+ str(int(h/7+1)) +" "+ str(z) +" replace move \n")
print('Done!')