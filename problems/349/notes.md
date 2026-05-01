# 349 - Intersection of Two Arrays

- URL: https://leetcode.com/problems/intersection-of-two-arrays/
- カテゴリ: Hash Set / Two Pointers
- 難易度: Easy

## 解いた日
2026/05/01

## 問題の本質
2つの配列から **重複なしの共通要素** を返す問題。
「含まれているかどうか」を効率よく判定するデータ構造を選ぶことがポイント。
重複を自動的に除外できる集合 (set) の性質を活かせるかがカギ。

## 自分のアプローチ

一番シンプルな解法は、nums1とnums2を単純比較して、一致するものをSetに入れていく方法。ただし計算量がO（N^2）。
今回、各要素の最大値は1000なので、nums1とnums2それぞれについて、数字のリスト（あれば1なければ0）に入れていく。2つの数字のリストを順に比較とすれば、計算量はO（N）にはなる。
ただ、setを使ってもっとうまく出来る気がする、、、
2段階のsetを使ってみるとか？num1、nums2それぞれのsetを作る。次に、nums1のsetの各要素について、nums2のset内にあればans_listにappendみたいな。これなら、O（N*K）で済むし、毎回必ず要素が1000のリストを作る必要がなくなる。

## レビュー結果

### 正確性
全テストケース (8/8) パス。正しく動作している。

### 計算量
- 時間計算量: O(N + M) — `set(nums1)` で O(N)、`set(nums2)` で O(M)、ループで O(N) の合計
- 空間計算量: O(N + M) — `nums1_unique_tuple` と `nums2_map` の両方を保持

### 解法の評価
アプローチは正しい。`nums1` を set に変換して重複排除し、`nums2_map` (set) でO(1)ルックアップを行う設計は最適に近い。

変数名が適切で読みやすい（`nums2_map` で set であることが伝わる）。ただし `nums1_unique_tuple` は tuple に変換しているが、set のままループしても同じ動作・同じ計算量になる。tuple 変換は不要。

```python
# よりシンプルな等価実装
nums1_set = set(nums1)
nums2_set = set(nums2)
return list(nums1_set & nums2_set)
```

### より良い解法
Python の set intersection 演算子 `&` を使うと 1 行で書ける。

```python
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))
```

計算量は同じ O(N + M)。内部的に CPython が最適化された C 実装で処理するため定数倍が小さい。

ソートして Two Pointers で解く方法もある（O(N log N + M log M)）が、ハッシュセット解法の方が平均的に速い。

### 類題・関連パターン
- **350 - Intersection of Two Arrays II**: 重複ありの共通要素を返す（各要素の出現回数を `Counter` で管理する）
- **1 - Two Sum**: ハッシュマップで補数を O(1) ルックアップするパターン
- **217 - Contains Duplicate**: set による重複検出の基礎
- **パターン**: 「含まれているか」の判定は set、「何回含まれているか」の判定は Counter (dict) で考える

## 学んだこと

方針は合っていた。Pythonの仕様的な話で、set のintersectionは `&` 演算子で直接計算できる
また、setをわざわざtupleへ変換しなくても、forループに使える（set 自体がイテラブル）
`nums2_set` のように変数名でデータ構造を示すのは良い習慣とのこと

## 復習チェック
- [ ] 1日後 (2026-05-02)
- [ ] 1週間後 (2026-05-08)
- [ ] 1ヶ月後 (2026-06-01)
