import cv2
import os

LABELS = ['one', 'two', 'three']

##### Active here to capture image from video file #####
# FILE_NAME_OR_WEBCAM_INDEX = 'video.mp4' # Video file name
# DELAY = 0 # 0 for video

##### Active here to capture image from webcam #####
FILE_NAME_OR_WEBCAM_INDEX = 0 # Webcam index
DELAY = 1 # 1 for Webcam

class ImageCapturer:
    '''
    Usage:
    Press label index to capture and save the frame as an image.
    Press 'q' to quit the program.
    Press any other key to skip to the next frame (only for videos).
    '''

    def __init__(self, labels, file_name_or_webcam_index=0, delay=1, output_folder='Images'):
        self.labels = labels
        self.file_name_or_webcam_index = file_name_or_webcam_index
        self.delay = delay
        self.output_folder = output_folder
        self.count_per_label = [0 for i in self.labels]
        self.cap = cv2.VideoCapture(self.file_name_or_webcam_index)
        os.makedirs(self.output_folder, exist_ok=True)

    def capture(self):
        while True:
            _, img = self.cap.read()
            cv2.imshow('Preview', img)
            key = cv2.waitKey(self.delay)
            if key == ord('q'):
                break
            key = key - 48 # ASCII to decimal
            if key >= 0 and key < len(self.labels):
                self.saveImage(img, key)
        self.cap.release()
        cv2.destroyAllWindows()

    def saveImage(self, img, key):
        str_label = self.labels[key]
        str_count = str(self.count_per_label[key]).zfill(3) # the counter will appear as 3 digits
        filename = self.output_folder + '/' + str_label + '-' + str_count + '.jpg'
        cv2.imwrite(filename, img)
        self.count_per_label[key] += 1

if __name__ == '__main__':
    imageCapturer = ImageCapturer(labels=LABELS,
                                file_name_or_webcam_index=FILE_NAME_OR_WEBCAM_INDEX,
                                delay=DELAY)
    imageCapturer.capture()