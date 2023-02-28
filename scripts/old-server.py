class Webserver:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.add_url_rule("/", view_func=self.__index)
        self.app.add_url_rule("/mjpeg", view_func=self.__mjpeg)
        self.app.add_url_rule("/send_yes", view_func=self.__send_yes)

        self.cam = Camera()
    
    def run(self, ip, port):
        self.app.run(host=ip, port=port)
    
    def __index(self):
        return render_template('app.html')
    
    def __send_yes(self):
        msg = String()
        msg.data = "yes"
        yes_pub.publish(msg)

    def __mjpeg(self):
        return Response(self.gather_img(), mimetype='multipart/x-mixed-replace; boundary=frame')
    
    def gather_img(self):
        while True:
            # time.sleep(0.01)
            frame = self.cam.capture()
            yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n')

if __name__ == '__main__':
    threading.Thread(target=lambda: rospy.init_node('otomo_webserver', disable_signals=True)).start()
    ws = Webserver()
    ws.run('127.0.0.1', 8080)
