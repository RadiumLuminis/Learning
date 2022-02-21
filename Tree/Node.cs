using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BinaryTree
{
    class Node
    {
        public int value;
        public Node left, right;

        public Node(int item)
        {
            value = item;
            left = right = null;
        }
    }

    public class Forest
    {//builds the three
        private Node root = null;

        public Forest()
        {
            root = null;
        }

        public void insert(int key)
        {//aufruf aus code für start rekursion
            root = insertRec(root, key);
        }

        private Node insertRec(Node root, int key)
        {
            if (root == null)
            {
                root = new Node(key);
                return root;
            }

            if (key < root.value)
            {
                root.left = insertRec(root.left, key);
            }
            else if (key > root.value)
            {
                root.right = insertRec(root.right, key);
            }
            return root;
        }

        public void outputTree()
        {
            outputTreeRec(root);
        }

        private void outputTreeRec(Node root)
        {
            if (root != null)
            {
                outputTreeRec(root.left);
                Console.WriteLine(root.value);
                outputTreeRec(root.right);
            }
        }


    }
}
