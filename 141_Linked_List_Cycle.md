問題：https://leetcode.com/problems/linked-list-cycle/

### Step 1（普通に解いてみる）
単純解法
Setを使って、current.Nextが既に訪れた場所か判定する

時間計算量（N）
空間計算量（N）

```Go
func hasCycle(head *ListNode) bool {
    if head == nil || head.Next == nil {
        return false
    }

    visited := make(map[*ListNode]struct{})

    current := head
    for current != nil {
        if _, ok := visited[current]; ok {
            return true
        }

        visited[current] = struct{}{}
        current = current.Next
    }

    return false
}
```
メモ
- 他に考えられる解法
    - fastポインタとslowポインタを使うフロイドの循環検出アルゴリズムを利用した解法

### Step2（別の解法があればそちらを試す）
fastポインタとsloポインタを使うフロイドの循環検出アルゴリズムを利用した解法

時間計算量（N）
空間計算量（1）

参考：https://ja.wikipedia.org/wiki/%E3%83%95%E3%83%AD%E3%82%A4%E3%83%89%E3%81%AE%E5%BE%AA%E7%92%B0%E6%A4%9C%E5%87%BA%E6%B3%95

```Go
func hasCycle(head *ListNode) bool {
    if head == nil || head.Next == nil {
        return false
    }

    slow := head
    fast := head
    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next

        if slow == fast {
            return true
        }
    }
    return false
}
```

メモ
変数名について、[他の方のPR](https://github.com/hroc135/leetcode/pull/1/files)で議論があったが、[Go Style Guide](https://google.github.io/styleguide/go/decisions#naming)に従い、fastとslowのままとした。

### Step3（関連知識を調べる
ポインタについて、他の方が読んでいたものを読んでみる
https://medium.com/@jamal.kaksouri/a-comprehensive-guide-to-pointers-in-go-4acc58eb1f4d

LinkedListの使いどころについて
https://techblog.kayac.com/effective-linked-list
