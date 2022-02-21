﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BinaryTree
{
    class Program
    {

        static void Main(string[] args)
        {

            Forest gump = new Forest();



            /* Let us create following BST (Binary Sorted Tree)

                  50
               /      \
              30      70
             /  \     /  \
            20    40    60    80                            */

            gump.insert(50);
            gump.insert(30);
            gump.insert(20);
            gump.insert(40);
            gump.insert(70);
            gump.insert(60);
            gump.insert(80);

            gump.outputTree();

            gump.deleteValue(50);

            gump.outputTree();

        }
    }
}
