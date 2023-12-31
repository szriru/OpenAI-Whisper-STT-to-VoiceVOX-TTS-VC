![catcher](https://github.com/szriru/OpenAI-Whisper-STT-to-VoiceVOX-TTS/blob/main/assets/images/main.png?raw=true)

# このプロジェクトについて
このプログラムは、OpenAI WhisperのSTT（音声認識）を利用して、ユーザーが話した内容をテキストに変換し、それをVoicevoxのTTS（テキスト読み上げ）に渡すことで、キャラクターにユーザーの話したことをで話させることができるボイスチェンジャープログラムです。

他のボイスチェンジャープログラム（例：MMVC、RVC）では、リアルタイムで声の変換が可能ですが、このプログラムはそれらとは異なり、事前のトレーニングが不要であり、音声の途切れもありません。完全なリアルタイム性を必要としない場合には、このプログラムが適しています。

ただしwhisperとVOICEVOXはローカルで動くのでGPUパワーとVRAMを必要とします。

Youtube動画:https://youtu.be/rYf2CvZsBlg

[始め方](#始め方)

[設定の変更](#設定の変更)

[キャラクターの変更](#キャラクターの変更)

[利用例](#利用例)

# 始め方

## VOICEVOX ENGINEの準備
VOICEVOXサーバーはこのプログラムとは独立して動くのでまずそれを準備する必要があります。
https://github.com/VOICEVOX/voicevox_engine
こちらからダウンロードしてセットアップしてください。
run.exeを起動してVOICEVOX ENGINEのサーバーが立ち上がればよいです。

## ffmpegのインストール
openai-whisperはffmpegという動画・音声処理ソフトウェアを必要とするのでそれもインストールしてください。

https://ffmpeg.org/download.html

## 方法1 Anaconda
(Anacondaは環境管理ソフトウェアです。環境管理とは、異なるPythonパッケージや依存関係を管理し、複数のプロジェクトで異なる環境を簡単に作成・切り替えることができる機能です。Anacondaを使用すると、仮想環境を作成し、それぞれの環境に必要なパッケージをインストールすることができます。これにより、プロジェクトごとに独立した環境を作成し、パッケージの競合や互換性の問題を回避することができます。)

1. リポジトリをクローンする

まずこのリポジトリをクローンします。

```
$ git clone https://github.com/szriru/OpenAI-Whisper-STT-to-VoiceVOX-TTS Kawaii-Voice
$ cd Kawaii-Voice
$ cd src
```

2. Anacondaの仮想環境を作成する

```
$ conda create --name KawaiiVoice --file environment.yml
$ conda activate KawaiiVoice
```

3. 必要なパッケージのインストール

確認環境: Windows 11, RTX 4000シリーズ

pytorch系とその他必要なパッケージをインストールします。

```
$ conda install torch torchvision torchaudio -c pytorch
$ pip install -r requirements.txt
```

4. 起動

VOICEVOXサーバーが動いていることを確認してからこのプログラムを起動してください。
Readyと表示されたら設定したキーを押して話してください。話し終わったらキーを離してください。
デフォルトはマウスの手前のサイドボタンになっています。

```
$ python main.py
```

# 設定の変更

設定はsrc/config.yamlから変更できます。
whisperのモデルの大きさ、whisperでgpuを使用するかどうか、VOICEVOXのキャラクター,録音のためのキー・マウスボタン, 音声出力アウトプットなどを変更できます。

src/utilsのcheckOutputDevices.pyから出力アウトプットのID,keyCodeChecker.pyから使いたいキーボードの番号を確認できます。

```
$ python utils/checkOutputDevices.py
$ python utils/keyCodeChecker.py
```


# 利用例

ボイスチェンジャー後の声のみをゲーム内などで出力したい場合は[Voice Meeter](https://vb-audio.com/Voicemeeter/)を利用するのが良いです。
インストール後,Voice Meeter Inputを出力デバイスに追加して、ゲーム内でVoice Meeter Outputをゲーム内ボイスチャットのインプットとして利用するのが良いです。

# 説明

![explanation](https://github.com/szriru/OpenAI-Whisper-STT-to-VoiceVOX-TTS/blob/main/assets/images/explanation.svg)

# キャラクター一覧

```json
[
  {
    "supported_features": {
      "permitted_synthesis_morphing": "SELF_ONLY"
    },
    "name": "四国めたん",
    "speaker_uuid": "7ffcb7ce-00ec-4bdc-82cd-45a8889e43ff",
    "styles": [
      {
        "name": "ノーマル",
        "id": 2
      },
      {
        "name": "あまあま",
        "id": 0
      },
      {
        "name": "ツンツン",
        "id": 6
      },
      {
        "name": "セクシー",
        "id": 4
      },
      {
        "name": "ささやき",
        "id": 36
      },
      {
        "name": "ヒソヒソ",
        "id": 37
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "SELF_ONLY"
    },
    "name": "ずんだもん",
    "speaker_uuid": "388f246b-8c41-4ac1-8e2d-5d79f3ff56d9",
    "styles": [
      {
        "name": "ノーマル",
        "id": 3
      },
      {
        "name": "あまあま",
        "id": 1
      },
      {
        "name": "ツンツン",
        "id": 7
      },
      {
        "name": "セクシー",
        "id": 5
      },
      {
        "name": "ささやき",
        "id": 22
      },
      {
        "name": "ヒソヒソ",
        "id": 38
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "春日部つむぎ",
    "speaker_uuid": "35b2c544-660e-401e-b503-0e14c635303a",
    "styles": [
      {
        "name": "ノーマル",
        "id": 8
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "雨晴はう",
    "speaker_uuid": "3474ee95-c274-47f9-aa1a-8322163d96f1",
    "styles": [
      {
        "name": "ノーマル",
        "id": 10
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "波音リツ",
    "speaker_uuid": "b1a81618-b27b-40d2-b0ea-27a9ad408c4b",
    "styles": [
      {
        "name": "ノーマル",
        "id": 9
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "玄野武宏",
    "speaker_uuid": "c30dc15a-0992-4f8d-8bb8-ad3b314e6a6f",
    "styles": [
      {
        "name": "ノーマル",
        "id": 11
      },
      {
        "name": "喜び",
        "id": 39
      },
      {
        "name": "ツンギレ",
        "id": 40
      },
      {
        "name": "悲しみ",
        "id": 41
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "白上虎太郎",
    "speaker_uuid": "e5020595-5c5d-4e87-b849-270a518d0dcf",
    "styles": [
      {
        "name": "ふつう",
        "id": 12
      },
      {
        "name": "わーい",
        "id": 32
      },
      {
        "name": "びくびく",
        "id": 33
      },
      {
        "name": "おこ",
        "id": 34
      },
      {
        "name": "びえーん",
        "id": 35
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "青山龍星",
    "speaker_uuid": "4f51116a-d9ee-4516-925d-21f183e2afad",
    "styles": [
      {
        "name": "ノーマル",
        "id": 13
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "冥鳴ひまり",
    "speaker_uuid": "8eaad775-3119-417e-8cf4-2a10bfd592c8",
    "styles": [
      {
        "name": "ノーマル",
        "id": 14
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "SELF_ONLY"
    },
    "name": "九州そら",
    "speaker_uuid": "481fb609-6446-4870-9f46-90c4dd623403",
    "styles": [
      {
        "name": "ノーマル",
        "id": 16
      },
      {
        "name": "あまあま",
        "id": 15
      },
      {
        "name": "ツンツン",
        "id": 18
      },
      {
        "name": "セクシー",
        "id": 17
      },
      {
        "name": "ささやき",
        "id": 19
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "SELF_ONLY"
    },
    "name": "もち子さん",
    "speaker_uuid": "9f3ee141-26ad-437e-97bd-d22298d02ad2",
    "styles": [
      {
        "name": "ノーマル",
        "id": 20
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "剣崎雌雄",
    "speaker_uuid": "1a17ca16-7ee5-4ea5-b191-2f02ace24d21",
    "styles": [
      {
        "name": "ノーマル",
        "id": 21
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "WhiteCUL",
    "speaker_uuid": "67d5d8da-acd7-4207-bb10-b5542d3a663b",
    "styles": [
      {
        "name": "ノーマル",
        "id": 23
      },
      {
        "name": "たのしい",
        "id": 24
      },
      {
        "name": "かなしい",
        "id": 25
      },
      {
        "name": "びえーん",
        "id": 26
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "後鬼",
    "speaker_uuid": "0f56c2f2-644c-49c9-8989-94e11f7129d0",
    "styles": [
      {
        "name": "人間ver.",
        "id": 27
      },
      {
        "name": "ぬいぐるみver.",
        "id": 28
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "No.7",
    "speaker_uuid": "044830d2-f23b-44d6-ac0d-b5d733caa900",
    "styles": [
      {
        "name": "ノーマル",
        "id": 29
      },
      {
        "name": "アナウンス",
        "id": 30
      },
      {
        "name": "読み聞かせ",
        "id": 31
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "ちび式じい",
    "speaker_uuid": "468b8e94-9da4-4f7a-8715-a22a48844f9e",
    "styles": [
      {
        "name": "ノーマル",
        "id": 42
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "櫻歌ミコ",
    "speaker_uuid": "0693554c-338e-4790-8982-b9c6d476dc69",
    "styles": [
      {
        "name": "ノーマル",
        "id": 43
      },
      {
        "name": "第二形態",
        "id": 44
      },
      {
        "name": "ロリ",
        "id": 45
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "小夜/SAYO",
    "speaker_uuid": "a8cc6d22-aad0-4ab8-bf1e-2f843924164a",
    "styles": [
      {
        "name": "ノーマル",
        "id": 46
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "ナースロボ＿タイプＴ",
    "speaker_uuid": "882a636f-3bac-431a-966d-c5e6bba9f949",
    "styles": [
      {
        "name": "ノーマル",
        "id": 47
      },
      {
        "name": "楽々",
        "id": 48
      },
      {
        "name": "恐怖",
        "id": 49
      },
      {
        "name": "内緒話",
        "id": 50
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "†聖騎士 紅桜†",
    "speaker_uuid": "471e39d2-fb11-4c8c-8d89-4b322d2498e0",
    "styles": [
      {
        "name": "ノーマル",
        "id": 51
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "雀松朱司",
    "speaker_uuid": "0acebdee-a4a5-4e12-a695-e19609728e30",
    "styles": [
      {
        "name": "ノーマル",
        "id": 52
      }
    ],
    "version": "0.14.2"
  },
  {
    "supported_features": {
      "permitted_synthesis_morphing": "ALL"
    },
    "name": "麒ヶ島宗麟",
    "speaker_uuid": "7d1e7ba7-f957-40e5-a3fc-da49f769ab65",
    "styles": [
      {
        "name": "ノーマル",
        "id": 53
      }
    ],
    "version": "0.14.2"
  }
]
```
