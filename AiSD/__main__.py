from TreeNode import TreeNode, print

def main():
    lisc1 = TreeNode(1)
    lisc2 = TreeNode(2)
    lisc3 = TreeNode(3)
    lisc4 = TreeNode(4)
    lisc5 = TreeNode(5)

    lisc1.add(lisc5)
    lisc1.add(lisc3)
    lisc3.add(lisc2)
    lisc3.add(lisc4)

    print(lisc1.is_leaf())
    print(lisc2.is_leaf())
    print(lisc3.is_leaf())
    print(lisc4.is_leaf())
    print(lisc5.is_leaf())



    lisc1.for_each_deep_first(print)
    #lisc1.for_each_level_order(print)


if __name__ == '__main__':
    main()
