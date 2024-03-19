# Клас, що представляє вузол у дереві
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Функція для пошуку мінімального значення в дереві
def find_min_value(root):
    # Якщо корінь дерева не існує, повертаємо None
    if root is None:
        return None
    
    # Ідемо ліворуч, доки не знайдемо останній вузол
    while root.left is not None:
        root = root.left
    
    # Повертаємо значення останнього вузла, яке є мінімальним
    return root.value

# Приклад використання
# Збудуємо BST з числами
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

# Знаходимо мінімальне значення
min_value = find_min_value(root)
print("Мінімальне значення в дереві:", min_value)