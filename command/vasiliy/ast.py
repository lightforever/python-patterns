from operator import mul, add, sub


class AST:
    class Node:
        def __init__(self, left_arg=None, right_arg=None, op=None):
            self.op = op
            self.left_arg = left_arg
            self.right_arg = right_arg

    def __init__(self, root):
        self._root = root

    @staticmethod
    def _eval(root):
        if isinstance(root.left_arg, AST.Node):
            left = AST._eval(root.left_arg)
        else:
            left = root.left_arg

        if isinstance(root.right_arg, AST.Node):
            right = AST._eval(root.right_arg)
        else:
            right = root.right_arg

        if root.op is None:
            return left or right
        else:
            return root.op(left, right)

    def eval(self):
        return AST._eval(self._root)


if __name__ == '__main__':
    # 3+3*3-4-2
    tree = AST(
        AST.Node(
            AST.Node(
                AST.Node(
                    3,
                    AST.Node(
                        3,
                        3,
                        mul
                    ),
                    add,
                ),
                4,
                sub,
            ),
            2,
            sub,
        )
    )
    print(tree.eval())
