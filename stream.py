from flask import Flask, render_template, Response, url_for
import cv2

app = Flask(__name__)

@app.route('/')
def index():
   #Video streaming .
   return render_template('index.html')

def gen():
   while True:
       try:
           image = cv2.imread('static/res.jpg')
           cv2.imwrite('static/stream.jpg', image)
       except:
           image = cv2.imread('static/stream.jpg')
           cv2.imwrite('static/stream.jpg', image)

       frame = open('static/stream.jpg', 'rb').read()
       yield (b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
   #Video streaming route. Put this in the src attribute of an img tag.
   return Response(gen(),
                   mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/', methods=['GET', 'POST'])
def image():
    return '<img src=' + url_for('static',filename='stream.jpg') + '>'

@app.after_request
def add_header(response):
    response.headers['Pragma'] = 'no-cache'
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')