using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace projectEuler.problem006
{
    class Program
    {
        static IEnumerable<int> Next(int start)
        {
            int i = start;
            while (true)
            {
                yield return i;
                i++;
            }
        }

        static void Main(string[] args)
        {
            var numbers = Next(1).Take(100);
            var total1 = numbers.Sum();
            total1 *= total1;

            var total2 = numbers.Select(x => x * x).Sum();

            Console.WriteLine(total1);
            Console.WriteLine(total2);
            Console.WriteLine(total1-total2);
            Console.ReadLine();
        }
    }
}
