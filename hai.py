import cv2 

img = cv2.imread("img/p04dgby5.jpg",6)


print(img.shape)


#gray scale image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#resize image
resize=cv2.resize(img,(200,200))

#add text
text="hello"
coordintes=(50,50)
font=cv2.FONT_HERSHEY_SIMPLEX
fontsize=1
color=(222,225,0)
fontthickness=2
txt=cv2.putText(img,text,coordintes,font,fontsize,color,fontthickness)


#display a line

pt1=(200,200)
pt2=(500,500)
color=(255,255,55)
thickness=2
line=cv2.line(img,(200,200),(500,500),(255,255,55),2)


#draw a circle

center=(200,200)
radius=150
COLOR=(255,255,55)
THICK=2
circle=cv2.circle(img,center,radius,COLOR,THICK)

#draw a rectangle


pt1=(200,200)#top left
pt2=(500,500)#bottom right
color=(255,255,255)#white
thickness=2
rect=cv2.rectangle(img,(200,200),(500,500),(255,255,55),2)

#draw a ellipse
center=(200,200)
axeslen=(100,100)
angle=30
startangle=0
endangle=0
color=(255,255,255)
thickness=2


ellipse=cv2.ellipse(img,center,axeslen,angle,startangle,endangle,color,thickness)


#displaying in grya ,bg ,rgb
gray=cv2.imread('img/p04dgby5.jpg',0)
#1 for bgr

#video cam

vid=cv2.VideoCapture(0)

while True:
    ret,frame=vid.read()#ret gives 1 for capturing and 0 for not capturing and frame give te img in 1 millisec

    cv2.imshow("frame",frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):#the ord func captures the ascii code of the key we press and compared it to 0xff which the code for q
        break



#cv2.imshow("image",vid)
#cv2.waitKey(0)

cv2.destroyAllWindows()