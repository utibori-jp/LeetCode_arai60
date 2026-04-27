# LeetCode 新井60問

新井60問 (LeetCode) を Claude Code と協働して学習するためのリポジトリです。

## セットアップ

```bash
uv sync
```

## tasks.py コマンド

```bash
uv run python tasks.py test 001   # 問題001のテストを実行
uv run python tasks.py test-all   # 全問題のテストを実行
uv run python tasks.py list       # 問題一覧を表示
```

## Claude Code コマンド

| コマンド | 動作 |
|----------|------|
| `start 001` | フォルダ・スケルトン・テストケース・notes.md を生成 |
| `review 001` | テスト実行 + 解法評価 + notes.md に結果を追記 |
| `due` | 今日復習すべき問題を一覧表示 |

## ディレクトリ構成

```
.
├── pyproject.toml
├── tasks.py
├── .claude/
│   └── templates/arai60/    # ファイル生成テンプレート
└── problems/
    └── 001/
        ├── README.md
        ├── solution.py
        ├── test_solution.py
        └── notes.md
```

## 学習フロー

1. Claude Code に `start XXX` と伝える
2. `problems/XXX/solution.py` に実装する
3. `uv run python tasks.py test XXX` でテストを実行する
4. Claude Code に `review XXX` と伝える
