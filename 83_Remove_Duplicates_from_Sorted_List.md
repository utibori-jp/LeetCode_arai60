問題：

### Step 1（普通に解いてみる）
単純解法
現在のノードと次のノードを比較し、値が等しければ、次のノードを飛ばす
時間計算量(N)
空間計算量(1)

```Go
func deleteDuplicates(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }

    current := head
    for current != nil && current.Next != nil {
        if current.Val == current.Next.Val {
            current.Next = current.Next.Next
            continue
        }

        current = current.Next
    }

    return head
}
```
メモ
- 他に考えられる解法
    - 再帰を用いて解く
    - 2つのポインタを使って解く

### Step2（別の解法があればそちらを試す）

**別解1**：再帰を用いて解く
後ろから、重複のないNodeを繋げていく。
現在のノードと、それ以降の重複のないリストの先頭ノードを比較し、値が等しければ現在のノードは飛ばす。
実装がシンプルで個人的には結構好き。ただ、重複のないリストが後ろからできていくというのは、初見の直感に反するため、読み手に負担がかかるかも。

時間計算量(N)
空間計算量(N)

参考：

```Go
func deleteDuplicates(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }
    
    tail := deleteDuplicates(head.Next)
    if head.Val == tail.Val {
        return tail
    } else {
        head.Next = tail
        return head
    }
}
```

**別解1**：2つのポインタを使って解く
2重ループとなるが、外のループと中のループの合計の実行数が、Nとなるため、時間計算量はO(n)となる。

時間計算量(N)
空間計算量(1)

```Go
func deleteDuplicates(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }

    current := head
    for current != nil {
        nextDistinct := current.Next
        for nextDistinct != nil && current.Val == nextDistinct.Val {
            nextDistinct = nextDistinct.Next
        }

        current.Next = nextDistinct
        current = current.Next
    }

    return head
}
```



メモ


### Step3（関連知識を調べる）
