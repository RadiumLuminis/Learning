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
    {
        private Node root = null;
        public Forest()
        {
            root = null;
        }

        public void insert(int key)
        {
            root = insertRec(root, key);
        }

        private Node insertRec(Node root, int key)
        {
            if (root == null)
            {
                root = new Node(key);
                return root;
            }


        }
    }



    class Program
    {
        static void Main(string[] args)
        {
        }
    }
}
