import picamera, time, socket

client_socket = socket.socket()
client_socket.connect(("192.168.1.2",8000))

connection = client_socket.makefile("wb")

try:
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 24
        camera.start_preview()
        time.sleep(2)

        camera.start_recording(connection, format = "h264")
        camera.wait_recording(30)
        camera.stop_recording()

finally:
    connection.close()
    client_socket.close()
