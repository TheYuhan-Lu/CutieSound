from flask import Flask, render_template, request
import random
import time
import threading

app = Flask(__name__,static_folder="static")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/music')
def music():
    return render_template('music.html')


@app.route('/result', methods=['POST'])
def result():
    a = request.form['length']
    selected_options = request.form.getlist('options')

    # 转换成原始标签值
    options_labels = {
        '0': 'Bach',
        '1': 'Handel',
        '2': 'Pachelbel',
        '3': 'Burgmueller',
        '4': 'Clementi',
        '5': 'Haydn',
        '6': 'Beethoven',
        '7': 'Brahms',
        '8': 'Mozart',
        '9': 'Balakirew',
        '10': 'Borodin',
        '11': 'Brahms',
        '12': 'Chopin',
        '13': 'Debussy',
        '14': 'Liszt',
        '15': 'Mendelssohn',
        '16': 'Moszkowski',
        '17': 'Mussorgsky',
        '18': 'Machmaninov',
        '19': 'Mchubert',
        '20': 'Mchumann',
        '21': 'Tchaikovsky',
        '22': 'Tschai'
    }
    selected_labels = [options_labels[option] for option in selected_options]
    
    
    
    return render_template('result.html', a=a, selected_labels=selected_labels)

def get_midi_url(length):
    
    time.sleep(5)  # 添加延时，单位为秒
    if length == 64:
        folder = '64'
        midi_files = ['64-1.mid', '64-2.mid', '64-3.mid']
    elif length == 128:
        folder = '128'
        midi_files = ['128-1.mid', '128-2.mid', '128-3.mid','128-4.mid', '128-5.mid', '128-6.mid']
    else:
        raise ValueError('Invalid length.')

    # 在特定目录下随机选择一个.mid文件
    # 这里使用了示例的链接，你可以根据需要修改
    base_url = 'https://cdn.jsdelivr.net/gh/TheYuhan-Lu/CutieSound@1.0/cutiesound/out'
     # 这里需要替换为实际的文件列表
    random_file = random.choice(midi_files)
    midi_url = f'{base_url}/{folder}/{random_file}'
    
    return midi_url

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
