using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace projectEuler.problem003.CSharp
{
    class Program
    {
        static List<long> FindFactors(long value)
        {
            List<long> factors = new List<long>();
            long factor = 2;
            while (factor < value)
            {
                if (value % factor == 0)
                {
                    factors.Add(factor);
                    do
                    {
                        value /= factor;
                    } while (value % factor == 0);
                }
                factor++;
            }
            if (value > 1)
            {
                factors.Add(value);
            }
            return factors;
        }

        static void Main(string[] args)
        {
            FindFactors(600851475143).ForEach(item => Console.WriteLine("  " + item));

            Console.ReadLine();
        }
    }
}
