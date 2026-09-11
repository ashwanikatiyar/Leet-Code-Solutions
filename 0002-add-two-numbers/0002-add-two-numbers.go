/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    dummy := &ListNode{} // Start with dummy node (It give us easy starting point)
    cur := dummy
    carry := 0

    // Keep going while there is something to add
    for l1 != nil || l2 != nil || carry != 0 {

        // Get current digits (0 if list ended)
        a, b := 0, 0
        if l1 != nil {
            a = l1.Val
            l1 = l1.Next
        }
        if l2 != nil {
            b = l2.Val
            l2 = l2.Next
        }

        // Add digits + carry
        sum := a + b + carry

        // Current digit + carry for next round
        digit := sum % 10
        carry = sum / 10

        // Add digit to result
        cur.Next = &ListNode{Val: digit}
        cur = cur.Next
    }

    return dummy.Next // Skip dummy and return the next one
}

// 🧠 Remember the pattern
// Every loop:

// get → add → digit → carry → attach

// Get a and b
// Add a + b + carry
// Digit = sum % 10
// Carry = sum / 10
// Attach digit to result