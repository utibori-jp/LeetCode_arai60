# 001 - Two Sum

- URL: https://leetcode.com/problems/two-sum/
- カテゴリ: Array / Hash Table
- 難易度: Easy

## 解いた日
2026-04-28

## 問題の本質

配列から2要素を選んで合計が target になるインデックスのペアを返す。
「あるインデックス i を見たとき、残りに必要な値がすでに登場済みかどうか」を
即座に調べる方法を考えると、探索の回数を大幅に減らせる。

## 自分のアプローチ
(自分で記入)

## レビュー結果

**テスト結果**: 6/6 passed ✓

**正しさ**: 正確。`i+1` から走査しているので同一インデックスの重複使用はなく、問題の制約（exactly one solution）下で必ず正解を返せる。

### 計算量

| | 自解 (brute force) |
|---|---|
| 時間 | O(n²) — 二重ループ |
| 空間 | O(1) |

### より良い解法

**Hash Map（1パス）** — O(n) 時間 / O(n) 空間

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

考え方: 各要素 `num` を見たとき、`target - num` がすでに `seen` に登録済みなら即座に返せる。1回の走査で完結するため O(n)。

### 類題・関連パターン

- **Two Pointers（ソート済み配列）**: LeetCode 167 Two Sum II — ソート後に左右から詰めると O(n)
- **3Sum / 4Sum**: LeetCode 15, 18 — 同じ「complement を探す」発想を多重ループに拡張
- **Subarray Sum Equals K**: LeetCode 560 — prefix sum + Hash Map という同系統のパターン
- パターン: **Hash Map で「あと何が必要か」を O(1) ルックアップ**

## 学んだこと


## 復習チェック
- [ ] 1日後 (2026-04-29)
- [ ] 1週間後 (2026-05-05)
- [ ] 1ヶ月後 (2026-05-28)
