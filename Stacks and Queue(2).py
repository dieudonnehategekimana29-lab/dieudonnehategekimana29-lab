# Stack(rwanda) canvas, push(open module,"view notes,"take quiz")
# Queue(rwanda) RRA office,4 client arrive.after 2 served,who is next
# ---------------- STACK IMPLEMENTATION ----------------
    def __init__(self):
        self.data = []
    def push(self, x): self.data.append(x)
    def pop(self): return self.data.pop()
    def top(self): return self.data[-1] if self.data else None

print("\n================ STACK QUESTIONS ================")

# --- Practical 1 ---
stack = Stack()
stack.push("Open Module")
stack.push("View Notes")
stack.push("Take Quiz")

removed = stack.pop()   # Undo once

print("\n=== Practical 1: Canvas Navigation ===")
print("┌" + "─"*60 + "┐")
print(f"│ Removed Action: {removed:<44} │")
print(f"│ Current Stack: {stack.data} │")
print("└" + "─"*60 + "┘")

# --- Practical 2 ---
stack = Stack()
stack.push("Step1")
stack.push("Step2")
stack.push("Step3")

stack.pop()
stack.pop()

print("\n=== Practical 2: UR Steps ===")
print("┌" + "─"*30 + "┐")
print(f"│ Top element now: {stack.top():<12} │")
print("└" + "─"*30 + "┘")

# --- Challenge ---
# Algorithm:
# 1. Push "1", "2", "3"
# 2. Pop once
# 3. Push "4"
# 4. Top is "4"
stack = Stack()
stack.push("1")
stack.push("2")
stack.push("3")
stack.pop()
stack.push("4")

print("\n=== Challenge: Stack ===")
print("┌" + "─"*30 + "┐")
print(f"│ Top element is: {stack.top():<12} │")
print("└" + "─"*30 + "┘")

# --- Reflection ---
print("\n=== Reflection: Stack ===")
print("Stacks are efficient for reversing lists because popping returns elements in reverse order.")


# ---------------- QUEUE IMPLEMENTATION ----------------
print("\n================ QUEUE QUESTIONS ================")

# --- Practical 1 ---
queue = deque(["Client1", "Client2", "Client3", "Client4"])
queue.popleft()  # serve Client1
queue.popleft()  # serve Client2

print("\n=== Practical 1: RRA Office ===")
print("┌" + "─"*30 + "┐")
print(f"│ Next to be served: {queue[0]:<12} │")
print("└" + "─"*30 + "┘")

# --- Practical 2 ---
queue = deque(["C1", "C2", "C3", "C4", "C5"])

print("\n=== Practical 2: Airtel Shop ===")
print("┌" + "─"*30 + "┐")
print(f"│ Last served: {queue[-1]:<12} │")
print("└" + "─"*30 + "┘")

# --- Challenge ---
# Algorithm:
# 1. Enqueue buses
# 2. Dequeue some buses
# 3. Show why linear queue wastes space
queue = []
queue.append("Bus1")
queue.append("Bus2")
queue.pop(0)
queue.append("Bus3")

print("\n=== Challenge: Nyabugogo Buses ===")
print("Queue state:", queue)
print("Problem: Linear queue wastes space after many dequeues.")
print("Solution: Use circular queue with modulo index.")

# --- Reflection ---
print("\n=== Reflection: Queue ===")
print("FIFO is better than random serving because it is fair, predictable, and avoids conflicts.")
D