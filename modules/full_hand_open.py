import cv2
import mediapipe as mp
import streamlit as st
import numpy as np
import time

def detect_hand_open():
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
    mp_draw = mp.solutions.drawing_utils

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)   
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)   
    
    frame_placeholder = st.empty()

    detected_frame = None
    start_time = time.time() 
    
    tolerance = 0.05
    
    while cap.isOpened():
        ret, img = cap.read()
        if not ret:
            st.error("Failed to grab frame.")
            break

        img = cv2.flip(img, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Detect victory sign (index and middle fingers open, rest closed)
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                index_base = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
                middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                middle_base = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
                ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
                ring_base = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_MCP]
                pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
                pinky_base = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP]
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                thumb_base = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP]

                is_victory = (
                    index_tip.y < index_base.y - tolerance and
                    middle_tip.y < middle_base.y - tolerance and
                    ring_tip.y > ring_base.y - tolerance and
                    pinky_tip.y > pinky_base.y - tolerance and
                    thumb_tip.x > thumb_base.x + tolerance  # assuming palm toward camera
                )

                if is_victory:
                    cv2.putText(img, "Victory Sign Detected!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
                    detected_frame = img.copy()
                    cap.release()
                    return detected_frame

        # Show webcam frame
        frame_placeholder.image(img, channels="BGR")

        # ⏰ Check if 15 seconds passed
        elapsed_time = time.time() - start_time
        if elapsed_time > 15:
            st.warning("⏰ Time Out! No hand detected in 15 seconds.")
            cap.release()
            return None

        time.sleep(0.01)

    cap.release()
    return None
