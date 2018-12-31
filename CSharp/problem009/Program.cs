using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace projectEuler.problem009
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
             * a^2 + b^2 = c^2
             * a + b + c = 1000
             * 
             * c = sqrt(a^2 + b^2)
             * c = 1000 - a - b
             * 
             */

            for (int a = 1; a < 1000; a++)
            {
                for (int b = 1; b < 1000; b++)
                {
                    double c = Math.Sqrt(a * a + b * b);
                    if (Math.Truncate(c) == c)
                    {
                        if (a + b + c == 1000)
                        {
                            Console.WriteLine(a * b * c);
                        }
                    }
                }
            }
            Console.ReadLine();
        }
    }
}
