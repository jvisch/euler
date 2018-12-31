using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace projectEuler.problem005
{
    class Program
    {
        static void Main(string[] args)
        {
            long max = 40;
            var fac = max * (max -1);
            var i = 0L;
            while (true)
            {
                i+= fac ;
                for(var j=2; j<=max; j++)
                {
                    if (i % j > 0)
                        break; ;
                    if (j == max)
                    {
                        Console.WriteLine(i);
                        Console.ReadLine();
                        return;
                    }
                }

            }
        }
    }
}
