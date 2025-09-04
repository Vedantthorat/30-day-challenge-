def insert_at_bottom(stack, item):
  
    if not stack:  # If stack is empty, push the item
        stack.append(item)
    else:
        top = stack.pop()
        insert_at_bottom(stack, item)
        stack.append(top)  # Push the popped element back


def reverse_stack(stack):
   
    if stack:  
        top = stack.pop()
        reverse_stack(stack)  # Reverse remaining stack
        insert_at_bottom(stack, top)  # Insert popped element at bottom


stack = [1, 2, 3, 4]
reverse_stack(stack)
print(stack)  # Output: [4, 3, 2, 1]
