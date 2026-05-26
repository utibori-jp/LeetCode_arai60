問題：

### Step 1（普通に解いてみる）
単純解法
訪れたNodeを記録していき、既に訪れたNodeを検知したとき、そのNodeを返す

時間計算量(N)
空間計算量(N)

```Go
func detectCycle(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return nil
    }

    visited := make(map[*ListNode]struct{})

    current := head
    for current != nil {
        if _, ok := visited[current]; ok {
            return current
        }

        visited[current] = struct{}{}

        current = current.Next
    }

    return nil
}
```
メモ
- 他に考えられる解法
    - フロイドの循環検出アルゴリズムを利用した方法

### Step2（別の解法があればそちらを試す）
まず初めに、フロイドの循環検出アルゴリズムを利用して、循環があるかを判断する。循環がある場合、新たにstartポインタを用意し、startポインタとslowポインタを利用して循環の始点を検出する。

時間計算量(N)
空間計算量(1)

参考：

```Go
func detectCycle(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return nil
    }

    slow := head
    fast := head
    for fast != nil && fast.Next != nil {
        slow = slow.Next
        fast = fast.Next.Next

        if slow == fast {
            break
        }
    }

    if slow != fast {
        return nil
    }

    start := head
    for slow != start {
        slow = slow.Next
        start = start.Next
    }

    return slow
}
```

**別解**
再帰を用いて解く

時間計算量(N)
空間計算量(N)

LeetCodeでは関数外に変数を定義できないため、この方法ではError。
```Go
visited := make(map[*ListNode]struct{})

func detectCycle(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return nil
    }

    if _, ok := visited[head]; ok {
        return head
    }

    visited[head] = struct{}{}
    return detectCycle(head.Next)
}
```

[他の方](https://github.com/hroc135/leetcode/pull/2)の以下の回答のように、関数を定義するのはできるらしい、、、
```Go
func detectCycle(head *ListNode) *ListNode {
    visited := make(map[*ListNode]struct{})
    return checkNode(head, visited)
}

func checkNode(node *ListNode, visited map[*ListNode]struct{}) *ListNode {
    if node == nil {
        return nil
    }

    if _, exist := visited[node]; exist {
        return node
    }

    visited[node] = struct{}{}
    return checkNode(node.Next, visited)
}
```

メモ

**slowポインタとfastポインタが始めに出会った地点が、サイクルの開始点となるロジックについて**

M（slowポインタとfastポインタが始めに出会った地点）は、長さKのサイクルをC周した地点であるため、K*Cと書ける。
循環を検出した時点で、startポインタはリストの先頭に、slowはMの地点にいる。
startポインタがL（サイクルの開始地点）まで進むとき、slowポインタもLだけ進み、M+Lの地点にいる。
M+L=K*C+Lと式変形でき、LからK*C進んだ地点はLとなる。
したがって、startポインタは、Lだけ進んだ時にslowポインタと出会い、その地点がサイクルの開始地点となる。

### Step3（関連知識を調べる）
