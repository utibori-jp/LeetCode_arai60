問題：https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

### Step 1（普通に解いてみる）
1つ目のノードの取り扱いをどうしようか考えていたが、結局うまくいかずChetGPTに聞いた。
番兵ノードは後ろに置くものというイメージだったが、今回の問題では先頭に置くことで、1つ目のノードが重複していた場合も、それ以降のノードと同じように扱えることが発見だった。
ノードが重複していたときは、prevNode.Nextを、重複していない時にprevNodeを更新することで、prevNode.Nextがユニークな値につながるまで更新され続け、結果ユニークな値のリストになるという発想は面白かった。

時間計算量(N)
空間計算量(1)

```Go
func deleteDuplicates(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }

    sentinelNode := &ListNode{Val: 0, Next: head}

    prevNode := sentinelNode
    candidateNode := head
    for candidateNode != nil {
        if candidateNode.Next != nil && candidateNode.Val == candidateNode.Next.Val {
            for candidateNode.Next != nil && candidateNode.Val == candidateNode.Next.Val {
                candidateNode = candidateNode.Next
            }

            prevNode.Next = candidateNode.Next
        } else {
            prevNode = candidateNode
        }
        
        candidateNode = candidateNode.Next
    }

    return sentinelNode.Next
}
```

- 他の解法
  - 再帰を用いる
- 他の人の解答
  - https://github.com/hroc135/leetcode/blob/4850d771dbac4381a752745f4d3c58a82e836664/82RemoveDuplicatesFromSortedListII.md
  - https://github.com/kazukiii/leetcode/pull/5/commits/6f0b47e756e954af07f99dad8a37c3d99c8ef65a

### Step2（別の解法があればそちらを試す）

**別解1**：再帰を用いる
基本的な発想はStep1の解法と同じ。
現在のノードと次のノードの値が等しければ、等しくなくなるまでheadを後ろへ動かす。
時間計算量(N)
空間計算量(N)

参考：

```Go
func noDuplicatesSortedList(head *ListNode) *ListNode {
    if head == nil {
        return nil
    }

    if head.Next != nil && head.Val == head.Next.Val {
        for head.Next != nil && head.Val == head.Next.Val {
            head = head.Next
        }

        return noDuplicatesSortedList(head.Next)
    } else {
        head.Next = noDuplicatesSortedList(head.Next)
        return head
    }
}

func deleteDuplicates(head *ListNode) *ListNode {
    return noDuplicatesSortedList(head)
}
```

メモ

### Step3（関連知識を調べる）
番兵法について
- [番兵法を用いた線形探索](https://zenn.dev/fikastudio/articles/2f6c27a12d10e7)
- [番兵法を用いると何がいいのか](https://qiita.com/tundes/items/2cc25fbcd5ab52a19000)
- [番兵法（線形探索の改良型）](https://www.youtube.com/watch?v=3CEB_wF-uno&ab_channel=%E6%83%85%E5%A0%B1%E2%85%A0%E3%82%92%E5%AD%A6%E3%81%B6%E3%81%9F%E3%82%81%E3%81%AE%E3%83%81%E3%83%A3%E3%83%B3%E3%83%8D%E3%83%AB)
