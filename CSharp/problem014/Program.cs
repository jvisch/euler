using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace projectEuler.problem014
{
    class Program
    {
        static IEnumerable<long> Sequence(long startpoint)
        {
            while (startpoint > 1)
            {
                yield return startpoint;

                if(startpoint % 2 == 0)
                {
                    startpoint /= 2;
                }
                else
                {
                    startpoint = (3 * startpoint) + 1;
                }
            }
            yield return startpoint;
        }

        static void Main(string[] args)
        {
            int max = 0;
            int startpoint = 0;
            for (int i = 1; i < 1000000; i++)
            {
                int count = Sequence(i).Count();
                if (count >= max)
                {
                    startpoint = i;
                    max = count;
                    Console.WriteLine(startpoint + ": " + max);
                }
            }
            Console.WriteLine();
            Console.WriteLine("done " + startpoint + ": " + max);
            Console.ReadLine();
        }
    }
}
