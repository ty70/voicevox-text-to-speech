# VOICEVOX Text-to-Speech Pipeline

このリポジトリでは、VOICEVOXエンジンを使用して、テキストを音声（MP3形式）に変換する Python スクリプト `voicevox_reader.py` を提供します。

## 🚀 主な機能

- テキストファイルから音声ファイル（MP3）を生成
- VOICEVOXエンジンと連携
- 話者IDの指定可能（デフォルト: ずんだもん）

# サンプル
```
sample.mp3
```
(smaple.txtを入力として出来たもの)
---

## ✅ 必要なもの

- Python 3.8+
- VOICEVOX エンジン（ローカルで動作）
- pip で以下のパッケージをインストール:

```bash
pip install requests pydub tqdm
```

---

## 🖥️ VOICEVOX エンジンの準備（Linux）

### 1. VOICEVOX エンジンのダウンロード

VOICEVOX公式のリリースページから以下のファイルを取得してください:

- `voicevox_engine-linux-nvidia-0.23.0.7z.001`
- `voicevox_engine-linux-nvidia-0.23.0.7z.002`

[🔗 VOICEVOX エンジン ダウンロード](https://github.com/VOICEVOX/voicevox_engine/releases)

### 2. 7zで展開（自動で結合＆展開）

`.001` ファイルだけを指定すれば、自動で結合・展開されます：

```bash
# 7z が未インストールならインストール
sudo apt install p7zip-full

# 展開（.001だけ指定すればOK）
7z x voicevox_engine-linux-nvidia-0.23.0.7z.001
```

これで linux-nvidia が作成される

### 3. VOICEVOXエンジンの起動

```bash
cd linux-nvidia
./run
```

エンジンが `http://127.0.0.1:50021` で起動します。

---

## 📜 スクリプトの使い方

### コマンド構文

```bash
python voicevox_reader.py --input input.txt --output output.mp3 --speaker_id 3
```

- `--input`: 入力するテキストファイル（UTF-8）
- `--output`: 出力する音声ファイル名（.mp3）
- `--speaker_id`: 話者ID（例：3 = ずんだもん）

---

## 💡 話者IDの例（VOICEVOX 0.23.0 時点）

| 話者名       | ID |
|--------------|----|
| 四国めたん    | 0  |
| ずんだもん    | 3  |
| 春日部つむぎ | 8  |
| 雨晴はう     | 10 |

（※ 最新のIDは VOICEVOX エンジン起動時に `/speakers` で確認可能）

---

## 📁 フォルダ構成例

```
.
├── voicevox_reader.py
├── input.txt
└── output.mp3
```

---

## 🧾 ライセンス

このスクリプトは MIT ライセンスで提供されています。詳細は [LICENSE](./LICENSE) をご覧ください。

---

## 🔗 関連リンク

- [VOICEVOX 公式サイト](https://voicevox.hiroshiba.jp/)
- [VOICEVOX GitHub](https://github.com/VOICEVOX/voicevox_engine)
