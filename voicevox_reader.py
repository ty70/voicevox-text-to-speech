# -----------------------------------------------
# voicevox_reader.py
#
# VOICEVOXエンジンと連携して、テキストを音声に変換し保存するスクリプト
#
# 用途:
#   コマンドライン引数から、入力ファイル・出力ファイル・話者IDを指定し
#   VOICEVOXで読み上げ音声を生成（MP3形式で保存）
#
# 入力:
#   --input: テキストファイルのパス（UTF-8）
#   --output: 出力ファイルパス（.mp3）
#   --speaker_id: 話者ID（デフォルト: 3 = ずんだもん）
#
# 出力:
#   指定パスに音声ファイル（MP3）を保存
# -----------------------------------------------

import argparse
import requests
from pydub import AudioSegment
import io
from tqdm import tqdm

# VOICEVOXエンジンのAPIエンドポイント
VOICEVOX_URL = "http://127.0.0.1:50021"

def synthesize_voice(text, speaker=3, output_path="output.mp3"):
    # プログレスバー表示のためのステップ風
    steps = ["クエリ作成", "音声合成", "音声変換・保存"]
    for i, step in enumerate(tqdm(steps, desc="処理中", unit="ステップ")):
        if step == "クエリ作成":
            params = {"text": text, "speaker": speaker}
            res1 = requests.post(f"{VOICEVOX_URL}/audio_query", params=params)
            if res1.status_code != 200:
                raise Exception(f"audio_queryエラー: {res1.text}")
            query = res1.json()

        elif step == "音声合成":
            res2 = requests.post(f"{VOICEVOX_URL}/synthesis", params={"speaker": speaker}, json=query)
            if res2.status_code != 200:
                raise Exception(f"synthesisエラー: {res2.text}")
            wav_data = res2.content

        elif step == "音声変換・保存":
            audio = AudioSegment.from_file(io.BytesIO(wav_data), format="wav")
            audio.export(output_path, format="mp3")

    print(f"\n✅ 音声ファイルを保存しました: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VOICEVOXでテキストを音声合成")
    parser.add_argument("--input", required=True, help="入力テキストファイル（UTF-8）")
    parser.add_argument("--output", required=True, help="出力音声ファイル（.mp3）")
    parser.add_argument("--speaker_id", type=int, default=3, help="話者ID（例: 3=ずんだもん）")

    args = parser.parse_args()

    # 入力ファイルを読み込む
    with open(args.input, "r", encoding="utf-8") as f:
        text = f.read().strip()

    # 音声合成の実行
    synthesize_voice(text, speaker=args.speaker_id, output_path=args.output)
