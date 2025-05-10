from flask import Flask, request

app = Flask(__name__)
logs = []

@app.route('/')
def index():
    ip = request.remote_addr
    if ip not in logs:
        logs.append(ip)
        with open('ip_logs.txt', 'a') as f:
            f.write(ip + '\n')
    return "Bạn đã truy cập thành công! Quay lại Tool và nhập key."

@app.route('/ip_logs.txt')
def get_logs():
    try:
        with open('ip_logs.txt', 'r') as f:
            return f.read(), 200, {'Content-Type': 'text/plain'}
    except:
        return "", 200
