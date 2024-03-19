# Клас, що представляє вузол у дереві
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Функція для пошуку максимального значення в дереві
def find_max_value(root):
    # Якщо корінь дерева не існує, повертаємо None
    if root is None:
        return None
    
    # Ідемо праворуч, доки не знайдемо останній вузол
    while root.right is not None:
        root = root.right
    
    # Повертаємо значення останнього вузла, яке є максимальним
    return root.value

# Приклад використання
# Збудуємо BST з числами
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

# Знаходимо максимальне значення
max_value = find_max_value(root)
print("Максимальне значення в дереві:", max_value)