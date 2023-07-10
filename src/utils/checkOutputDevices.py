import pyaudio

def write_output_devices_to_file(filename):
    # PyAudioを初期化
    p = pyaudio.PyAudio()

    # 出力デバイスの数を取得
    num_devices = p.get_device_count()

    # 出力デバイスの情報をテキストファイルに書き込む
    with open(filename, 'w', encoding='utf-8') as f:  # エンコーディングをutf-8に指定
        for i in range(num_devices):
            device_info = p.get_device_info_by_index(i)
            if device_info['maxOutputChannels'] > 0:
                f.write(f"Device {i}: {device_info['name']}\n")

    # PyAudioを終了
    p.terminate()

# 出力デバイス一覧を書き込むテキストファイルの名前を指定
output_file = './output_devices.txt'

# 出力デバイスの一覧をテキストファイルに書き込む
write_output_devices_to_file(output_file)