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
    
    generation_status = "Generating"
    
    generation_thread = threading.Thread(target=generate_data, args=(a, selected_options, generation_status))
    generation_thread.start()
    result_data = generate_data(a, selected_options, generation_status)
    
    return render_template('result.html', a=a, selected_labels=selected_labels,generation_status=generation_status,result_data=result_data)

def generate_data(a, selected_options, generation_status):
    # 在生成函数执行期间，将生成状态参数设置为"Generating"
    # 在生成完成后，将生成状态参数设置为"Result"
    try:
        # 调用生成函数
        result_data = get_random_url(a)
    
        # 生成完成后，将生成状态参数设置为"Result"
        generation_status = "Result"

        # 在这里进行其他后续操作，如保存文件等
        return result_data
    
    except Exception as e:
        # 处理生成函数的异常情况
        generation_status = "Error"
        return None

def get_random_url(a):
  
    if a == 64:
        url_midi = get_random_midi_url('out/64',64)
    elif a == 128:
        url_midi = get_random_midi_url('out/128',128)
    else:
        url_midi = None  # 处理其他情况
    
    time.sleep(5)  # 添加延时，单位为秒
    
    return f'{url_midi}'

def get_random_midi_url(directory,a):
    # 假设在指定目录中有多个MIDI文件
    # 这里使用随机数选择一个文件
    
    if a == 64:
        midi_files = ['64-1.mid', '64-2.mid', '64-3.mid']
    elif a == 128:
        midi_files = ['128-1.mid', '128-2.mid', '128-3.mid','128-4.mid', '128-5.mid', '128-6.mid']
    
    random_file = random.choice(midi_files)
    return f'https://cdn.jsdelivr.net/gh/TheYuhan-Lu/CutieSound@first/cutiesound/{directory}/{random_file}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
