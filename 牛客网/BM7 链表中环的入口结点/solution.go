package main

func EntryNodeOfLoop(pHead *ListNode) *ListNode {
	var fast, slow = pHead, pHead
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
		if fast == nil || slow.Val == fast.Val {
			// 快指针指向队尾，或两指针相遇
			break
		}
	}

	// 无环
	if fast == nil || fast.Next == nil {
		return nil
	}

	for pHead.Val != slow.Val {
		pHead = pHead.Next
		slow = slow.Next
	}

	return pHead
}
