import cv2 as cv
import mediapipe as mp
import pyautogui as py
import math

video = cv.VideoCapture(0)

mp_draw=mp.solutions.drawing_utils
mp_hand=mp.solutions.hands

hands=mp_hand.Hands(
  static_image_mode=False,       
  max_num_hands=2,              
  min_detection_confidence=0.7, 
  min_tracking_confidence=0.5 
)
prev_x, prev_y = 0, 0

while True:
  isTrue, frame=video.read()

  if isTrue is False:
    break

  frame=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
  frame=cv.flip(frame,1)
  frame.flags.writeable=False

  result=hands.process(frame)
  frame.flags.writeable=True

  if result.multi_hand_landmarks:
    for hand_landmarks in result.multi_hand_landmarks:
      screen_width,screen_height=py.size()

      index_tip=hand_landmarks.landmark[8]
      index_joint=hand_landmarks.landmark[6]

      thumb_tip=hand_landmarks.landmark[4]
      part_x=(thumb_tip.x-index_tip.x)**2
      part_y=(thumb_tip.y-index_tip.y)**2

      dist=math.sqrt(part_x+part_y)
      if dist < 0.05:
        py.click()

      if index_tip.y<index_joint.y:
        screen_x=int(index_tip.x*screen_width)
        screen_y=int(index_tip.y*screen_height)

        if abs(screen_x - prev_x) < 5 and abs(screen_y - prev_y) < 5:
          continue

        smooth_x=prev_x + (screen_x-prev_x)*0.2
        smooth_y=prev_y + (screen_y-prev_y)*0.2

        py.moveTo(smooth_x, smooth_y)

        prev_x,prev_y=smooth_x,smooth_y

      mp_draw.draw_landmarks(frame, hand_landmarks, mp_hand.HAND_CONNECTIONS)

  key=cv.waitKey(20)
  if key==ord('q'):
    break
  
  frame=cv.cvtColor(frame,cv.COLOR_RGB2BGR)
  cv.imshow('Webcam',frame)

video.release()
cv.destroyAllWindows()