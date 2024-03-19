# Клас, що представляє вузол у дереві
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Функція для обходу дерева в глибину і знаходження суми всіх значень
def find_tree_sum(root):
    # Якщо корінь дерева не існує, повертаємо 0
    if root is None:
        return 0
    
    # Обхід дерева в глибину (DFS) за допомогою рекурсії
    # Додаємо значення поточного вузла до суми та рекурсивно обходимо лівий і правий піддерева
    return root.value + find_tree_sum(root.left) + find_tree_sum(root.right)

# Приклад використання
# Збудуємо BST з числами
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

# Знаходимо суму всіх значень в дереві
tree_sum = find_tree_sum(root)
print("Сума всіх значень в дереві:", tree_sum)