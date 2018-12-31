using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;
using System.Diagnostics;

namespace projectEuler.problem012
{
    class Program
    {
        public static IEnumerable<int> Dividers(int value)
        {
            bool[] notdividable = new bool[value / 2];
            //for (int i = 0; i < dividable.Length; i++) dividable[i] = true;
            for (int i = 0; i < notdividable.Length; i++)
            {
                if (!notdividable[i])
                {
                    int divider = i + 1;
                    if (value % divider == 0)
                    {
                        yield return divider;
                    }
                    else
                    {
                        for (int j = i; j < notdividable.Length; j += divider)
                        {
                            notdividable[j] = true;
                        }
                    }
                }
                Thread.Sleep(0);
            }
            yield return value;
        }
        
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

        static int GetNrOfDividers(long value)
        {
            List<long> factors = FindFactors(value);
            int total = 1;
            foreach (long i in factors)
            {
                int count = 1;
                while (value % i == 0)
                {
                    value = value / i;
                    count++;
                }
                total *= count;
            }
            return total ;
        }

        static void Main(string[] args)
       {
           for (int x = 12; x < 100; x++)
           {
               int a = GetNrOfDividers(x);
               var c = Dividers(x);
               int b = c.Count();
               if (a != b)
               {
                   Debug.Assert(false);
               }
           }

            int maxcount = 0;
            Console.WriteLine("type startingpoint: ");
            int i = int.Parse(Console.ReadLine());
            long value = Enumerable.Range(0, i).Sum();
            while(true)
            {
                value += i;
                i++;
                
                int count = GetNrOfDividers(value);
                Console.WriteLine(i + " " + value + " " + count + ", count: " + maxcount);
                maxcount = Math.Max(maxcount, count);
                if (count >= 500 + 1)
                {
                    Console.WriteLine("found: " + value + " (" + i + ")");
                    break;
                }
            }

            Console.ReadLine();
        }
    }
}
