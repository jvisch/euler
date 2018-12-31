using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;

namespace projectEuler.problem015
{
    class Program
    {
        static long PathCount(int x, int y)
        {
            long result;
            if (x == 0 || y == 0)
            {
                result = 1;
            }
            else
            {
                result = PathCount(x - 1, y) + PathCount(x, y - 1);
            }
            return result;
        }

        static void Main(string[] args)
        {
            Thread.CurrentThread.Priority = ThreadPriority.BelowNormal;
            //Console.WriteLine(PathCount(1, 1));
            //Console.WriteLine(PathCount(2, 2));
            Console.WriteLine(PathCount(20,20));

            Console.ReadLine();
        }
    }
}
